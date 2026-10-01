"""Protect the existing archive when collecting incremental updates."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "collect_daily_news.py"


class IncrementalCollectionTest(unittest.TestCase):
    def test_merge_keeps_old_articles_and_refreshes_existing_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "articles.json"
            existing = [{"title": "Old article", "url": "https://eikaiwa.dmm.com/app/daily-news/article/old/id", "level": 5, "difficulty": "Intermediate", "published_at": "2020-01-01T00:00:00Z"}, {"title": "Outdated title", "url": "https://eikaiwa.dmm.com/app/daily-news/article/new/id", "level": 5, "difficulty": "Intermediate", "published_at": "2026-09-01T00:00:00Z"}]
            output.write_text(json.dumps(existing))
            html = root / "input.html"
            html.write_text('<a href="/app/daily-news/article/new/id"><h2>Updated article</h2><span>6</span><span>Intermediate</span><time datetime="2026-09-23T17:00:00Z">Today</time></a>')
            subprocess.run([sys.executable, str(SCRIPT), "--input", str(html), "--merge", str(output), "--output", str(output)], check=True)
            result = json.loads(output.read_text())
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0]["title"], "Updated article")
            self.assertEqual(result[0]["level"], 6)
            self.assertEqual(result[1], existing[0])

    def test_empty_response_does_not_overwrite_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "articles.json"
            output.write_text('[{"sentinel": true}]')
            html = root / "empty.html"
            html.write_text('<html>Please enable JavaScript</html>')
            result = subprocess.run([sys.executable, str(SCRIPT), "--input", str(html), "--output", str(output)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(output.read_text(), '[{"sentinel": true}]')


if __name__ == "__main__":
    unittest.main()
