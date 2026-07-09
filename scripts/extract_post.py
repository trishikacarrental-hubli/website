import json, sys
lh = json.load(open(sys.argv[1], encoding='utf-8'))
print('scores:', {k: round(v['score'] * 100) for k, v in lh['categories'].items()})
for k in ['largest-contentful-paint', 'first-contentful-paint', 'speed-index',
          'total-blocking-time', 'cumulative-layout-shift', 'interactive', 'total-byte-weight']:
    print(f"  {k:34s} {lh['audits'][k]['displayValue']}")
