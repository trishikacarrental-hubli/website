import json, sys
lh = json.load(open(sys.argv[1], encoding='utf-8'))
a = lh['audits']
ins = a.get('lcp-breakdown-insight', {})
d = ins.get('details') or {}
print(json.dumps(d, indent=1)[:3000])
# also probe metrics + any node info elsewhere
m = a.get('metrics', {})
if m.get('details') and m['details'].get('items'):
    it = m['details']['items'][0]
    print({k: v for k, v in it.items() if 'argest' in k or 'irst' in k})
