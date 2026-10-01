import { cp, mkdir, readFile, rm } from 'node:fs/promises';

const data = JSON.parse(await readFile('site/data/articles.json', 'utf8'));
const ids = new Set(data.articles.map(a => a.id));
if (!data.articles.length || ids.size !== data.articles.length) throw new Error('Invalid article IDs');
for (const a of data.articles) {
  if (!Number.isFinite(a.x) || !Number.isFinite(a.y) || a.similar.some(id => !ids.has(id) || id === a.id)) {
    throw new Error(`Invalid map data: ${a.id}`);
  }
}
await rm('dist', { recursive: true, force: true });
await mkdir('dist');
await cp('site', 'dist', { recursive: true });
console.log(`Static site built: dist/ (${data.articles.length.toLocaleString()} articles)`);
