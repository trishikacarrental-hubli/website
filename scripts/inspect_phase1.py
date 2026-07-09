import json, csv, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open(os.path.join(ROOT,'data','keyword_master.csv'), encoding='utf-8')))
s = json.load(open(os.path.join(ROOT,'data','phase1_summary.json'), encoding='utf-8'))

def show(title, subset, n=15):
    print(f'== {title} ==')
    for r in subset[:n]:
        print(f"{r['normalized'][:52]:54s} clicks:{r['clicks']:>4} cost:{r['cost']:>9} conv:{r['conversions']}")
    print()

show('travels-generic (cost desc)', sorted([r for r in rows if r['cluster']=='travels-generic'], key=lambda r:-float(r['cost'])))
show('misc-local (cost desc)', sorted([r for r in rows if r['cluster']=='misc-local'], key=lambda r:-float(r['cost'])), 12)
show('core-generic (cost desc)', sorted([r for r in rows if r['cluster']=='core-generic'], key=lambda r:-float(r['cost'])), 10)

print('== money by conversions (top 15) ==')
for m in s['money_by_conv'][:15]:
    print(f"{m['normalized'][:47]:49s} conv:{m['conversions']:>5} cost:{m['cost']:>8} cpa:{m['cpa']:>7} {m['cluster']}")
print()
print('== money by CVR min 5 clicks (top 12) ==')
for m in s['money_by_cvr_min5clicks'][:12]:
    print(f"{m['normalized'][:47]:49s} cvr:{m['cvr']:>6} clicks:{m['clicks']:>3} conv:{m['conversions']} {m['cluster']}")
print()
print('== bleeders top 20 ==')
for b in s['bleeders_top'][:20]:
    print(f"{b['normalized'][:47]:49s} clicks:{b['clicks']:>3} cost:{b['cost']:>8} {b['cluster']}")
