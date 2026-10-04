const $ = id => document.getElementById(id);
const fmt = n => n.toLocaleString('ja-JP');
const escapeHTML = value => String(value ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const facets = ['categories', 'topics', 'regions', 'levels'];
const state = { categories: new Set(), topics: new Set(), regions: new Set(), levels: new Set(), query: '', from: '', to: '', view: 'map', sort: 'date-desc', page: 0, selected: null };
let data, articles = [], matches = [], byId, categoryInfo, topicInfo, matchingIds = new Set();
let width = 0, height = 0, zoom = 1, panX = 0, panY = 0, frame = 0, hovered = null;
const canvas = $('map'), ctx = canvas.getContext('2d');
const pageSize = 12;
// Phones start with the list, which is easier to scan and tap than the map.
const defaultView = () => matchMedia('(max-width: 620px)').matches ? 'list' : 'map';

function loadURL() {
  const params = new URLSearchParams(location.search);
  for (const key of facets) {
    const allowed = key === 'levels' ? [...new Set(articles.map(a => String(a.level)).filter(x => x !== 'null'))] : data.facets[key].map(v => typeof v === 'string' ? v : v.name);
    state[key] = new Set(params.getAll(key).filter(value => allowed.includes(value)));
  }
  if (params.getAll('themes').includes('AI')) state.topics.add('AI');
  state.query = params.get('q') || '';
  for (const [key, param] of [['from', 'from'], ['to', 'to']]) {
    const value = params.get(param) || '';
    state[key] = /^\d{4}-\d{2}-\d{2}$/.test(value) ? value : '';
  }
  state.view = ['map', 'list'].includes(params.get('view')) ? params.get('view') : defaultView();
  state.selected = byId.has(params.get('article')) ? params.get('article') : null;
  $('search').value = state.query;
  $('date-from').value = state.from;
  $('date-to').value = state.to;
}

function saveURL() {
  const params = new URLSearchParams();
  for (const key of facets) for (const value of state[key]) params.append(key, value);
  if (state.query) params.set('q', state.query);
  if (state.from) params.set('from', state.from);
  if (state.to) params.set('to', state.to);
  if (state.view !== defaultView()) params.set('view', state.view);
  if (state.selected) params.set('article', state.selected);
  history.replaceState(null, '', `${location.pathname}${params.size ? `?${params}` : ''}${location.hash}`);
}

function createFilters() {
  const counts = { categories: new Map(), topics: new Map() };
  for (const a of articles) for (const key of ['categories', 'topics']) for (const name of a[key]) counts[key].set(name, (counts[key].get(name) || 0) + 1);
  $('topic-filters').innerHTML = data.facets.categories.map((c, i) => {
    const topics = data.facets.topics.filter(t => t.category === c.name && counts.topics.get(t.name)).sort((a, b) => counts.topics.get(b.name) - counts.topics.get(a.name));
    return `<div class="category" data-category="${escapeHTML(c.name)}"><div class="category-row"><button class="topic-option" data-facet="categories" data-value="${escapeHTML(c.name)}" aria-pressed="false"><i style="background:${c.color}"></i><span class="topic-label">${escapeHTML(c.label)}</span><span class="topic-count">${fmt(counts.categories.get(c.name) || 0)}</span></button><button class="category-toggle" data-toggle-category aria-expanded="false" aria-controls="subtopics-${i}" aria-label="${escapeHTML(c.label)} の小カテゴリー">${topics.length}<span aria-hidden="true">▾</span></button></div><div id="subtopics-${i}" class="subtopics" hidden>${topics.map(t => `<button class="subtopic" data-facet="topics" data-value="${escapeHTML(t.name)}" aria-pressed="false">${escapeHTML(t.label)}<span>${fmt(counts.topics.get(t.name))}</span></button>`).join('')}</div></div>`;
  }).join('');
  for (const facet of ['regions']) {
    $('region-filters').innerHTML = data.facets[facet].map(name => `<button class="chip" data-facet="${facet}" data-value="${escapeHTML(name)}" aria-pressed="false">${escapeHTML(name)}</button>`).join('');
  }
  $('level-filters').innerHTML = [...new Set(articles.map(a => a.level).filter(n => Number.isInteger(n)))].sort((a, b) => a - b).map(n => `<button class="level-option" data-facet="levels" data-value="${n}" aria-label="Level ${n}" aria-pressed="false">${n}</button>`).join('');
  $('discovery-tags').innerHTML = [['regions', 'Japan', '日本の記事'], ['topics', 'AI', 'AIの記事'], ['topics', 'Travel', '旅行の記事']].map(([facet, value, label]) => `<button data-facet="${facet}" data-value="${value}">${label}<span>↗</span></button>`).join('');
}

function matchesSet(selected, values) { return selected.size === 0 || values.some(value => selected.has(String(value))); }
// Categories and topics are one facet: an article matches if it has any selected category or topic.
function matchesTopic(a) { return (!state.categories.size && !state.topics.size) || a.categories.some(c => state.categories.has(c)) || a.topics.some(t => state.topics.has(t)); }
function setCategoryOpen(category, open) {
  category.querySelector('[data-toggle-category]').setAttribute('aria-expanded', String(open));
  category.querySelector('.subtopics').hidden = !open;
}
function updateFilters() {
  const terms = state.query.trim().toLowerCase().split(/\s+/).filter(Boolean);
  const invalidDate = Boolean(state.from && state.to && state.from > state.to);
  $('date-error').hidden = !invalidDate;
  matches = invalidDate ? [] : articles.filter(a => terms.every(term => a.searchText.includes(term)) && matchesTopic(a) && matchesSet(state.regions, a.regions) && matchesSet(state.levels, [a.level]) && (!state.from || a.date >= state.from) && (!state.to || (a.date && a.date <= state.to)));
  matchingIds = new Set(matches.map(a => a.id));
  state.page = 0;
  hovered = null;
  $('map-tooltip').hidden = true;
  $('match-count').textContent = `${fmt(matches.length)} 記事`;
  for (const button of document.querySelectorAll('[data-facet]')) button.setAttribute('aria-pressed', String(state[button.dataset.facet].has(button.dataset.value)));
  // Keep selected subtopics visible.
  for (const category of document.querySelectorAll('.category')) if (category.querySelector('.subtopic[aria-pressed=true]')) setCategoryOpen(category, true);
  const active = [];
  for (const facet of facets) for (const value of state[facet]) {
    const label = facet === 'levels' ? `Lv. ${value}` : facet === 'regions' ? value : (facet === 'categories' ? categoryInfo : topicInfo).get(value)?.label || value;
    active.push(`<button class="active-filter" data-facet="${facet}" data-value="${escapeHTML(value)}" aria-label="${escapeHTML(label)} の絞り込みを解除">${escapeHTML(label)}<span>×</span></button>`);
  }
  $('active-filters').innerHTML = active.join('');
  $('active-filters').hidden = !active.length;
  if (!matches.length) {
    $('map-status').innerHTML = '<p>条件に一致する記事はありません。<br>検索語や絞り込み条件を変更してください。</p><button data-reset>絞り込みをリセット</button>';
    $('map-status').hidden = false;
  } else $('map-status').hidden = true;
  renderList();
  requestDraw();
  saveURL();
}

function resetFilters() {
  for (const key of facets) state[key].clear();
  state.query = state.from = state.to = '';
  $('search').value = $('date-from').value = $('date-to').value = '';
  updateFilters();
}

function setView(view) {
  state.view = view;
  $('map-panel').hidden = view !== 'map';
  $('list-panel').hidden = view !== 'list';
  for (const name of ['map', 'list']) {
    $(`${name}-view`).classList.toggle('active', name === view);
    $(`${name}-view`).setAttribute('aria-pressed', String(name === view));
  }
  if (view === 'map') resize(); else renderList();
  saveURL();
}

function renderList() {
  const sorted = [...matches].sort((a, b) => {
    if (state.sort === 'date-asc') return a.date.localeCompare(b.date) || a.id.localeCompare(b.id);
    if (state.sort === 'level') return (a.level ?? 99) - (b.level ?? 99) || b.date.localeCompare(a.date);
    if (state.sort === 'title') return a.title.localeCompare(b.title, 'en');
    return b.date.localeCompare(a.date) || a.id.localeCompare(b.id);
  });
  const totalPages = Math.max(1, Math.ceil(sorted.length / pageSize));
  state.page = Math.min(state.page, totalPages - 1);
  const page = sorted.slice(state.page * pageSize, (state.page + 1) * pageSize);
  $('article-list').innerHTML = page.length ? page.map(a => {
    const category = categoryInfo.get(a.categories[0]);
    return `<button class="article-row ${a.id === state.selected ? 'selected' : ''}" data-article="${a.id}" aria-label="${escapeHTML(a.title)} の詳細"><span class="row-topic"><i class="tag-dot" style="background:${category.color}"></i>${escapeHTML(category.label)}</span><strong>${escapeHTML(a.title)}</strong><span class="row-meta"><span class="level-badge">${a.level == null ? 'Level 不明' : `Level ${a.level}`}</span><span>${a.date || '公開日不明'}</span>${[...a.topics.map(t => topicInfo.get(t).label), ...a.regions].slice(0, 3).map(t => `<span class="row-tag">${escapeHTML(t)}</span>`).join('')}</span></button>`;
  }).join('') : '<div class="empty-list"><strong>条件に一致する記事はありません</strong>検索語や絞り込み条件を変更してください。</div>';
  $('page-info').textContent = `${state.page + 1} / ${totalPages}`;
  $('prev-page').disabled = state.page === 0;
  $('next-page').disabled = state.page >= totalPages - 1;
}

function openArticle(id, scroll = false) {
  const a = byId.get(id);
  if (!a) return;
  state.selected = id;
  const category = categoryInfo.get(a.categories[0]);
  $('discovery').hidden = true;
  $('article-detail').hidden = false;
  $('article-detail').innerHTML = `<div class="detail-top"><span>記事詳細</span><button class="close-button" data-close-detail aria-label="記事の詳細を閉じる">×</button></div><div class="detail-topic"><i class="tag-dot" style="background:${category.color}"></i>${escapeHTML(category.label)}</div><h2 class="article-title">${escapeHTML(a.title)}</h2><div class="detail-meta"><span class="level-badge">${a.level == null ? 'Level 不明' : `Level ${a.level}`}</span><time datetime="${a.date}">${a.date || '公開日不明'}</time></div><div class="detail-tags">${[['categories', categoryInfo], ['topics', topicInfo], ['regions']].flatMap(([facet, info]) => a[facet].map(tag => `<button class="chip${facet === 'categories' ? ' category-chip' : ''}" data-facet="${facet}" data-value="${escapeHTML(tag)}" aria-pressed="${state[facet].has(tag)}">${escapeHTML(info ? info.get(tag).label : tag)}</button>`)).join('')}</div><a class="primary-link" href="${escapeHTML(a.url)}" target="_blank" rel="noopener noreferrer">DMMで記事を読む <span>↗</span></a><p class="source-note">DMM Daily News のサイトが開きます</p><div class="similar-heading"><h3>類似記事</h3></div>${a.similar.map(similarId => byId.get(similarId)).filter(Boolean).map(b => `<button class="similar-article" data-article="${b.id}"><strong>${escapeHTML(b.title)}</strong><small>Level ${b.level ?? '不明'} <span>·</span> ${b.date || '公開日不明'}</small></button>`).join('')}`;
  renderList();
  requestDraw();
  saveURL();
  $('detail-panel').scrollTop = 0;
  if (scroll && matchMedia('(max-width: 960px)').matches) $('detail-panel').scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block: 'start' });
}

