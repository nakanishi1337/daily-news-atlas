import { test, expect } from '@playwright/test';
import { readFileSync } from 'node:fs';

const data = JSON.parse(readFileSync('site/data/articles.json', 'utf8'));
const all = data.articles;
const count = articles => `${articles.length.toLocaleString('ja-JP')} 記事`;

test.beforeEach(async ({ page }) => {
  // The app must work without external font access.
  await page.route('https://fonts.googleapis.com/**', route => route.abort());
  await page.goto('/');
  await expect(page.locator('#match-count')).toHaveText(count(all));
});

test('facets use OR within one facet and AND between facets; state survives reload', async ({ page }) => {
  await page.locator('#region-filters [data-value="Japan"]').click();
  await expect(page.locator('#match-count')).toHaveText(count(all.filter(a => a.regions.includes('Japan'))));
  await page.locator('#region-filters [data-value="South Korea"]').click();
  await page.locator('#level-filters [data-value="6"]').click();
  const matching = all.filter(a => (a.regions.includes('Japan') || a.regions.includes('South Korea')) && a.level === 6);
  await expect(page.locator('#match-count')).toHaveText(count(matching));
  await page.reload();
  await expect(page.locator('#match-count')).toHaveText(count(matching));
  await expect(page.locator('#region-filters [data-value="Japan"]')).toHaveAttribute('aria-pressed', 'true');
  await page.locator('#reset-filters').click();
  await expect(page.locator('#match-count')).toHaveText(count(all));
});

test('search, list selection, source link and embedding neighbors work together', async ({ page }) => {
  const article = all.find(a => a.title.includes('AI Uptake')) || all[0];
  await page.locator('#search').fill(article.title);
  await page.locator('#list-view').click();
  await page.locator(`[data-article="${article.id}"]`).first().click();
  await expect(page.locator('.article-title')).toHaveText(article.title);
  await expect(page.locator('#article-detail .primary-link')).toHaveAttribute('href', article.url);
  await expect(page.locator('.similar-article')).toHaveCount(article.similar.length);
  await page.locator('.similar-article').first().click();
  await expect(page.locator('.article-title')).toHaveText(all.find(a => a.id === article.similar[0]).title);
  await page.reload();
  await expect(page.locator('.article-title')).toHaveText(all.find(a => a.id === article.similar[0]).title);
  await expect(page.locator('#list-panel')).toBeVisible();
});

test('AI uses the Topic filter and old Theme URLs migrate to Topic', async ({ page }) => {
  await expect(page.locator('#theme-filters')).toHaveCount(0);
  const aiArticles = all.filter(a => a.topics.includes('AI'));
  await page.locator('#discovery-tags [data-value="AI"]').click();
  await expect(page.locator('#match-count')).toHaveText(count(aiArticles));
  await expect(page).toHaveURL(/topics=AI/);
  await expect(page.locator('#topic-filters [data-value="AI"]')).toHaveAttribute('aria-pressed', 'true');
  await page.goto('/?themes=AI');
  await expect(page.locator('#match-count')).toHaveText(count(aiArticles));
  await expect(page).toHaveURL(/topics=AI/);
  expect(new URL(page.url()).searchParams.has('themes')).toBe(false);
});

test('categories expand to subtopics and combine with OR inside the Topic facet', async ({ page }) => {
  const food = page.locator('[data-category="Food & Drink"]');
  await expect(food.locator('.subtopics')).toBeHidden();
  await food.locator('[data-facet="categories"]').click();
  await expect(page.locator('#match-count')).toHaveText(count(all.filter(a => a.categories.includes('Food & Drink'))));
  await food.locator('[data-toggle-category]').click();
  await expect(food.locator('[data-toggle-category]')).toHaveAttribute('aria-expanded', 'true');
  await page.locator('[data-category="Travel & Transport"] [data-toggle-category]').click();
  await page.locator('#topic-filters [data-value="Trains"]').click();
  const matching = all.filter(a => a.categories.includes('Food & Drink') || a.topics.includes('Trains'));
  await expect(page.locator('#match-count')).toHaveText(count(matching));
  await expect(page).toHaveURL(/categories=Food/);
  await page.reload();
  await expect(page.locator('#match-count')).toHaveText(count(matching));
  // A row with a selected subtopic opens on load, so the selection stays visible.
  await expect(page.locator('#topic-filters [data-value="Trains"]')).toBeVisible();
  await expect(page.locator('.active-filter')).toHaveText(['食・飲み物×', '鉄道×']);
});

test('Japanese topic labels are searchable', async ({ page }) => {
  await page.locator('#search').fill('和食');
  await expect(page.locator('#match-count')).toHaveText(count(all.filter(a => a.topics.includes('Japanese Food'))));
});

