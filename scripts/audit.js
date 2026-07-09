#!/usr/bin/env node
/**
 * Live Core Web Vitals audit for trishikacarrentalhubli.in
 * Runs Lighthouse (via npx) mobile + desktop for every URL listed below,
 * writes a compact summary to /reports/02_cwv.json.
 *
 * Usage:  node scripts/audit.js
 * Requires: Node 18+, Chrome installed. Set CHROME_PATH if Chrome is not auto-found.
 * Note: chrome-launcher may throw an EPERM while deleting its temp profile on
 * Windows AFTER the report is written — the report file is still valid.
 */
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const URLS = [
  'https://trishikacarrentalhubli.in/',
  // add route/service pages here as Phase 3 ships them
];
const OUT = path.join(__dirname, '..', 'reports', '02_cwv.json');
const TMP = fs.mkdtempSync(path.join(os.tmpdir(), 'lh-'));

const AUDIT_KEYS = [
  'largest-contentful-paint', 'first-contentful-paint', 'total-blocking-time',
  'cumulative-layout-shift', 'speed-index', 'interactive', 'server-response-time',
];
const DETAIL_KEYS = [
  'render-blocking-resources', 'unminified-css', 'unminified-javascript',
  'modern-image-formats', 'uses-optimized-images', 'uses-responsive-images',
  'offscreen-images', 'total-byte-weight', 'uses-long-cache-ttl',
  'largest-contentful-paint-element', 'layout-shifts', 'font-display',
];

function run(url, preset) {
  const file = path.join(TMP, `lh-${preset}-${Buffer.from(url).toString('hex').slice(0, 12)}.json`);
  const presetFlag = preset === 'desktop' ? '--preset=desktop' : '';
  try {
    execSync(
      `npx -y lighthouse "${url}" ${presetFlag} --output=json --output-path="${file}" --quiet ` +
      `--chrome-flags="--headless=new" --only-categories=performance,seo,best-practices,accessibility`,
      { stdio: 'pipe', timeout: 300000 }
    );
  } catch (e) {
    if (!fs.existsSync(file)) throw e; // EPERM-on-cleanup still writes the report
  }
  const lh = JSON.parse(fs.readFileSync(file, 'utf8'));
  const metrics = {};
  for (const k of AUDIT_KEYS) metrics[k] = {
    value: lh.audits[k] && lh.audits[k].numericValue, display: lh.audits[k] && lh.audits[k].displayValue,
  };
  const opportunities = {};
  for (const k of DETAIL_KEYS) {
    const a = lh.audits[k];
    if (!a) continue;
    opportunities[k] = {
      score: a.score, display: a.displayValue || null,
      savingsMs: a.details && a.details.overallSavingsMs, savingsBytes: a.details && a.details.overallSavingsBytes,
      items: a.details && a.details.items ? a.details.items.slice(0, 10) : undefined,
    };
  }
  return {
    fetchedAt: lh.fetchTime, lighthouseVersion: lh.lighthouseVersion,
    scores: Object.fromEntries(Object.entries(lh.categories).map(([k, v]) => [k, v.score])),
    metrics, opportunities,
  };
}

const result = { generated: new Date().toISOString(), pages: {} };
for (const url of URLS) {
  console.log(`Auditing ${url} ...`);
  result.pages[url] = { mobile: run(url, 'mobile'), desktop: run(url, 'desktop') };
}
fs.writeFileSync(OUT, JSON.stringify(result, null, 1));
console.log(`Wrote ${OUT}`);
