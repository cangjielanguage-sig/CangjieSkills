from __future__ import annotations


ADMIN_HTML = r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>HarmonyOS Knowledge 管理面板</title>
  <style>
    :root {
      color-scheme: light;
      --bg: #f5f7fa;
      --panel: #ffffff;
      --text: #17202a;
      --muted: #637083;
      --line: #dbe2ea;
      --soft: #eef3f8;
      --accent: #1167d8;
      --accent-2: #0f766e;
      --danger: #b42318;
      --warn: #ad6800;
      --ok: #14804a;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: var(--text); }
    header {
      background: linear-gradient(180deg, #ffffff 0%, #f9fbfd 100%);
      border-bottom: 1px solid var(--line);
      padding: 18px 28px;
      position: sticky;
      top: 0;
      z-index: 2;
    }
    .header-inner { max-width: 1240px; margin: 0 auto; display: flex; justify-content: space-between; gap: 18px; align-items: center; }
    h1 { font-size: 20px; margin: 0 0 4px; }
    h2 { font-size: 16px; margin: 0 0 14px; }
    main { max-width: 1240px; margin: 0 auto; padding: 20px; display: grid; gap: 16px; }
    main > *, section, .split, .grid, .stats { min-width: 0; }
    section { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 16px; }
    .toolbar { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; align-items: end; }
    .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; }
    .stat { background: var(--soft); border: 1px solid #e4ebf2; border-radius: 8px; padding: 12px; }
    .stat b { display: block; font-size: 22px; line-height: 1.2; }
    .stat span, .muted { color: var(--muted); font-size: 13px; }
    label { display: grid; gap: 6px; color: #435266; font-size: 13px; }
    input, select, button {
      font: inherit;
      border-radius: 6px;
      border: 1px solid #c7d0da;
      padding: 9px 10px;
      background: #fff;
      color: var(--text);
      min-height: 38px;
    }
    input[type="checkbox"] { min-height: auto; }
    button { cursor: pointer; background: var(--accent); border-color: var(--accent); color: #fff; font-weight: 650; }
    button.secondary { background: #fff; color: var(--accent); }
    button.ghost { background: #fff; color: var(--text); border-color: var(--line); }
    button.danger { background: var(--danger); border-color: var(--danger); }
    button:disabled { cursor: not-allowed; opacity: .55; }
    table { width: 100%; border-collapse: collapse; font-size: 13px; }
    th, td { text-align: left; padding: 9px; border-bottom: 1px solid #edf1f5; vertical-align: top; }
    th { color: var(--muted); font-weight: 650; white-space: nowrap; }
    tr:hover td { background: #fafcff; }
    pre { margin: 0; white-space: pre-wrap; word-break: break-word; background: #f3f6f9; border: 1px solid #e5ebf1; border-radius: 6px; padding: 10px; max-height: 360px; overflow: auto; }
    .row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }
    .pill { display: inline-flex; align-items: center; border-radius: 999px; padding: 3px 8px; font-size: 12px; font-weight: 650; background: var(--soft); color: #405064; }
    .pill.ok { background: #e8f6ef; color: var(--ok); }
    .pill.warn { background: #fff4df; color: var(--warn); }
    .pill.bad { background: #fdecea; color: var(--danger); }
    .pill.info { background: #eaf2ff; color: var(--accent); }
    .split { display: grid; grid-template-columns: minmax(0, 1fr) minmax(320px, .45fr); gap: 16px; }
    .checks { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 12px; }
    .checks label { display: inline-flex; flex-direction: row; align-items: center; gap: 6px; }
    .result-list { display: grid; gap: 10px; }
    .result { border: 1px solid var(--line); border-radius: 8px; padding: 12px; }
    .result h3 { margin: 0 0 6px; font-size: 15px; }
    .result .ref { color: var(--muted); font-size: 12px; word-break: break-all; }
    .result p { margin: 8px 0 0; color: #354254; font-size: 13px; max-height: 120px; overflow: auto; }
    .empty { padding: 16px; background: var(--soft); border: 1px dashed #cbd6e2; border-radius: 8px; color: var(--muted); }
    .job-log { max-width: 440px; }
    @media (max-width: 860px) {
      .header-inner, .split { display: block; }
      .header-inner .toolbar { margin-top: 12px; }
      main { padding: 12px; width: 100%; max-width: 100%; }
      .grid, .stats { grid-template-columns: 1fr; }
      input, select { width: 100%; }
      table { display: block; overflow-x: auto; }
    }
  </style>
</head>
<body>
<header>
  <div class="header-inner">
    <div>
      <h1>HarmonyOS Knowledge 管理面板</h1>
      <div class="muted">多版本文档索引、完整向量构建与检索测试</div>
    </div>
    <div class="toolbar">
      <button id="refresh" class="secondary">刷新</button>
      <button id="run-query" class="ghost">测试查询</button>
    </div>
  </div>
</header>

<main>
  <section>
    <h2>状态概览</h2>
    <div id="stats" class="stats"></div>
  </section>

  <div class="split">
    <section>
      <h2>构建 / 同步版本</h2>
      <div class="grid">
        <label>文档目录 <input id="docs_root" placeholder="bundled docs"></label>
        <label>版本 <input id="version" placeholder="6.1.1.345"></label>
        <label>向量模式
          <select id="embedding_mode">
            <option value="off">off</option>
            <option value="index" selected>index</option>
            <option value="all">all</option>
          </select>
        </label>
        <label>Embedding Key 环境变量 <input id="embedding_api_key_env" value="DASHSCOPE_API_KEY"></label>
        <label>Embedding batch <input id="embedding_batch_size" type="number" min="1" placeholder="10"></label>
      </div>
      <div class="checks">
        <label><input id="incremental" type="checkbox" checked> 增量同步</label>
        <label><input id="keep_missing" type="checkbox"> 保留磁盘已删除文档</label>
      </div>
      <div class="toolbar" style="margin-top: 14px">
        <button id="start-build">开始构建</button>
        <span class="muted">后台执行。面板会保留最近 300 条构建日志。</span>
      </div>
    </section>

    <section>
      <h2>查询测试</h2>
      <div class="grid">
        <label>问题 <input id="q" value="HUKS generateKeyItem"></label>
        <label>版本 <input id="q_version" placeholder="留空使用默认，all 跨版本"></label>
        <label>top_k <input id="top_k" type="number" value="5"></label>
        <label>向量检索
          <select id="q_embedding">
            <option value="">默认</option>
            <option value="off">off</option>
            <option value="search">search</option>
            <option value="all">all</option>
          </select>
        </label>
      </div>
      <div id="query_out" class="result-list" style="margin-top:12px"></div>
    </section>
  </div>

  <section>
    <h2>版本</h2>
    <div class="row" style="margin-bottom: 10px">
      <label><input id="physical_remove" type="checkbox"> Physical delete</label>
      <button id="compact-index" class="ghost">Compact storage</button>
      <span class="muted">Default removal is logical and fast; physical delete rebuilds storage and should be treated as offline maintenance.</span>
    </div>
    <div id="versions"></div>
  </section>

  <section>
    <h2>构建任务</h2>
    <div id="jobs"></div>
  </section>

  <section>
    <h2>原始健康状态</h2>
    <pre id="health"></pre>
  </section>
</main>

<script>
const $ = id => document.getElementById(id);

async function getJson(url, options) {
  const res = await fetch(url, options);
  const data = await res.json();
  if (!res.ok) throw new Error(data.message || data.error || res.statusText);
  return data;
}

function value(id) { return $(id).value.trim(); }
function checked(id) { return $(id).checked; }
function esc(s) { return String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function escAttr(s) { return esc(s).replace(/`/g, '&#96;'); }
function statusPill(status) {
  const s = String(status || 'unknown');
  const cls = s === 'complete' || s === 'ready' ? 'ok' : s === 'failed' ? 'bad' : s === 'queued' ? 'warn' : 'info';
  return `<span class="pill ${cls}">${esc(s)}</span>`;
}

async function refresh() {
  const [health, versions, jobs] = await Promise.all([
    getJson('/health'),
    getJson('/api/versions'),
    getJson('/api/jobs')
  ]);
  $('health').textContent = JSON.stringify(health, null, 2);
  $('stats').innerHTML = renderStats(health, versions, jobs);
  $('versions').innerHTML = renderVersions(versions);
  $('jobs').innerHTML = renderJobs(jobs);
}

function renderStats(health, versions, jobs) {
  const running = jobs.filter(j => ['running', 'queued'].includes(j.status)).length;
  return [
    ['版本数', versions.length],
    ['文档数', health.documents ?? versions.reduce((n, v) => n + (v.documents || 0), 0)],
    ['Sections', health.sections ?? versions.reduce((n, v) => n + (v.sections || 0), 0)],
    ['Vectors', health.vectors ?? 0],
    ['运行任务', running],
    ['检索模式', health.mode || '-']
  ].map(([label, value]) => `<div class="stat"><b>${esc(value)}</b><span>${esc(label)}</span></div>`).join('');
}

function renderVersions(items) {
  if (!items.length) return '<div class="empty">暂无版本。可以在上方发起一次构建。</div>';
  return `<table><thead><tr><th>版本</th><th>文档</th><th>Sections</th><th>Symbols</th><th>Examples</th><th>Vectors</th><th>更新时间</th><th>操作</th></tr></thead><tbody>` +
    items.map(v => `<tr>
      <td>${esc(v.version)}</td>
      <td>${v.documents}</td>
      <td>${v.sections}</td>
      <td>${v.symbols}</td>
      <td>${v.examples}</td>
      <td>${v.vectors}</td>
      <td>${esc(v.updated_at || '')}</td>
      <td><button class="danger remove-version" data-version="${escAttr(v.version)}">删除</button></td>
    </tr>`).join('') +
    '</tbody></table>';
}

function renderJobs(items) {
  if (!items.length) return '<div class="empty">暂无构建任务。</div>';
  return `<table><thead><tr><th>ID</th><th>状态</th><th>版本</th><th>最近事件</th><th>结果 / 日志</th></tr></thead><tbody>` +
    items.map(j => `<tr>
      <td>${esc(j.id)}</td>
      <td>${statusPill(j.status)}</td>
      <td>${esc((j.request || {}).version || '')}</td>
      <td>${esc((j.last_event || {}).stage || '')}<br><span class="muted">${esc((j.last_event || {}).message || j.message || '')}</span></td>
      <td class="job-log"><details><summary>查看</summary><pre>${esc(JSON.stringify(j.result || j.error || '', null, 2))}</pre><pre>${esc((j.logs || []).map(e => `[${e.elapsed_text}] ${e.stage} ${e.message}`).join('\n'))}</pre></details></td>
    </tr>`).join('') +
    '</tbody></table>';
}

async function startBuild() {
  const payload = {
    docs_root: value('docs_root') || undefined,
    version: value('version') || 'default',
    embedding_mode: value('embedding_mode') || 'index',
    embedding_api_key_env: value('embedding_api_key_env') || undefined,
    embedding_batch_size: value('embedding_batch_size') || undefined,
    incremental: checked('incremental'),
    keep_missing: checked('keep_missing')
  };
  $('start-build').disabled = true;
  try {
    await getJson('/api/build', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload) });
    await refresh();
  } finally {
    $('start-build').disabled = false;
  }
}

async function removeVersion(version) {
  const physical = checked('physical_remove');
  const action = physical ? 'Physically delete' : 'Logically remove';
  if (!version || !confirm(`${action} version ${version}?`)) return;
  await getJson('/api/versions/remove', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({version, physical}) });
  await refresh();
}

async function compactIndex() {
  if (!confirm('Compact storage by keeping ready versions only?')) return;
  $('compact-index').disabled = true;
  try {
    await getJson('/api/compact', { method: 'POST', headers: {'Content-Type':'application/json'}, body: '{}' });
    await refresh();
  } finally {
    $('compact-index').disabled = false;
  }
}

async function testSearch() {
  const params = new URLSearchParams({ q: value('q'), top_k: value('top_k') || '5' });
  if (value('q_version')) params.set('version', value('q_version'));
  if (value('q_embedding')) params.set('embedding', value('q_embedding'));
  const results = await getJson('/search?' + params.toString());
  $('query_out').innerHTML = renderResults(results);
}

function renderResults(results) {
  if (!Array.isArray(results) || !results.length) return '<div class="empty">没有匹配结果。</div>';
  return results.map(item => `<div class="result">
    <h3>${esc(item.title)} <span class="pill info">${esc(item.version || '')}</span></h3>
    <div class="ref">${esc(item.ref)}</div>
    <div class="muted">score ${esc(item.score)} · ${esc((item.reasons || []).join(', '))}</div>
    <p>${esc(item.snippet || '')}</p>
  </div>`).join('');
}

document.addEventListener('click', event => {
  const removeButton = event.target.closest('.remove-version');
  if (removeButton) removeVersion(removeButton.dataset.version || '');
});
$('refresh').addEventListener('click', refresh);
$('run-query').addEventListener('click', testSearch);
$('start-build').addEventListener('click', startBuild);
$('compact-index').addEventListener('click', compactIndex);

refresh().catch(err => { $('health').textContent = String(err); });
setInterval(() => refresh().catch(() => {}), 5000);
</script>
</body>
</html>"""
