import json, sys
lh = json.load(open(sys.argv[1], encoding='utf-8'))
A = lh['audits']
for key in ['lcp-breakdown-insight','lcp-discovery-insight','render-blocking-insight',
            'image-delivery-insight','font-display-insight','unsized-images','dom-size-insight',
            'cls-culprits-insight','document-latency-insight']:
    a = A.get(key)
    if not a: continue
    print(f"== {key}: score={a.get('score')} display={a.get('displayValue') or ''}")
    d = a.get('details') or {}
    def walk(items, depth=0):
        for i in items[:10]:
            if not isinstance(i, dict): continue
            node = i.get('node') or {}
            bits = []
            if node: bits.append('node=' + str(node.get('selector'))[:80])
            for k in ('label','url','subpart','duration','timing','wastedBytes','totalBytes','value','phase'):
                if k in i:
                    v = i[k]
                    if isinstance(v, dict): v = v.get('value', v)
                    bits.append(f'{k}={str(v)[:90]}')
            print('  ' * (depth + 1) + ' | '.join(map(str, bits)))
            if isinstance(i.get('items'), list): walk(i['items'], depth + 1)
    if isinstance(d.get('items'), list): walk(d['items'])
    print()
