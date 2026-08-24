#!/usr/bin/env python3
"""Collect article metadata from the server-rendered DMM Daily News page."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin


BASE_URL = "https://eikaiwa.dmm.com"
INDEX_URL = f"{BASE_URL}/app/daily-news"
SEARCH_URL = f"{INDEX_URL}/search"


@dataclass
class Article:
    title: str
    level: int | None
    difficulty: str | None
    published_at: str | None
    url: str


class DailyNewsParser(HTMLParser):
    VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.articles: list[Article] = []
        self._href: str | None = None
        self._depth = 0
        self._texts: list[str] = []
        self._heading_depth = 0
        self._heading_texts: list[str] = []
        self._published_at: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        href = values.get("href")
        if self._href is None and tag == "a" and href and "/app/daily-news/article/" in href:
            self._href = href
            self._depth = 1
            self._texts = []
            self._heading_texts = []
            self._published_at = None
            return
        if self._href is not None:
            if tag not in self.VOID_TAGS:
                self._depth += 1
            if tag == "h2":
                self._heading_depth = 1
            elif self._heading_depth:
                self._heading_depth += 1
            if tag == "time":
                self._published_at = values.get("datetime")

    def handle_endtag(self, tag: str) -> None:
        if self._href is None:
            return
        if self._heading_depth:
            self._heading_depth -= 1
        self._depth -= 1
        if self._depth == 0:
            self._finish_article()

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            text = " ".join(data.split())
            if text:
                self._texts.append(text)
                if self._heading_depth:
                    self._heading_texts.append(text)

    def _finish_article(self) -> None:
        difficulty_index = next(
            (i for i, text in enumerate(self._texts) if text in {"Intermediate", "Advanced", "Proficient"}),
            None,
        )
        difficulty = self._texts[difficulty_index] if difficulty_index is not None else None
        level = None
        if difficulty_index is not None and difficulty_index > 0:
            candidate = self._texts[difficulty_index - 1]
            level = int(candidate) if candidate.isdigit() else None

        ignored = {"Intermediate", "Advanced", "Proficient"}
        heading_title = " ".join(self._heading_texts)
        if heading_title == "New":
            heading_title = ""
        inferred_title = ""
        if difficulty_index is not None and difficulty_index >= 2:
            inferred_title = self._texts[difficulty_index - 2]
        title = heading_title or inferred_title or next(
            (
                text
                for text in self._texts
                if text not in ignored and not text.isdigit() and not self._looks_like_relative_date(text)
            ),
            "",
        )
        if title:
            self.articles.append(
                Article(title, level, difficulty, self._published_at, urljoin(BASE_URL, self._href or ""))
            )
        self._href = None
        self._texts = []
        self._heading_texts = []

    @staticmethod
    def _looks_like_relative_date(text: str) -> bool:
        markers = ("前", "ago", "昨日", "今日", "hour", "day", "month", "year")
        return any(marker in text for marker in markers)


def fetch(url: str) -> str:
    try:
        result = subprocess.run(
            ["curl", "-fsSL", "--max-time", "30", url],
            check=True,
            capture_output=True,
        )
    except FileNotFoundError as error:
        raise RuntimeError("curl is required to download the DMM page") from error
    except subprocess.CalledProcessError as error:
        message = error.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"failed to download DMM Daily News: {message}") from error
    return result.stdout.decode("utf-8")


def parse(html: str) -> list[Article]:
    parser = DailyNewsParser()
    parser.feed(html)
    # The page can repeat cards in responsive/featured sections.
    return list({article.url: article for article in parser.articles}.values())


def has_next_page(html: str, current_page: int) -> bool:
    pages = {
        int(value)
        for value in re.findall(r'href="/app/daily-news/search\?[^"#]*\bpage=(\d+)', html)
    }
    return current_page + 1 in pages


def fetch_all_pages(delay: float, max_pages: int | None = None) -> list[Article]:
    collected: dict[str, Article] = {}
    page = 1
    while max_pages is None or page <= max_pages:
        separator = "&" if "?" in SEARCH_URL else "?"
        page_url = f"{SEARCH_URL}{separator}page={page}"
        html = fetch(page_url)
        articles = parse(html)
        # Some older result pages intermittently return only the client-side
        # loading shell. A changing query parameter bypasses that bad cache.
        for retry in range(1, 6):
            if articles:
                break
            html = fetch(f"{page_url}&collector_retry={retry}")
            articles = parse(html)
        new_count = 0
        for article in articles:
            if article.url not in collected:
                collected[article.url] = article
                new_count += 1
        print(
            f"page {page}: {len(articles)} articles ({new_count} new, {len(collected)} total)",
            file=sys.stderr,
        )
        if not articles or not new_count or not has_next_page(html, page):
            break
        page += 1
        if delay:
            time.sleep(delay)
    return list(collected.values())


def main() -> int:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--input", type=Path, help="Parse saved HTML instead of downloading the page")
    arg_parser.add_argument("--all-pages", action="store_true", help="Follow search result pages until the end")
    arg_parser.add_argument("--delay", type=float, default=0.3, help="Seconds between page requests (default: 0.3)")
    arg_parser.add_argument("--max-pages", type=int, help="Stop after this many pages (useful for testing)")
    arg_parser.add_argument("--output", type=Path, help="Write JSON to a file instead of stdout")
    arg_parser.add_argument("--min-level", type=int)
    arg_parser.add_argument("--max-level", type=int)
    arg_parser.add_argument("--limit", type=int)
    arg_parser.add_argument("--pretty", action="store_true")
    args = arg_parser.parse_args()

    if args.input and args.all_pages:
        arg_parser.error("--input and --all-pages cannot be used together")
    if args.delay < 0:
        arg_parser.error("--delay must be zero or greater")

    if args.all_pages:
        articles = fetch_all_pages(args.delay, args.max_pages)
    else:
        html = args.input.read_text(encoding="utf-8") if args.input else fetch(INDEX_URL)
        articles = parse(html)
    if args.min_level is not None:
        articles = [a for a in articles if a.level is not None and a.level >= args.min_level]
    if args.max_level is not None:
        articles = [a for a in articles if a.level is not None and a.level <= args.max_level]
    if args.limit is not None:
        articles = articles[: args.limit]

    output = args.output.open("w", encoding="utf-8") if args.output else sys.stdout
    try:
        json.dump(
            [asdict(article) for article in articles],
            output,
            ensure_ascii=False,
            indent=2 if args.pretty else None,
        )
        output.write("\n")
    finally:
        if args.output:
            output.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
