# Phase 4 — inject JSON-LD into /site-optimized/ pages.
# - Homepage: upgrade LocalBusiness/TaxiService (@id, Google Maps sameAs)
# - Subpages: Service + BreadcrumbList + FAQPage (FAQs parsed from the page's own HTML)
# Idempotent: strips previously-injected phase4 blocks before re-adding.
import os, re, json
from html import unescape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SO = os.path.join(ROOT, 'site-optimized')
DOMAIN = 'https://trishikacarrentalhubli.in'
BIZ_ID = f'{DOMAIN}/#business'
MAPS_CID = int('7a62f19360002a86', 16)  # from the GBP place id -> cid decimal
MAPS_URL = f'https://maps.google.com/?cid={MAPS_CID}'

PAGES = {
    'services/airport-taxi-hubli/index.html': {
        'crumbs': [('Home', '/'), ('Services', '/services/outstation-cabs-hubli/'), ('Airport Taxi Hubli', '/services/airport-taxi-hubli/')],
        'service': {'name': 'Hubli Airport Taxi (HBX)', 'serviceType': 'Airport taxi service',
                    'desc': 'Pickup and drop for all flights at Hubli Airport (HBX), Gokul Road — flight-tracked, 24/7, fixed transparent rates. Serving Hubli city and Dharwad.'},
    },
    'vehicles/tempo-traveller-hubli/index.html': {
        'crumbs': [('Home', '/'), ('Vehicles', '/vehicles/tempo-traveller-hubli/'), ('Tempo Traveller Hubli', '/vehicles/tempo-traveller-hubli/')],
        'service': {'name': 'Tempo Traveller on Rent in Hubli', 'serviceType': 'Group vehicle rental with driver',
                    'desc': 'AC Tempo Traveller (12+1) and Mini Bus (21–25 seater) with driver for group trips, weddings and tours from Hubli-Dharwad. From ₹19/km + driver batta.'},
    },
    'services/outstation-cabs-hubli/index.html': {
        'crumbs': [('Home', '/'), ('Services', '/services/outstation-cabs-hubli/'), ('Outstation Cabs Hubli', '/services/outstation-cabs-hubli/')],
        'service': {'name': 'Outstation Cabs from Hubli', 'serviceType': 'Outstation taxi service',
                    'desc': 'Round trips and one-way drops from Hubli-Dharwad across Karnataka, Goa and Maharashtra. Per-km rates from ₹10, minimum 300 km/day, driver batta stated upfront.'},
    },
    'fare/hubli-taxi-fare/index.html': {
        'crumbs': [('Home', '/'), ('Fares', '/fare/hubli-taxi-fare/'), ('Hubli Taxi Fare & Rates', '/fare/hubli-taxi-fare/')],
        'service': None,  # rate card page: FAQ + breadcrumb only
    },
}
ROUTES = {
    'hubli-to-goa-taxi': ('Goa', 'Hubli to Goa taxi — about 160 km via Anmod Ghat, 4–4.5 hours. Round trips and one-way drops with driver.'),
    'hubli-to-bangalore-taxi': ('Bangalore', 'Hubli to Bangalore cab — about 420 km on NH-48, ~7 hours. One-way and round trips with driver.'),
    'hubli-to-dandeli-taxi': ('Dandeli', 'Hubli to Dandeli taxi — 75 km, ~2 hours. Day trips, rafting groups and resort drops.'),
    'hubli-to-gokarna-taxi': ('Gokarna', 'Hubli to Gokarna cab — about 150 km via Yellapur and Ankola, 3.5 hours. Temple and beach trips.'),
    'hubli-to-belgaum-taxi': ('Belgaum', 'Hubli to Belgaum (Belagavi) taxi — about 100 km on NH-48, 2 hours. Business, medical and airport runs.'),
}
for slug, (dest, desc) in ROUTES.items():
    PAGES[f'routes/{slug}/index.html'] = {
        'crumbs': [('Home', '/'), ('Outstation Routes', '/services/outstation-cabs-hubli/'), (f'Hubli to {dest} Taxi', f'/routes/{slug}/')],
        'service': {'name': f'Hubli to {dest} Taxi', 'serviceType': 'Outstation taxi service', 'desc': desc},
    }

