import json, sys
lh = json.load(open(sys.argv[1], encoding='utf-8'))
A = lh['audits']

def dump(key, n=6):
    a = A.get(key)
    if not a: print(f'-- {key}: MISSING'); return
    print(f"-- {key}: score={a.get('score')} display={a.get('displayValue')}")
    d = a.get('details') or {}
    items = d.get('items') or []
    for i in items[:n]:
        if 'node' in i and isinstance(i.get('node'), dict):
            print('   node:', i['node'].get('selector'), '|', (i['node'].get('snippet') or '')[:110])
            for k in ('phases','timing','percent'):
                if k in i: print('    ', k, i[k])
            if 'items' in i:
                for sub in i['items'][:6]: print('    sub:', json.dumps(sub)[:160])
        else:
            print('   ', json.dumps({k: v for k, v in i.items() if k in ('url','wastedBytes','wastedMs','totalBytes','transferSize','resourceType','label','duration','scriptParseCompile','scripting')})[:170])

for k in ['largest-contentful-paint-element','lcp-lazy-loaded','prioritize-lcp-image',
          'render-blocking-resources','font-display','modern-image-formats','uses-optimized-images',
          'uses-responsive-images','offscreen-images','bootup-time','mainthread-work-breakdown',
          'third-party-summary','uses-text-compression','total-byte-weight','resource-summary']:
    dump(k)