function point(a) {
  const padding = 50;
  return [width / 2 + ((a.x - .5) * (width - padding * 2)) * zoom + panX, height / 2 + ((a.y - .5) * (height - padding * 2)) * zoom + panY];
}
function resize() {
  if (state.view !== 'map') return;
  const rect = $('map-panel').getBoundingClientRect();
  width = rect.width; height = rect.height;
  const dpr = Math.min(devicePixelRatio || 1, 2);
  canvas.width = Math.round(width * dpr); canvas.height = Math.round(height * dpr);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  requestDraw();
}
function requestDraw() {
  if (!frame) frame = requestAnimationFrame(() => { frame = 0; draw(); });
}
function draw() {
  if (!data || state.view !== 'map') return;
  ctx.clearRect(0, 0, width, height);
  const radius = Math.min(3.5, 1.65 + (zoom - 1) * .16);
  const filtered = matches.length !== articles.length;
  // Draw the context first and matching articles on top.
  for (const matching of [false, true]) {
    if (!filtered && !matching) continue;
    for (const a of articles) {
      if (matchingIds.has(a.id) !== matching) continue;
      const [x, y] = point(a);
      if (x < -10 || x > width + 10 || y < -10 || y > height + 10) continue;
      ctx.globalAlpha = matching ? (filtered ? .86 : .61) : .19;
      ctx.fillStyle = matching ? categoryInfo.get(a.categories[0]).color : '#bec8b9';
      ctx.beginPath(); ctx.arc(x, y, matching ? radius : 1.3, 0, Math.PI * 2); ctx.fill();
    }
  }
  ctx.globalAlpha = 1;
  const boxes = [];
  ctx.font = '500 11px "DM Sans", sans-serif';
  const topicFilter = state.categories.size + state.topics.size > 0;
  for (const label of data.labels) {
    const selected = state[label.kind === 'category' ? 'categories' : 'topics'].has(label.name);
    if (topicFilter ? !selected : zoom < (label.minZoom || 0)) continue;
    const [x, y] = point(label);
    const textWidth = ctx.measureText(label.name).width;
    const box = { x: x - textWidth / 2 - 7, y: y - 17, w: textWidth + 14, h: 22 };
    if (box.x < 8 || box.x + box.w > width - 8 || y < 94 || y > height - 45 || boxes.some(b => box.x < b.x + b.w + 5 && box.x + box.w + 5 > b.x && box.y < b.y + b.h + 5 && box.y + box.h + 5 > b.y)) continue;
    boxes.push(box);
    ctx.fillStyle = '#fafbf8e8'; ctx.beginPath(); ctx.roundRect(box.x, box.y, box.w, box.h, 4); ctx.fill();
    ctx.fillStyle = '#71836c'; ctx.textAlign = 'center'; ctx.fillText(label.name, x, y - 3);
  }
  for (const id of new Set([state.selected, hovered?.id])) {
    const a = byId.get(id); if (!a) continue;
    const [x, y] = point(a);
    const color = categoryInfo.get(a.categories[0]).color;
    ctx.fillStyle = color;
    ctx.strokeStyle = '#fff'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(x, y, 5, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
    ctx.strokeStyle = color; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.arc(x, y, 8, 0, Math.PI * 2); ctx.stroke();
  }
}
function hit(x, y) {
  let closest = null, best = 64;
  for (const a of matches) {
    const [px, py] = point(a);
    const distance = (px - x) ** 2 + (py - y) ** 2;
    if (distance < best) { closest = a; best = distance; }
  }
  return closest;
}
function zoomAt(factor, x = width / 2, y = height / 2) {
  const next = Math.max(.7, Math.min(14, zoom * factor));
  const ratio = next / zoom;
  panX = x - width / 2 - (x - width / 2 - panX) * ratio;
  panY = y - height / 2 - (y - height / 2 - panY) * ratio;
  zoom = next;
  $('map-tooltip').hidden = true;
  requestDraw();
}
let drag;
canvas.addEventListener('pointerdown', e => {
  if (e.button !== 0) return;
  drag = { id: e.pointerId, startX: e.clientX, startY: e.clientY, x: panX, y: panY, moved: false };
  canvas.setPointerCapture(e.pointerId);
  $('map-tooltip').hidden = true;
});
canvas.addEventListener('pointermove', e => {
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left, y = e.clientY - rect.top;
  if (drag && drag.id === e.pointerId) {
    if (Math.hypot(e.clientX - drag.startX, e.clientY - drag.startY) > 4) drag.moved = true;
    if (drag.moved) { panX = drag.x + e.clientX - drag.startX; panY = drag.y + e.clientY - drag.startY; hovered = null; requestDraw(); }
    return;
  }
  hovered = hit(x, y);
  canvas.style.cursor = hovered ? 'pointer' : 'grab';
  const tooltip = $('map-tooltip');
  tooltip.hidden = !hovered;
  if (hovered) {
    tooltip.innerHTML = `<strong>${escapeHTML(hovered.title)}</strong><small>Level ${hovered.level ?? '不明'} · ${hovered.date || '公開日不明'}</small>`;
    tooltip.style.left = `${Math.max(8, Math.min(x + 14, width - tooltip.offsetWidth - 8))}px`;
    tooltip.style.top = `${Math.max(8, Math.min(y + 14, height - tooltip.offsetHeight - 8))}px`;
  }
  requestDraw();
});
canvas.addEventListener('pointerup', e => {
  if (!drag || drag.id !== e.pointerId) return;
  if (!drag.moved) {
    const rect = canvas.getBoundingClientRect();
    const a = hit(e.clientX - rect.left, e.clientY - rect.top);
    if (a) openArticle(a.id, true);
  }
  drag = null;
});
canvas.addEventListener('pointercancel', () => { drag = null; });
canvas.addEventListener('pointerleave', () => { hovered = null; $('map-tooltip').hidden = true; requestDraw(); });
canvas.addEventListener('wheel', e => {
  e.preventDefault();
  const rect = canvas.getBoundingClientRect();
  zoomAt(Math.exp(-Math.max(-100, Math.min(100, e.deltaY)) * .002), e.clientX - rect.left, e.clientY - rect.top);
}, { passive: false });
canvas.addEventListener('keydown', e => {
  if (e.key === '+' || e.key === '=') zoomAt(1.25);
  else if (e.key === '-') zoomAt(.8);
  else if (e.key === '0') { zoom = 1; panX = panY = 0; requestDraw(); }
  else if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
    e.preventDefault(); panX += e.key === 'ArrowLeft' ? 30 : e.key === 'ArrowRight' ? -30 : 0;
    panY += e.key === 'ArrowUp' ? 30 : e.key === 'ArrowDown' ? -30 : 0; requestDraw();
  }
});

