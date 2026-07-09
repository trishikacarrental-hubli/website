# Pull candidate keywords per campaign/ad-group from keyword_master for Phase 6 build.
import csv, os
from collections import defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open(os.path.join(ROOT,'data','keyword_master.csv'), encoding='utf-8')))
def f(r,k): return float(r[k])

# candidates = terms we'd bid on: scale-paid or both, transactional/navigational-own
cand = [r for r in rows if r['action'] in ('scale-paid','both')]

def show(title, pred, sort_impr=True):
    sub = [r for r in cand if pred(r)]
    sub.sort(key=lambda r:(-int(r['impressions']), -int(r['clicks'])))
    print(f"\n== {title} ({len(sub)}) ==")
    for r in sub[:25]:
        print(f"  {r['normalized'][:45]:47s} impr:{r['impressions']:>4} clk:{r['clicks']:>3} cost:{r['cost']:>7} conv:{r['conversions']}")

show("CORE-LOCAL", lambda r: r['cluster']=='core-local')
show("AIRPORT", lambda r: r['cluster']=='airport')
show("ROUTES (all)", lambda r: r['cluster'].startswith('route-') and not r['cluster'].startswith('route-into'))
show("VEHICLE-TEMPO", lambda r: r['cluster']=='vehicle-tempo-traveller' or r['cluster']=='vehicle-force-urbania' or r['cluster']=='vehicle-force-cruiser')
show("TRAVELS-LOCAL", lambda r: r['cluster']=='travels-local')
show("COMPETITOR (converting)", lambda r: r['cluster']=='competitor')
