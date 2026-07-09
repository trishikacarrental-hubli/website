import csv, os
from collections import defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open(os.path.join(ROOT,'data','keyword_master.csv'), encoding='utf-8')))
f = lambda r,k: float(r[k])

def agg(subset, key):
    g = defaultdict(lambda: [0,0,0,0.0,0.0])
    for r in subset:
        d = g[key(r)]
        d[0]+=1; d[1]+=int(r['impressions']); d[2]+=int(r['clicks']); d[3]+=f(r,'cost'); d[4]+=f(r,'conversions')
    return g

print('== ROUTE DEMAND (incl zero-click, by impressions) ==')
routes = [r for r in rows if r['cluster'].startswith('route-') and not r['cluster'].startswith('route-into')]
for k,v in sorted(agg(routes, lambda r:r['cluster']).items(), key=lambda kv:(-kv[1][4],-kv[1][3],-kv[1][1])):
    print(f'{k:26s} terms:{v[0]:3d} impr:{v[1]:4d} clicks:{v[2]:3d} cost:{v[3]:8.2f} conv:{v[4]:.2f}')
print()
print('== VEHICLE DEMAND ==')
vehs = [r for r in rows if r['cluster'].startswith('vehicle-')]
for k,v in sorted(agg(vehs, lambda r:r['cluster']).items(), key=lambda kv:(-kv[1][4],-kv[1][3])):
    print(f'{k:32s} terms:{v[0]:3d} impr:{v[1]:4d} clicks:{v[2]:3d} cost:{v[3]:8.2f} conv:{v[4]:.2f}')
print()
print('== SELF-DRIVE top terms (for negatives) ==')
sd = sorted([r for r in rows if r['cluster']=='self-drive'], key=lambda r:-f(r,'cost'))
for r in sd[:12]: print(f"  {r['normalized'][:55]:57s} {r['clicks']:>3} clicks  rs{r['cost']}")
print()
print('== COMPETITOR terms by cost (top 15) ==')
comp = sorted([r for r in rows if r['cluster']=='competitor'], key=lambda r:-f(r,'cost'))
for r in comp[:15]: print(f"  {r['normalized'][:55]:57s} {r['clicks']:>3} clicks  rs{r['cost']}  conv:{r['conversions']}")
print()
print('== AIRPORT terms ==')
for r in sorted([r for r in rows if r['cluster']=='airport'], key=lambda r:-f(r,'cost')):
    print(f"  {r['normalized'][:55]:57s} impr:{r['impressions']:>4} {r['clicks']:>3} clicks  rs{r['cost']}  conv:{r['conversions']}")
print()
print('== TEMPO TRAVELLER terms ==')
for r in sorted([r for r in rows if r['cluster']=='vehicle-tempo-traveller'], key=lambda r:-f(r,'cost'))[:10]:
    print(f"  {r['normalized'][:55]:57s} impr:{r['impressions']:>4} {r['clicks']:>3} clicks  rs{r['cost']}")
print()
print('== PRICE-modified core-local terms ==')
for r in sorted([r for r in rows if r['modifier_type']=='price'], key=lambda r:-int(r['impressions']))[:12]:
    print(f"  {r['normalized'][:55]:57s} impr:{r['impressions']:>4} {r['clicks']:>3} clicks  rs{r['cost']} [{r['cluster']}]")
print()
print('== GOA route terms detail ==')
for r in sorted([r for r in rows if r['cluster']=='route-goa'], key=lambda r:-int(r['impressions'])):
    print(f"  {r['normalized'][:55]:57s} impr:{r['impressions']:>4} {r['clicks']:>3} clicks  rs{r['cost']}")