document.addEventListener('click', e => {
  if (!data) return;
  const facetButton = e.target.closest('[data-facet]');
  if (facetButton) {
    const { facet, value } = facetButton.dataset;
    if (state[facet].has(value)) state[facet].delete(value); else state[facet].add(value);
    updateFilters();
  }
  const toggle = e.target.closest('[data-toggle-category]');
  if (toggle) setCategoryOpen(toggle.closest('.category'), toggle.getAttribute('aria-expanded') !== 'true');
  const articleButton = e.target.closest('[data-article]');
  if (articleButton) openArticle(articleButton.dataset.article, true);
  if (e.target.closest('[data-reset]')) resetFilters();
  if (e.target.closest('[data-close-detail]')) {
    state.selected = null; $('article-detail').hidden = true; $('discovery').hidden = false; renderList(); requestDraw(); saveURL();
  }
});
$('reset-filters').addEventListener('click', () => { if (data) resetFilters(); });
$('toggle-filters').addEventListener('click', () => {
  const expanded = document.querySelector('.filters').classList.toggle('filters-expanded');
  $('toggle-filters').setAttribute('aria-expanded', String(expanded));
  $('toggle-filters').textContent = expanded ? '絞り込み ▴' : '絞り込み ▾';
});
$('search').addEventListener('input', () => { state.query = $('search').value; if (data) updateFilters(); });
for (const key of ['from', 'to']) $(`date-${key}`).addEventListener('change', () => { state[key] = $(`date-${key}`).value; if (data) updateFilters(); });
$('map-view').addEventListener('click', () => { if (data) setView('map'); });
$('list-view').addEventListener('click', () => { if (data) setView('list'); });
$('sort').addEventListener('change', () => { state.sort = $('sort').value; state.page = 0; renderList(); });
$('prev-page').addEventListener('click', () => { state.page--; renderList(); });
$('next-page').addEventListener('click', () => { state.page++; renderList(); });
$('zoom-in').addEventListener('click', () => zoomAt(1.35));
$('zoom-out').addEventListener('click', () => zoomAt(1 / 1.35));
$('fit-map').addEventListener('click', () => { zoom = 1; panX = panY = 0; hovered = null; $('map-tooltip').hidden = true; requestDraw(); });
$('about-button').addEventListener('click', () => $('about-dialog').showModal());
$('close-about').addEventListener('click', () => $('about-dialog').close());
new ResizeObserver(resize).observe($('map-panel'));
window.addEventListener('popstate', () => {
  if (!data) return;
  loadURL(); updateFilters(); setView(state.view);
  if (state.selected) openArticle(state.selected);
  else { $('article-detail').hidden = true; $('discovery').hidden = false; }
});

