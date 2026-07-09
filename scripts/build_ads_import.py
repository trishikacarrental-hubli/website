# Phase 6d — generate Google Ads Editor import CSVs into /ads/import/
# Formats target Google Ads Editor's per-section paste (Keywords grid, Negatives grid,
# Ads grid, Assets). Headers verified against Ads Editor export columns; README flags
# any that should be double-checked before posting.
import csv, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'ads', 'import')
os.makedirs(OUT, exist_ok=True)
DOMAIN = 'https://trishikacarrentalhubli.in'

def w(name, header, rows):
    with open(os.path.join(OUT, name), 'w', newline='', encoding='utf-8') as f:
        wr = csv.writer(f); wr.writerow(header); wr.writerows(rows)
    print(f'{name:26s} {len(rows)} rows')

# ---------------- structure ----------------
CAMPAIGNS = [
    # Campaign, Type, Daily Budget (INR), Bid Strategy, Networks
    ['Search - Core Local', 'Search', '300', 'Manual CPC', 'Google search'],
    ['Search - Airport', 'Search', '80', 'Manual CPC', 'Google search'],
    ['Search - Outstation Routes', 'Search', '120', 'Manual CPC', 'Google search'],
    ['Search - Vehicles', 'Search', '60', 'Manual CPC', 'Google search'],
]

# ad group -> (campaign, max cpc, final url)
AG = {
    'Car Rental Hubli':  ('Search - Core Local', '25', f'{DOMAIN}/'),
    'Taxi & Cab Hubli':  ('Search - Core Local', '25', f'{DOMAIN}/'),
    'Travels Hubli':     ('Search - Core Local', '22', f'{DOMAIN}/'),
    'Airport Taxi HBX':  ('Search - Airport', '22', f'{DOMAIN}/services/airport-taxi-hubli/'),
    'Route - Goa':       ('Search - Outstation Routes', '22', f'{DOMAIN}/routes/hubli-to-goa-taxi/'),
    'Route - Bangalore': ('Search - Outstation Routes', '22', f'{DOMAIN}/routes/hubli-to-bangalore-taxi/'),
    'Route - Dandeli':   ('Search - Outstation Routes', '22', f'{DOMAIN}/routes/hubli-to-dandeli-taxi/'),
    'Route - Gokarna':   ('Search - Outstation Routes', '22', f'{DOMAIN}/routes/hubli-to-gokarna-taxi/'),
    'Route - Belgaum':   ('Search - Outstation Routes', '22', f'{DOMAIN}/routes/hubli-to-belgaum-taxi/'),
    'Tempo Traveller & Group': ('Search - Vehicles', '22', f'{DOMAIN}/vehicles/tempo-traveller-hubli/'),
}

# ad group -> list of (keyword, match) ; match in {Phrase, Exact}
KW = {
    'Car Rental Hubli': [
        ('car rental in hubli','Exact'), ('car rental in hubli','Phrase'),
        ('car rental hubli','Phrase'), ('rental car in hubli','Phrase'),
        ('car for rent hubli','Phrase'), ('rent a car in hubli','Phrase'),
        ('car on rent in hubli','Phrase'), ('car rental in hubli with driver','Phrase')],
    'Taxi & Cab Hubli': [
        ('taxi service in hubli','Exact'), ('taxi service in hubli','Phrase'),
        ('cab service in hubli','Phrase'), ('taxi in hubli','Phrase'),
        ('cab in hubli','Phrase'), ('hubli taxi service','Phrase'),
        ('cab booking hubli','Phrase'), ('cab service hubli','Phrase')],
    'Travels Hubli': [
        ('car travels in hubli','Phrase'), ('hubli car travels','Phrase'),
        ('travels in hubli','Phrase'), ('tours and travels in hubli','Phrase')],
    'Airport Taxi HBX': [
        ('hubli airport taxi','Phrase'), ('taxi service in hubli airport','Phrase'),
        ('hubli airport taxi service','Phrase'), ('dharwad to hubli airport taxi','Phrase')],
    'Route - Goa': [
        ('hubli to goa taxi','Phrase'), ('hubli to goa cab','Phrase'),
        ('hubli to goa car rental','Phrase'), ('hubli to goa cab fare','Phrase')],
    'Route - Bangalore': [
        ('hubli to bangalore cab','Phrase'), ('hubli to bangalore taxi','Phrase'),
        ('hubli to bangalore car rental','Phrase')],
    'Route - Dandeli': [
        ('hubli to dandeli cab','Phrase'), ('hubli to dandeli taxi','Phrase'),
        ('hubli to dandeli car rental','Phrase')],
    'Route - Gokarna': [
        ('hubli to gokarna cab','Phrase'), ('hubli to gokarna taxi','Phrase'),
        ('hubli to gokarna car rental','Phrase')],
    'Route - Belgaum': [
        ('hubli to belgaum cab','Phrase'), ('hubli to belgaum taxi','Phrase')],
    'Tempo Traveller & Group': [
        ('tempo traveller in hubli','Phrase'), ('tempo traveller rent in hubli','Phrase'),
        ('tempo traveller rent per km in hubli','Phrase'), ('force urbania for rent in hubli','Phrase'),
        ('mini bus rent in hubli','Phrase')],
}

