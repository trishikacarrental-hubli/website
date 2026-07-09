# One-off: build reports/02_cwv.json from the two Lighthouse JSONs already captured,
# and print the headline findings used in 02_technical_seo.md.
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRATCH = sys.argv[1]
OUT = os.path.join(ROOT, 'reports', '02_cwv.json')

AUDIT_KEYS = ['largest-contentful-paint','first-contentful-paint','total-blocking-time',
    'cumulative-layout-shift','speed-index','interactive','server-response-time']
DETAIL_KEYS = ['render-blocking-resources','modern-image-formats','uses-optimized-images',
    'uses-responsive-images','offscreen-images','total-byte-weight','uses-long-cache-ttl',
    'largest-contentful-paint-element','font-display','unminified-css','unminified-javascript']

def extract(fn):
    lh = json.load(open(fn, encoding='utf-8'))
    metrics = {k: {'value': lh['audits'][k].get('numericValue'), 'display': lh['audits'][k].get('displayValue')}
               for k in AUDIT_KEYS if k in lh['audits']}
    opp = {}
    for k in DETAIL_KEYS:
        a = lh['audits'].get(k)
        if not a: continue
        d = a.get('details') or {}
        opp[k] = {'score': a.get('score'), 'display': a.get('displayValue'),
                  'savingsMs': d.get('overallSavingsMs'), 'savingsBytes': d.get('overallSavingsBytes'),
                  'items': (d.get('items') or [])[:8]}
    return {'fetchedAt': lh['fetchTime'], 'lighthouseVersion': lh['lighthouseVersion'],
            'scores': {k: v['score'] for k, v in lh['categories'].items()}, 'metrics': metrics, 'opportunities': opp}

res = {'generated': None, 'pages': {'https://trishikacarrentalhubli.in/': {
    'mobile': extract(os.path.join(SCRATCH, 'lh_mobile.json')),
    'desktop': extract(os.path.join(SCRATCH, 'lh_desktop.json'))}}}
res['generated'] = res['pages']['https://trishikacarrentalhubli.in/']['mobile']['fetchedAt']
json.dump(res, open(OUT, 'w', encoding='utf-8'), indent=1)
print('wrote', OUT)
for form in ('mobile', 'desktop'):
    d = res['pages']['https://trishikacarrentalhubli.in/'][form]
    print(f"\n=== {form.upper()} scores: " + ' '.join(f'{k}:{v}' for k, v in d['scores'].items()))
    for k, v in d['metrics'].items(): print(f"  {k:36s} {v['display']}")
    print('  -- opportunities --')
    for k, v in d['opportunities'].items():
        if v['score'] is not None and v['score'] < 1:
            print(f"  {k:36s} score:{v['score']} {v['display'] or ''} savings:{v['savingsMs'] or v['savingsBytes'] or ''}")
mob = res['pages']['https://trishikacarrentalhubli.in/']['mobile']['opportunities']
lcp_el = mob.get('largest-contentful-paint-element', {}).get('items')
print('\nLCP element (mobile):', json.dumps(lcp_el, indent=1)[:1500] if lcp_el else 'n/a')
rb = mob.get('render-blocking-resources', {}).get('items')
print('\nRender-blocking (mobile):', json.dumps(rb, indent=1)[:1200] if rb else 'n/a')
imgs = mob.get('modern-image-formats', {}).get('items')
print('\nImage-format savings (mobile):', json.dumps([{ 'url': i.get('url'), 'wastedBytes': i.get('wastedBytes')} for i in (imgs or [])], indent=1)[:1200])
