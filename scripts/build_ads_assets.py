# Phase 6c/6d — RSAs + extensions into /ads/import/. Validates char limits (H<=30, D<=90,
# sitelink text<=25, callout<=25, snippet value<=25). One strong RSA per ad group (Google
# recommends 1 RSA/ad group; 3 near-duplicates hurt more than help — documented in README).
import csv, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'ads', 'import')
DOMAIN = 'https://trishikacarrentalhubli.in'
errors = []
def chk(s, lim, ctx):
    if len(s) > lim: errors.append(f'{ctx}: {len(s)}>{lim} :: {s}')
    return s

# shared headline pool (each <=30)
POOL = ['Trishika Car Rental Hubli','24/7 Cabs, Book in Minutes','Clean AC Cars With Driver',
 'From Rs 10/km, No Surge','Call +91 82175 77849','Transparent Per-KM Rates',
 '5.0 Star, 58 Google Reviews','Verified Local Drivers','No Hidden Charges',
 'Instant WhatsApp Booking','Hubli, Dharwad & Outstation','On-Time, Every Time']
DESC = ['Book clean AC cars with professional drivers across Hubli-Dharwad. Call or WhatsApp now.',
 'Transparent per-km rates from Rs 10/km. No surge, no hidden charges. Available 24/7.',
 'Airport, outstation and local trips. Rated 5.0 stars by 58 riders on Google. Book fast.',
 'Call +91 82175 77849 for instant booking. Verified drivers, on-time pickups, fair fares.']

# ad group -> (pinned H1, [theme extra headlines], [theme descriptions override or []], final url)
RSA = {
 'Car Rental Hubli': ('Car Rental in Hubli', ['Rent a Car in Hubli','Car Rental With Driver','Sedan, SUV & Tempo'], [], f'{DOMAIN}/'),
 'Taxi & Cab Hubli': ('Taxi Service in Hubli', ['Cab Service in Hubli','Book a Cab in Hubli','Local & Outstation Cabs'], [], f'{DOMAIN}/'),
 'Travels Hubli': ('Hubli Car Travels', ['Trusted Hubli Travels','Cars With Driver','Local & Outstation Trips'], [], f'{DOMAIN}/'),
 'Airport Taxi HBX': ('Hubli Airport Taxi HBX', ['Flight-Tracked Pickups','Airport Drop From Rs 10/km','Dharwad Airport Cabs'],
    ['Pickup and drop for every flight at Hubli Airport HBX. Flight-tracked, driver waits free.',
     'Our office is on Gokul Road, minutes from HBX. Fixed rates, no surge, 24/7 airport runs.',
     'Book Hubli airport taxi on call or WhatsApp +91 82175 77849. On-time, clean AC cars.',
     'Dharwad to Hubli Airport and outstation onward trips. Transparent per-km pricing.'], f'{DOMAIN}/services/airport-taxi-hubli/'),
 'Route - Goa': ('Hubli to Goa Taxi', ['160 km, 4.5 hrs, AC Cabs','Round Trip & One-Way','Via Anmod Ghat'],
    ['Door-to-door cab from Hubli to Goa, about 160 km via Anmod Ghat. AC cars with driver.',
     '2-day Sedan round trip from about Rs 7,800 + tolls. Innova & Tempo also available.',
     'Book Hubli to Goa taxi on call or WhatsApp +91 82175 77849. One-way drops on request.',
     'Transparent per-km billing, driver batta stated upfront, tolls at actuals. No surprises.'], f'{DOMAIN}/routes/hubli-to-goa-taxi/'),
 'Route - Bangalore': ('Hubli to Bangalore Cab', ['420 km on NH-48','One-Way Drops Available','Doorstep to Doorstep'],
    ['Comfortable AC cab from Hubli to Bengaluru, about 420 km on NH-48, roughly 7 hours.',
     'One-way Sedan drop from about Rs 5,340 + tolls. No station queues, luggage door-to-door.',
     'Book on call or WhatsApp +91 82175 77849. BLR airport pickups timed to your flight.',
     'Transparent per-km rates, verified highway drivers, on-time pickups. Both directions.'], f'{DOMAIN}/routes/hubli-to-bangalore-taxi/'),
 'Route - Dandeli': ('Hubli to Dandeli Cab', ['75 km, 2 Hours','Rafting Day Trips','Groups by Tempo'],
    ['Hubli to Dandeli cab, just 75 km via Kalghatgi. Day trips, resort drops, rafting groups.',
     'Day trip by Sedan about Rs 3,900; the cab waits through your rafting slot. AC cars.',
     'Book on call or WhatsApp +91 82175 77849. Tempo Traveller for groups of 12.',
     'Transparent per-km rates, forest-road drivers, honest billing. No hidden charges.'], f'{DOMAIN}/routes/hubli-to-dandeli-taxi/'),
 'Route - Gokarna': ('Hubli to Gokarna Cab', ['150 km, Temple + Beach','Day Trips Possible','AC Cars With Driver'],
    ['Hubli to Gokarna cab, about 150 km via Yellapur and Ankola, roughly 3.5 hours.',
     'Temple darshan and Om Beach in a day, about Rs 3,900 by Sedan including batta.',
     'Book on call or WhatsApp +91 82175 77849. Add Murudeshwar for a coastal double.',
     'Transparent per-km rates, ghat-experienced drivers, fair fares. No surge pricing.'], f'{DOMAIN}/routes/hubli-to-gokarna-taxi/'),
 'Route - Belgaum': ('Hubli to Belgaum Taxi', ['100 km, 2 Hours','Business & Medical Runs','IXG Airport Drops'],
    ['Hubli to Belgaum (Belagavi) taxi, about 100 km on NH-48 via Kittur, roughly 2 hours.',
     'Same-day return about Rs 3,900 with the cab on standby through your work. AC cars.',
     'Book on call or WhatsApp +91 82175 77849. KLE hospital and IXG airport runs.',
     'Transparent per-km rates, both directions, verified drivers. No hidden charges.'], f'{DOMAIN}/routes/hubli-to-belgaum-taxi/'),
 'Tempo Traveller & Group': ('Tempo Traveller Hubli', ['12-17 Seater AC','Rs 19/km + Driver','Mini Bus 21-25 Seats'],
    ['AC Tempo Traveller (12-17 seater) with driver for groups, weddings and tours from Hubli.',
     'From Rs 19/km + batta. Mini Bus for 21-25 passengers. Goa, Dandeli, pilgrim trips.',
     'Book on call or WhatsApp +91 82175 77849. One vehicle, whole group, one bill.',
     'Transparent per-km rates, experienced drivers, honest billing. No hidden charges.'], f'{DOMAIN}/vehicles/tempo-traveller-hubli/'),
}