test('date range, pagination, sorting and empty state', async ({ page }) => {
  await page.locator('#date-from').fill('2026-09-01');
  await page.locator('#date-to').fill('2026-09-23');
  const matching = all.filter(a => a.date >= '2026-09-01' && a.date <= '2026-09-23');
  await expect(page.locator('#match-count')).toHaveText(count(matching));
  await page.locator('#list-view').click();
  await page.locator('#next-page').click();
  await expect(page.locator('#page-info')).toContainText('2 /');
  await page.locator('#sort').selectOption('level');
  const levels = await page.locator('.article-row .level-badge').allTextContents();
  expect(levels.map(s => Number(s.replace('Level ', '')))).toEqual(levels.map(s => Number(s.replace('Level ', ''))).sort((a, b) => a - b));
  await page.locator('#date-from').fill('2026-09-23');
  await page.locator('#date-to').fill('2026-09-01');
  await expect(page.locator('#date-error')).toBeVisible();
  await expect(page.locator('#match-count')).toHaveText('0 記事');
  await page.locator('#reset-filters').click();
  await page.locator('#search').fill('xyz-not-a-real-article-91827');
  await expect(page.locator('.empty-list')).toBeVisible();
});

test('map points can be clicked and zoomed; filters do not change coordinates', async ({ page }) => {
  const article = all.find(a => a.x > .25 && a.x < .75 && a.y > .3 && a.y < .7);
  // Isolate a title while keeping the original map position.
  await page.locator('#search').fill(article.title);
  const bounds = await page.locator('#map').boundingBox();
  const x = bounds.width / 2 + (article.x - .5) * (bounds.width - 100);
  const y = bounds.height / 2 + (article.y - .5) * (bounds.height - 100);
  await page.locator('#map').click({ position: { x, y } });
  await expect(page.locator('.article-title')).toHaveText(article.title);
  await page.locator('#zoom-in').click();
  await page.locator('#fit-map').click();
  await page.locator('#map').click({ position: { x, y } });
  await expect(page.locator('.article-title')).toHaveText(article.title);
});

test('long article details do not resize or move the map, including after zooming', async ({ page }) => {
  const article = all.find(a => a.x > .35 && a.x < .65 && a.y > .35 && a.y < .65);
  const longTitle = 'A long article title about technology, travel and everyday life '.repeat(5);
  const modified = {
    ...data,
    articles: all.map(a => a.id === article.id ? {
      ...a, title: longTitle, regions: Array.from({ length: 30 }, (_, i) => `Additional region ${i}`),
    } : a),
  };
  await page.route('**/data/articles.json', route => route.fulfill({ json: modified }));
  for (const viewportWidth of [1024, 1440, 1680]) {
    await page.setViewportSize({ width: viewportWidth, height: 1100 });
    await page.goto('/');
    await expect(page.locator('#match-count')).toHaveText(count(all));
    await page.locator('#search').fill(longTitle);
    const before = await page.locator('#map').boundingBox();
    const x = before.width / 2 + (article.x - .5) * (before.width - 100);
    const y = before.height / 2 + (article.y - .5) * (before.height - 100);
    await page.locator('#map').click({ position: { x, y } });
    await expect(page.locator('.article-title')).toHaveText(longTitle);
    await expect.poll(async () => page.locator('#map').boundingBox()).toEqual(before);
    expect(await page.locator('#detail-panel').evaluate(el => el.scrollHeight > el.clientHeight)).toBe(true);
    await page.locator('#zoom-in').click();
    await page.locator('.similar-article').first().click();
    await expect(page.locator('.article-title')).not.toHaveText(longTitle);
    expect(await page.locator('#map').boundingBox()).toEqual(before);
    await page.locator('[data-close-detail]').click();
    expect(await page.locator('#map').boundingBox()).toEqual(before);
  }
});

test('mobile layout fits and details are accessible', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  await page.locator('#list-view').click();
  await page.locator('.article-row').first().click();
  await expect(page.locator('.article-title')).toBeVisible();
  await expect(page.locator('#article-detail .primary-link')).toBeVisible();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
});

test('map fits in the initial viewport and mobile filters can be opened', async ({ page }) => {
  for (const size of [{ width: 1440, height: 900 }, { width: 1024, height: 768 }, { width: 390, height: 844 }]) {
    await page.setViewportSize(size);
    const bounds = await page.locator('#map').boundingBox();
    expect(bounds.y + bounds.height).toBeLessThanOrEqual(size.height);
    expect(await page.locator('.filter-note').count()).toBe(0);
  }
  await expect(page.locator('#topic-filters')).toBeHidden();
  await page.locator('#toggle-filters').click();
  await expect(page.locator('#topic-filters')).toBeVisible();
  await page.locator('[data-category="Health & Body"] [data-toggle-category]').click();
  await page.locator('#topic-filters [data-value="Sleep"]').click();
  await expect(page.locator('#match-count')).toHaveText(count(all.filter(a => a.topics.includes('Sleep'))));
  await page.locator('#toggle-filters').click();
  await expect(page.locator('#topic-filters')).toBeHidden();
  await expect(page.locator('#toggle-filters')).toHaveAttribute('aria-expanded', 'false');
});

test('failed JSON request offers a working retry', async ({ page }) => {
  let fail = true;
  await page.route('**/data/articles.json', route => fail ? route.fulfill({ status: 503, body: 'Unavailable' }) : route.continue());
  await page.reload();
  await expect(page.locator('#match-count')).toHaveText('読み込みエラー');
  fail = false;
  await page.locator('#retry').click();
  await expect(page.locator('#match-count')).toHaveText(count(all));
});