FAQ_RE = re.compile(
    r'<button class="faq-q" aria-expanded="false">\s*(.*?)\s*<span class="faq-arrow">.*?</button>\s*<div class="faq-a">(.*?)</div>',
    re.S)
MARK_START = '<!-- phase4-schema -->'
MARK_END = '<!-- /phase4-schema -->'

def clean(s):
    return unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s))).strip()

def block(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + '\n</script>'

count = 0
for rel, cfg in PAGES.items():
    path = os.path.join(SO, rel.replace('/', os.sep))
    html = open(path, encoding='utf-8').read()
    html = re.sub(re.escape(MARK_START) + '.*?' + re.escape(MARK_END), '', html, flags=re.S)
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', html).group(1)

    blocks = []
    blocks.append(block({
        '@context': 'https://schema.org', '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': DOMAIN + u}
            for i, (n, u) in enumerate(cfg['crumbs'])],
    }))
    if cfg['service']:
        s = cfg['service']
        blocks.append(block({
            '@context': 'https://schema.org', '@type': 'Service',
            '@id': canonical + '#service',
            'name': s['name'], 'serviceType': s['serviceType'], 'description': s['desc'],
            'url': canonical,
            'provider': {'@id': BIZ_ID},
            'areaServed': [{'@type': 'City', 'name': 'Hubballi'}, {'@type': 'City', 'name': 'Dharwad'}],
            'availableChannel': {'@type': 'ServiceChannel', 'servicePhone': '+918217577849', 'serviceUrl': canonical},
        }))
    faqs = [(clean(q), clean(a)) for q, a in FAQ_RE.findall(html)]
    if faqs:
        blocks.append(block({
            '@context': 'https://schema.org', '@type': 'FAQPage',
            'mainEntity': [{'@type': 'Question', 'name': q,
                            'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faqs],
        }))
    inject = f'  {MARK_START}\n  ' + '\n  '.join(blocks) + f'\n  {MARK_END}\n</head>'
    html = html.replace('</head>', inject, 1)
    open(path, 'w', encoding='utf-8').write(html)
    print(f'{rel:48s} breadcrumb + {"service + " if cfg["service"] else ""}{len(faqs)} FAQs')
    count += 1

# ---- homepage LocalBusiness upgrade ----
ix = os.path.join(SO, 'index.html')
html = open(ix, encoding='utf-8').read()
html = html.replace('"@type": ["LocalBusiness", "TaxiService"],\n    "name": "Trishika Car Rental Hubli",',
    f'"@type": ["LocalBusiness", "TaxiService"],\n    "@id": "{BIZ_ID}",\n    "name": "Trishika Car Rental Hubli",')
html = html.replace('''"sameAs": [
      "https://www.instagram.com/trishika_car_rentals_offical",
      "https://www.facebook.com/share/1Ttc9pSKWr/"
    ]''', f'''"sameAs": [
      "https://www.instagram.com/trishika_car_rentals_offical",
      "https://www.facebook.com/share/1Ttc9pSKWr/",
      "{MAPS_URL}"
    ]''')
open(ix, 'w', encoding='utf-8').write(html)
print(f'index.html: @id added, Maps sameAs added ({MAPS_URL})')

# ---- validate every JSON-LD block on every page ----
print('\nValidation:')
ok = True
for dp, _, fns in os.walk(SO):
    for fn in fns:
        if not fn.endswith('.html'): continue
        p = os.path.join(dp, fn)
        h = open(p, encoding='utf-8').read()
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            try:
                obj = json.loads(m.group(1))
                t = obj.get('@type')
            except Exception as e:
                print(f'  INVALID JSON-LD in {os.path.relpath(p, SO)}: {e}'); ok = False
print('  all JSON-LD blocks parse OK' if ok else '  FIX ERRORS ABOVE')