# ad group -> campaign (mirrors build_ads_import.py)
AG_CAMP = {
 'Car Rental Hubli':'Search - Core Local','Taxi & Cab Hubli':'Search - Core Local','Travels Hubli':'Search - Core Local',
 'Airport Taxi HBX':'Search - Airport',
 'Route - Goa':'Search - Outstation Routes','Route - Bangalore':'Search - Outstation Routes',
 'Route - Dandeli':'Search - Outstation Routes','Route - Gokarna':'Search - Outstation Routes',
 'Route - Belgaum':'Search - Outstation Routes',
 'Tempo Traveller & Group':'Search - Vehicles'}
PATHS = {'Car Rental Hubli':('Car-Rental','Hubli'),'Taxi & Cab Hubli':('Taxi-Service','Hubli'),
 'Travels Hubli':('Car-Travels','Hubli'),'Airport Taxi HBX':('Airport-Taxi','Hubli'),
 'Route - Goa':('Hubli-to-Goa','Cab'),'Route - Bangalore':('Hubli-Bangalore','Cab'),
 'Route - Dandeli':('Hubli-Dandeli','Cab'),'Route - Gokarna':('Hubli-Gokarna','Cab'),
 'Route - Belgaum':('Hubli-Belgaum','Taxi'),'Tempo Traveller & Group':('Tempo-Traveller','Hubli')}

# build 15 headlines per ad group: pinned H1 + 3 theme + fill from POOL (dedup, cap 15)
def headlines(ag, h1, extra):
    hl = [h1] + extra + [h for h in POOL if h not in extra]
    return hl[:15]

hdr = ['Campaign','Ad Group']
for i in range(1,16): hdr += [f'Headline {i}', f'Headline {i} position']
for i in range(1,5): hdr.append(f'Description {i}')
hdr += ['Path 1','Path 2','Final URL']