async function init() {
  try {
    const response = await fetch(new URL('./data/articles.json', import.meta.url));
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    data = await response.json();
    if (!Array.isArray(data.articles) || !data.articles.length) throw new Error('Article data is empty');
    categoryInfo = new Map(data.facets.categories.map(c => [c.name, c]));
    topicInfo = new Map(data.facets.topics.map(t => [t.name, t]));
    // Japanese labels make topics searchable in Japanese as well.
    articles = data.articles.map(a => ({ ...a, searchText: `${a.title} ${a.tags.join(' ')} ${a.categories.map(c => categoryInfo.get(c).label).join(' ')} ${a.topics.map(t => topicInfo.get(t).label).join(' ')}`.toLowerCase() }));
    byId = new Map(articles.map(a => [a.id, a]));
    const dates = articles.map(a => a.date).filter(Boolean).sort();
    $('data-info').textContent = `収録範囲：${dates[0]}〜${dates.at(-1)}（${fmt(articles.length)}記事）`;
    for (const id of ['date-from', 'date-to']) { $(id).min = dates[0]; $(id).max = dates.at(-1); }
    createFilters(); loadURL(); updateFilters(); setView(state.view);
    if (state.selected) openArticle(state.selected);
  } catch (error) {
    console.error('Could not load article data', error);
    data = null;
    $('map-status').hidden = false;
    $('map-status').innerHTML = '<p class="error-state">記事データを読み込めませんでした。<br>接続を確認して、再読み込みしてください。</p><button id="retry">再読み込み</button>';
    $('retry').addEventListener('click', init);
    $('match-count').textContent = '読み込みエラー';
  }
}
init();
