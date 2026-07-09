#!/usr/bin/env node
/**
 * Trishika Car Rental — one-page performance summary from a fresh Google Ads
 * "Search terms" export. Keeps the account maintainable after handoff.
 *
 * Usage:  node scripts/report.js "C:\\path\\to\\search_terms_export.csv"
 * Output: prints a one-page markdown summary to stdout AND writes
 *         reports/latest_report.md . Run it weekly with the fresh export.
 *
 * Handles the raw Google Ads export as-is: UTF-16LE, tab-delimited,
 * 2 title lines, header on line 3, "Total:" summary rows at the bottom.
 * No dependencies — plain Node.
 */
const fs = require('fs');
const path = require('path');

const src = process.argv[2];
if (!src) { console.error('Usage: node scripts/report.js <search_terms_export.csv>'); process.exit(1); }

// --- read (auto-detect UTF-16LE BOM vs UTF-8) ---
let buf = fs.readFileSync(src);
let text;
if (buf[0] === 0xFF && buf[1] === 0xFE) text = buf.toString('utf16le');
else text = buf.toString('utf8');
const lines = text.split(/\r?\n/).filter(l => l.length);

// find header row (contains "Search term" and "Cost")
let hi = lines.findIndex(l => /Search term/i.test(l) && /Cost/i.test(l));
if (hi < 0) { console.error('Could not find header row.'); process.exit(1); }
const delim = lines[hi].includes('\t') ? '\t' : ',';
const header = lines[hi].split(delim).map(s => s.trim());
const col = name => header.findIndex(h => h.toLowerCase() === name.toLowerCase());
const ci = {
  term: col('Search term'), clicks: col('Clicks'), impr: col('Impr.'),
  cost: col('Cost'), conv: col('Conversions'), cpc: col('Avg. CPC'),
};
const num = s => parseFloat(String(s || '').replace(/[,%]/g, '')) || 0;

const rows = [], totals = {};
for (const line of lines.slice(hi + 1)) {
  const c = line.split(delim);
  const term = (c[ci.term] || '').trim();
  if (!term) continue;
  const rec = { term, clicks: num(c[ci.clicks]), impr: num(c[ci.impr]),
    cost: num(c[ci.cost]), conv: num(c[ci.conv]) };
  if (/^Total:/i.test(term)) { totals[term] = rec; continue; }
  rows.push(rec);
}

// --- junk detectors (mirror Phase 1) ---
const JUNK = [/self ?driv/, /without driver/, /\brapido\b/, /\bola\b/, /\buber\b/, /zoom ?car/,
  /namma yatri/, /blusmart/, /\bjob\b/, /salary/, /vacancy/, /olx/, /second hand/, /driving school/,
  /car (wash|service|repair|servicing)/, /rishikesh|hassan|guwahati/];
const isJunk = t => JUNK.some(r => r.test(t.toLowerCase()));

// --- aggregates ---
const sum = (arr, k) => arr.reduce((a, r) => a + r[k], 0);
const spend = sum(rows, 'cost'), clicks = sum(rows, 'clicks'), conv = sum(rows, 'conv');
const cpl = conv ? spend / conv : 0;
const converting = rows.filter(r => r.conv > 0).sort((a, b) => b.conv - a.conv);
const bleeders = rows.filter(r => r.cost > 0 && r.conv === 0).sort((a, b) => b.cost - a.cost);
const junk = rows.filter(r => isJunk(r.term) && r.cost > 0).sort((a, b) => b.cost - a.cost);
const junkSpend = sum(junk, 'cost');

const fmt = n => '₹' + n.toLocaleString('en-IN', { maximumFractionDigits: 0 });
const cv = n => Math.round(n * 100) / 100;
const row = r => `${r.term.slice(0, 42).padEnd(44)} clk:${String(r.clicks).padStart(4)} cost:${fmt(r.cost).padStart(9)} conv:${cv(r.conv)}`;

let out = `# Trishika Ads — Weekly Report\n\n`;
out += `Source: \`${path.basename(src)}\` · rows: ${rows.length}\n\n`;
out += `## The numbers\n`;
out += `- **Spend:** ${fmt(spend)}  ·  **Clicks:** ${clicks}  ·  **Conversions:** ${cv(conv)}\n`;
out += `- **Cost per lead (CPL):** ${conv ? fmt(cpl) : 'n/a (0 conversions — check tracking!)'}\n`;
out += `- **Visible junk spend this period:** ${fmt(junkSpend)} across ${junk.length} terms\n\n`;

out += `## Top converting terms (scale these)\n`;
out += converting.slice(0, 10).map(row).join('\n') || '  (none — is conversion tracking live?)';
out += `\n\n## Biggest bleeders (spend, 0 conversions — review / negative)\n`;
out += bleeders.slice(0, 12).map(row).join('\n') || '  (none)';
out += `\n\n## New junk to add as negatives (self-drive / apps / jobs / wrong-city)\n`;
out += (junk.slice(0, 15).map(r => `  ${r.term.slice(0, 46).padEnd(48)} ${fmt(r.cost)}`).join('\n') || '  (clean — negatives holding)');
out += `\n\n## Do this week (20 min)\n`;
out += `1. Add the junk terms above as negatives.\n`;
out += `2. Move budget from bleeders toward the top converters.\n`;
out += `3. If CPL is blank/0, STOP and fix conversion tracking before touching bids.\n`;

const outPath = path.join(__dirname, '..', 'reports', 'latest_report.md');
fs.writeFileSync(outPath, out);
console.log(out);
console.log(`\n(written to ${outPath})`);