rsa_rows = []
for ag,(h1,extra,dov,url) in RSA.items():
    hl = headlines(ag, chk(h1,30,f'{ag} H1'), [chk(x,30,f'{ag} Hx') for x in extra])
    descs = dov if dov else DESC
    for d in descs: chk(d,90,f'{ag} D')
    p1,p2 = PATHS[ag]; chk(p1,15,f'{ag} path1'); chk(p2,15,f'{ag} path2')
    row = [AG_CAMP[ag], ag]
    for i,h in enumerate(hl):
        chk(h,30,f'{ag} H{i+1}')
        row += [h, '1' if i==0 else '']   # pin only H1 to position 1
    # pad if fewer than 15
    for _ in range(15-len(hl)): row += ['','']
    row += list(descs[:4]) + [p1,p2,url]
    rsa_rows.append(row)
with open(os.path.join(OUT,'rsa.csv'),'w',newline='',encoding='utf-8') as f:
    csv.writer(f).writerows([hdr]+rsa_rows)
print(f'rsa.csv {len(rsa_rows)} ads')

# ---------------- sitelinks.csv (8, account/campaign level) ----------------
SITELINKS = [
 ('Airport Taxi (HBX)','Flight-tracked pickup & drop','24/7, fixed rates, driver waits',f'{DOMAIN}/services/airport-taxi-hubli/'),
 ('Outstation Cabs','Goa, Gokarna, Bangalore & more','Per-km rates from Rs 10/km',f'{DOMAIN}/services/outstation-cabs-hubli/'),
 ('Tempo Traveller','12-25 seater for groups','Weddings, tours, pilgrim trips',f'{DOMAIN}/vehicles/tempo-traveller-hubli/'),
 ('Taxi Fares & Rates','Full rate card, no surge','Sedan to Mini Bus per-km rates',f'{DOMAIN}/fare/hubli-taxi-fare/'),
 ('Hubli to Goa','160 km, AC cabs with driver','From about Rs 7,800 round trip',f'{DOMAIN}/routes/hubli-to-goa-taxi/'),
 ('Hubli to Bangalore','420 km one-way or round','From about Rs 5,340 one-way',f'{DOMAIN}/routes/hubli-to-bangalore-taxi/'),
 ('Book on WhatsApp','Instant estimate in minutes','No app, no account needed',f'{DOMAIN}/#cabForm'),
 ('Rate Estimator','Get your fare before booking','Outstation & local packages',f'{DOMAIN}/#estimator'),
]
srows=[]
for t,d1,d2,u in SITELINKS:
    chk(t,25,'sitelink text'); chk(d1,35,'sl d1'); chk(d2,35,'sl d2')
    srows.append([t,d1,d2,u])
w = lambda n,h,r: (lambda p: (csv.writer(open(p,'w',newline='',encoding='utf-8')).writerow(h) or
    csv.writer(open(p,'a',newline='',encoding='utf-8')).writerows(r)))(os.path.join(OUT,n))
import csv as _csv
def writecsv(n,h,r):
    with open(os.path.join(OUT,n),'w',newline='',encoding='utf-8') as f:
        wr=_csv.writer(f); wr.writerow(h); wr.writerows(r)
    print(f'{n} {len(r)} rows')
writecsv('sitelinks.csv',['Sitelink Text','Description Line 1','Description Line 2','Final URL'],srows)

# ---------------- callouts.csv (10) ----------------
CALLOUTS=['24/7 Availability','Clean AC Cars','Verified Drivers','No Hidden Charges',
 'From Rs 10/km','Airport Transfers','Outstation Cabs','Instant WhatsApp Booking',
 'On-Time Pickups','5.0 Star Rated']
for c in CALLOUTS: chk(c,25,'callout')
writecsv('callouts.csv',['Callout Text'],[[c] for c in CALLOUTS])

# ---------------- structured_snippets.csv ----------------
SNIP_HEADER='Service catalog'
SNIP=['Airport Taxi','Outstation Cabs','Local City Rides','Tempo Traveller','Wedding Cars','Railway Pickup']
for s in SNIP: chk(s,25,'snippet')
writecsv('structured_snippets.csv',['Header','Value'],[[SNIP_HEADER,s] for s in SNIP])

if errors:
    print('\n*** CHAR-LIMIT ERRORS ***'); [print(' -',e) for e in errors]
else:
    print('\nAll assets within character limits.')

