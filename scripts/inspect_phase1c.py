import csv, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open(os.path.join(ROOT,'data','keyword_master.csv'), encoding='utf-8')))
rental = re.compile(r'\b(rent|rental|hire)\b')
taxi = re.compile(r'\b(taxi|cab)\b')
buckets = {'rental-language':[0,0,0.0,0.0], 'taxi/cab-language':[0,0,0.0,0.0], 'both':[0,0,0.0,0.0], 'neither':[0,0,0.0,0.0]}
for r in rows:
    if r['intent'] != 'transactional': continue
    t = r['normalized']
    has_r, has_t = bool(rental.search(t)), bool(taxi.search(t))
    k = 'both' if (has_r and has_t) else 'rental-language' if has_r else 'taxi/cab-language' if has_t else 'neither'
    b = buckets[k]
    b[0]+=1; b[1]+=int(r['clicks']); b[2]+=float(r['cost']); b[3]+=float(r['conversions'])
print('Transactional terms only — language split:')
for k,v in buckets.items():
    cpa = v[2]/v[3] if v[3] else 0
    print(f'{k:20s} terms:{v[0]:4d} clicks:{v[1]:5d} cost:{v[2]:9.2f} conv:{v[3]:6.2f} cpa:{cpa:7.2f}')
tot_route = [0,0,0.0,0.0]
for r in rows:
    if r['cluster'].startswith('route-') and not r['cluster'].startswith('route-into'):
        tot_route[0]+=1; tot_route[1]+=int(r['clicks']); tot_route[2]+=float(r['cost']); tot_route[3]+=float(r['conversions'])
print(f"\nAll outward routes combined: terms:{tot_route[0]} clicks:{tot_route[1]} cost:{tot_route[2]:.2f} conv:{tot_route[3]:.2f}")
allv = [sum(int(r['clicks']) for r in rows), sum(float(r['cost']) for r in rows)]
print(f"Route share of visible: {tot_route[1]/allv[0]*100:.1f}% of clicks, {tot_route[2]/allv[1]*100:.1f}% of cost")
