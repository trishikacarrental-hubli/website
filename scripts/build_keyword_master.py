# Phase 1 — build /data/keyword_master.csv from /data/search_terms_12mo.csv
# Deterministic rule-based classification. Review flags printed at end.
import csv, re, json, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "search_terms_12mo.csv")
OUT = os.path.join(ROOT, "data", "keyword_master.csv")
SUMMARY = os.path.join(ROOT, "data", "phase1_summary.json")

def num(s):
    s = (s or "").replace(",", "").replace("%", "").strip()
    return float(s) if s not in ("", "-", "--") else 0.0

# ---------- normalization ----------
def normalize(term):
    t = term.lower().strip()
    t = re.sub(r"[^\w\s]", " ", t)
    t = re.sub(r"\bhubball?i\b", "hubli", t)      # hubballi/hubbali -> hubli
    t = re.sub(r"\bbengaluru\b|\bbanglore\b|\bbangalor\b", "bangalore", t)
    t = re.sub(r"\bbelagavi\b", "belgaum", t)
    t = re.sub(r"\brentals\b", "rental", t)
    t = re.sub(r"\bcabs\b", "cab", t)
    t = re.sub(r"\bcars\b", "car", t)
    t = re.sub(r"\btaxis\b", "taxi", t)
    t = re.sub(r"\bservices\b", "service", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

# ---------- vocab ----------
COMPETITORS = ["ola","uber","rapido","rido","zoom car","zoomcar","revv","savaari","makemytrip",
    "bharat taxi","bharath taxi","blusmart","namma yatri","sai cab","shiva cab","balaji",
    "nikhil travel","queens","suman cab","tirupati cab","bila bila","bala bala","ats cab",
    "taxisafar","madhu car","swadeshi","raahiz","akash cab","wali","khushi","shreeshail",
    "shanteshwara","seven tour","laxmi","meru","redtaxi","red taxi","goibibo","abhibus","drivezy",
    "myles","carzonrent","gozo","yatra","cleartrip","redbus","tt travel","bhagya travel",
    "ganesh travel","vrl","sujata"]
WRONG_GEO = ["rishikesh","hassan","mysore","mangalore","udupi","pune","mumbai","hyderabad",
    "bangalore","goa","kolhapur","solapur","belgaum"]  # only applied when query is NOT a route and lacks hubli/dharwad
OWN_BRAND = ["trishika"]
JOB_WORDS = ["job","salary","vacancy","wanted","hiring","recruitment","computer operator",
    "attachment","attach","olx","second hand","used car","car sale","sale car","buy car",
    "showroom","driving school","licence","license","loan","emi","insurance"]
SELF_DRIVE = ["self drive","self driving","without driver","self car","selfdrive","self rental"]
VEHICLES = {
    "cruiser":"Force Cruiser",
    "innova crysta":"Innova Crysta","crysta":"Innova Crysta","innova":"Innova",
    "ertiga":"Ertiga","dzire":"Sedan (Dzire/Etios)","etios":"Sedan (Dzire/Etios)",
    "swift":"Sedan (Dzire/Etios)","sedan":"Sedan (Dzire/Etios)",
    "tempo traveller":"Tempo Traveller","tempo traveler":"Tempo Traveller","traveller":"Tempo Traveller",
    "urbania":"Force Urbania","force":"Force Urbania",
    "mini bus":"Mini Bus","minibus":"Mini Bus","bus":"Mini Bus",
    "eeco":"Eeco","luxury":"Luxury","suv":"SUV (generic)","xylo":"SUV (generic)",
    "scorpio":"SUV (generic)","bolero":"SUV (generic)","fortuner":"Luxury","audi":"Luxury","bmw":"Luxury",
    "tavera":"SUV (generic)","marazzo":"SUV (generic)","carens":"SUV (generic)","tempo":"Tempo Traveller",
}
DESTS = ["goa","gokarna","bangalore","belgaum","dandeli","murudeshwar","hampi","sirsi",
    "shimoga","jog","davangere","dharwad","mumbai","hyderabad","mysore","karwar","badami",
    "bijapur","vijayapura","kolhapur","pune","solapur","mantralaya","tirupati","sringeri",
    "udupi","mangalore","ankola","yellapur","haveri","gadag","ranebennur","alnavar",
    "kundgol","saundatti","yellamma","panaji","calangute","madgaon","margao","vasco",
    "airport","hospet","koppal","bagalkot","hukkeri","gokak","athani","chikodi","nipani",
    "sangli","miraj","belur","halebidu","chikmagalur","sakleshpur","hassan","gokarn",
    "yana","magod","unkal","kalghatgi","mundgod","haliyal","tadas","shiggaon","savanur",
    "lakshmeshwar","annigeri","navalgund","nargund","ron","gajendragad","ilkal","hungund",
    "almatti","kudalasangama","pattadakal","aihole","mahakuta","banashankari","amingad"]
PRICE_WORDS = ["price","fare","rate","charge","cost","per km","cheap","cheapest","tariff","package price"]
TIME_WORDS = ["24 hour","24 7","24x7","night","now","today","tomorrow","urgent"]
AIRPORT_WORDS = ["airport"]
SERVICE_MAP = [
    ("airport", "airport"),
    ("outstation", "outstation"),
    ("wedding|marriage", "wedding"),
    ("corporate|office|employee|staff", "corporate"),
    ("tour|trip|package|darshan|jyotirlinga|pilgrim", "tour-package"),
    ("railway|station pickup", "railway"),
    ("local|city ride|hourly|8 hour|per day|full day|one day|monthly", "local-package"),
    ("travels|travel agency|tours and travel", "travels-generic"),
    ("driver for|driver only|acting driver|call driver|driver service", "driver-hire"),
]
CORE_PAT = re.compile(r"\b(car rental|rent a car|car rent|rental car|car for rent|car hire|hire car|rent car|car booking|book a car|car on rent|taxi|cab)\b")
AUTO_REPAIR = re.compile(r"\bcar (service|servicing|wash|repair|garage)\b")

def find_route(t):
    m = re.search(r"([a-z ]+?)\s+to\s+([a-z ]+)", t)
    if not m: return "", ""
    o, d = m.group(1).strip(), m.group(2).strip()
    o = o.split()[-1] if o else ""
    for known in DESTS + ["hubli"]:
        if d.startswith(known) or known in d.split():
            return o, known
    return o, d.split()[0] if d else ""

def classify(t):
    """returns intent, modifier, cluster, route, veh"""
    origin, dest = find_route(t)
    route = f"{origin}->{dest}" if dest else ""
    veh = ""
    for k, v in VEHICLES.items():
        if re.search(rf"\b{k}\b", t): veh = v; break

    if any(w in t for w in OWN_BRAND):
        return "navigational", "brand", "brand-own", route, veh
    if any(w in t for w in COMPETITORS):
        return "navigational", "brand", "competitor", route, veh
    if any(w in t for w in JOB_WORDS):
        return "job-seeker", "none", "job-irrelevant", route, veh
    if any(w in t for w in SELF_DRIVE):
        return "irrelevant", "service", "self-drive", route, veh
    if AUTO_REPAIR.search(t) and not CORE_PAT.search(t):
        return "irrelevant", "none", "auto-repair", route, veh
    if (not dest) and "hubli" not in t and "dharwad" not in t and any(re.search(rf"\b{c}\b", t) for c in WRONG_GEO):
        return "irrelevant", "geo", "wrong-geo", route, veh
    if "travels" in t or "travel agency" in t:
        if "hubli" in t or "dharwad" in t or "near me" in t:
            return "transactional", "none", "travels-local", route, veh

    is_price = any(w in t for w in PRICE_WORDS)
    is_time = any(w in t for w in TIME_WORDS)

    if "airport" in t:
        return "transactional", "service", "airport", route, veh
    if dest and dest != "hubli" and origin in ("hubli",""):
        cl = f"route-{dest}"
        return "transactional", "geo", cl, route, veh
    if dest == "hubli" and origin and origin != "hubli":
        return "transactional", "geo", f"route-into-hubli-{origin}", route, veh
    if veh:
        return "transactional", "vehicle", f"vehicle-{veh.lower().replace(' ','-').replace('/','-')}", route, veh
    for pat, svc in SERVICE_MAP:
        if re.search(rf"\b(?:{pat})\b", t):
            return "transactional", "service", svc, route, veh
    if CORE_PAT.search(t):
        if "hubli" in t or "near me" in t or "dharwad" in t:
            mod = "price" if is_price else ("time" if is_time else "none")
            return "transactional", mod, "core-local", route, veh
        if is_price:
            return "informational", "price", "price-generic", route, veh
        return "transactional", "none", "core-generic", route, veh
    if is_price:
        return "informational", "price", "price-generic", route, veh
    if "hubli" in t or "dharwad" in t:
        return "informational", "geo", "misc-local", route, veh
    return "irrelevant", "none", "misc-irrelevant", route, veh

PAGE_MAP = {
    "core-local": "/ (homepage)",
    "brand-own": "/ (homepage)",
    "airport": "MISSING PAGE -> /services/airport-taxi-hubli/",
    "local-package": "MISSING PAGE -> /services/local-taxi-hubli/",
    "outstation": "MISSING PAGE -> /services/outstation-cabs-hubli/",
    "wedding": "MISSING PAGE -> /services/wedding-car-rental-hubli/",
    "corporate": "MISSING PAGE -> /services/corporate-cab-hubli/",
    "tour-package": "MISSING PAGE -> /services/outstation-cabs-hubli/",
    "railway": "MISSING PAGE -> /services/local-taxi-hubli/",
    "travels-generic": "/ (homepage)",
    "travels-local": "/ (homepage)",
    "auto-repair": "NONE",
    "wrong-geo": "NONE",
    "driver-hire": "NONE (service unclear - ask Sayed)",
    "self-drive": "NONE (service not offered)",
    "competitor": "NONE (paid-only decision)",
    "job-irrelevant": "NONE",
    "misc-irrelevant": "NONE",
    "price-generic": "MISSING PAGE -> /fare/hubli-taxi-fare/",
    "misc-local": "/ (homepage)",
    "core-generic": "/ (homepage)",
}
def page_for(cluster, veh):
    if cluster.startswith("route-into-hubli"):
        return "MISSING PAGE -> route page (reverse direction)"
    if cluster.startswith("route-"):
        d = cluster[6:]
        return f"MISSING PAGE -> /routes/hubli-to-{d}-taxi/"
    if cluster.startswith("vehicle-"):
        return f"MISSING PAGE -> /vehicles/{cluster[8:]}-hubli/"
    return PAGE_MAP.get(cluster, "/ (homepage)")

def action_for(intent, cluster, clicks, cost, conv):
    if cluster in ("self-drive", "job-irrelevant", "misc-irrelevant", "auto-repair", "wrong-geo"):
        return "negative-keyword"
    if cluster == "competitor":
        # converting competitor terms move to a deliberate competitor campaign in Phase 6
        return "scale-paid" if conv > 0 else "negative-keyword"
    if cluster in ("brand-own", "travels-local"):
        return "scale-paid"
    if intent == "informational" and cluster == "price-generic":
        return "negative-keyword" if cost > 0 and conv == 0 else "ignore"
    if cluster == "core-local":
        return "scale-paid"
    if cluster.startswith("route-") or cluster.startswith("vehicle-") or cluster in (
        "airport","outstation","local-package","wedding","corporate","tour-package","railway"):
        return "both" if (clicks > 0 or conv > 0) else "build-organic-page"
    if cluster in ("core-generic","misc-local","travels-generic","driver-hire"):
        return "ignore"
    return "ignore"

# ---------- run ----------
agg = defaultdict(lambda: {"terms": set(), "impr":0.0,"clicks":0.0,"cost":0.0,"conv":0.0})
rows_in = 0
with open(SRC, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        rows_in += 1
        n = normalize(r["Search term"])
        a = agg[n]
        a["terms"].add(r["Search term"])
        a["impr"] += num(r["Impr."]); a["clicks"] += num(r["Clicks"])
        a["cost"] += num(r["Cost"]);  a["conv"]  += num(r["Conversions"])

out_rows = []
for n, a in agg.items():
    intent, mod, cluster, route, veh = classify(n)
    ctr = a["clicks"]/a["impr"] if a["impr"] else 0
    cpc = a["cost"]/a["clicks"] if a["clicks"] else 0
    cvr = a["conv"]/a["clicks"] if a["clicks"] else 0
    cpa = a["cost"]/a["conv"] if a["conv"] else 0
    out_rows.append({
        "search_term": " | ".join(sorted(a["terms"]))[:200],
        "normalized": n,
        "impressions": int(a["impr"]), "clicks": int(a["clicks"]),
        "cost": round(a["cost"],2), "conversions": round(a["conv"],2),
        "conv_value": "",  # not present in source report
        "ctr": round(ctr,4), "cpc": round(cpc,2), "cvr": round(cvr,4), "cpa": round(cpa,2),
        "intent": intent, "modifier_type": mod, "cluster": cluster, "route": route,
        "serp_intent_match": page_for(cluster, veh),
        "action": action_for(intent, cluster, a["clicks"], a["cost"], a["conv"]),
    })

out_rows.sort(key=lambda r: (-r["conversions"], -r["cost"]))
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
    w.writeheader(); w.writerows(out_rows)

# ---------- summaries ----------
def group(rows, key):
    g = defaultdict(lambda: {"n":0,"impr":0,"clicks":0,"cost":0.0,"conv":0.0})
    for r in rows:
        k = key(r); d = g[k]
        d["n"]+=1; d["impr"]+=r["impressions"]; d["clicks"]+=r["clicks"]
        d["cost"]+=r["cost"]; d["conv"]+=r["conversions"]
    return {k:{**v,"cost":round(v["cost"],2),"conv":round(v["conv"],2)} for k,v in g.items()}

summary = {
    "rows_in": rows_in, "unique_normalized": len(out_rows),
    "totals": {"impr":sum(r["impressions"] for r in out_rows),
               "clicks":sum(r["clicks"] for r in out_rows),
               "cost":round(sum(r["cost"] for r in out_rows),2),
               "conv":round(sum(r["conversions"] for r in out_rows),2)},
    "by_intent": group(out_rows, lambda r: r["intent"]),
    "by_cluster": group(out_rows, lambda r: r["cluster"]),
    "by_action": group(out_rows, lambda r: r["action"]),
    "routes": group([r for r in out_rows if r["cluster"].startswith("route-")], lambda r: r["cluster"]),
    "bleeders_top": [
        {k:r[k] for k in ("normalized","clicks","cost","cluster")}
        for r in sorted([r for r in out_rows if r["cost"]>0 and r["conversions"]==0],
                        key=lambda r:-r["cost"])[:40]],
    "bleed_total": round(sum(r["cost"] for r in out_rows if r["cost"]>0 and r["conversions"]==0),2),
    "money_by_conv": [
        {k:r[k] for k in ("normalized","clicks","cost","conversions","cpa","cluster")}
        for r in sorted([r for r in out_rows if r["conversions"]>0], key=lambda r:-r["conversions"])[:30]],
    "money_by_cvr_min5clicks": [
        {k:r[k] for k in ("normalized","clicks","cost","conversions","cvr","cluster")}
        for r in sorted([r for r in out_rows if r["clicks"]>=5 and r["conversions"]>0],
                        key=lambda r:-r["cvr"])[:30]],
    "self_drive": group([r for r in out_rows if r["cluster"]=="self-drive"], lambda r: "all"),
    "vehicle_clusters": group([r for r in out_rows if r["cluster"].startswith("vehicle-")], lambda r: r["cluster"]),
}
with open(SUMMARY, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=1)
print(json.dumps({k: summary[k] for k in ("rows_in","unique_normalized","totals","by_intent","by_action","bleed_total")}, indent=1))
print("\nCLUSTERS (cost desc):")
for k,v in sorted(summary["by_cluster"].items(), key=lambda kv:-kv[1]["cost"]):
    print(f"  {k:32s} terms:{v['n']:4d} clicks:{v['clicks']:5d} cost:{v['cost']:10.2f} conv:{v['conv']:6.2f}")