# ---------------- campaigns.csv ----------------
w('campaigns.csv',
  ['Campaign','Campaign Type','Campaign Daily Budget','Bid Strategy Type','Networks','Campaign Status'],
  [[c[0],c[1],c[2],c[3],c[4],'Paused'] for c in CAMPAIGNS])

# ---------------- ad_groups.csv ----------------
w('ad_groups.csv',
  ['Campaign','Ad Group','Max CPC','Ad Group Status'],
  [[v[0],k,v[1],'Paused'] for k,v in AG.items()])

# ---------------- keywords.csv ----------------
kw_rows = []
for ag,(camp,cpc,url) in AG.items():
    for term,match in KW[ag]:
        kw_rows.append([camp, ag, term, match, cpc])
w('keywords.csv', ['Campaign','Ad Group','Keyword','Match Type','Max CPC'], kw_rows)

# ---------------- negatives_campaign.csv (shared, applied to all 4 campaigns) ----------------
NEG_PHRASE = ['self drive','self driven','self driving','without driver','self car','self rental',
 'rapido','ola','uber','zoom car','zoomcar','namma yatri','blusmart','red taxi','bharat taxi',
 'bharath taxi','taxisafar','job','salary','vacancy','hiring','olx','second hand','used car',
 'car sale','driving school','car wash','car service','car repair','car servicing','insurance','loan']
NEG_EXACT = ['[car rental rishikesh]','[hassan cab service]','[guwahati to tezpur car fare]',
 '[car service in hubli]','[hubli car service]','[bangalore to hubli]']
neg_rows = []
for camp in [c[0] for c in CAMPAIGNS]:
    for t in NEG_PHRASE:
        neg_rows.append([camp, t, 'Phrase'])
    for t in NEG_EXACT:
        neg_rows.append([camp, t.strip('[]'), 'Exact'])
w('negatives_campaign.csv', ['Campaign','Negative Keyword','Match Type'], neg_rows)

# ---------------- negatives_adgroup.csv (cross-theme, prevent cannibalization) ----------------
# each ad group excludes the OTHER themes' head terms
adneg = []
def addneg(ag, terms, match='Phrase'):
    camp = AG[ag][0]
    for t in terms: adneg.append([camp, ag, t, match])
# Core-local ad groups should not eat airport / route / vehicle intent
for ag in ['Car Rental Hubli','Taxi & Cab Hubli','Travels Hubli']:
    addneg(ag, ['airport','tempo traveller','mini bus','urbania',
                'to goa','to bangalore','to dandeli','to gokarna','to belgaum','outstation'])
# Route/airport/vehicle groups don't need core negatives (their phrase terms are specific),
# but keep airport out of routes and vice versa where overlap is possible:
for ag in ['Route - Goa','Route - Bangalore','Route - Dandeli','Route - Gokarna','Route - Belgaum']:
    addneg(ag, ['airport','tempo traveller'])
addneg('Airport Taxi HBX', ['to goa','to bangalore','tempo traveller'])
addneg('Tempo Traveller & Group', ['airport'])
w('negatives_adgroup.csv', ['Campaign','Ad Group','Negative Keyword','Match Type'], adneg)

print('DONE structure files. RSAs + extensions next (build_ads_assets.py).')
