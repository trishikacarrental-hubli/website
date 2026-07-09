# Phase 3 — generate the 9 approved pages into /site-optimized/
# One template, per-page data. All facts either from the site's published rate card
# (script.js DATA), the homepage routes section, or arithmetic on those rates.
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SO = os.path.join(ROOT, 'site-optimized')
DOMAIN = 'https://trishikacarrentalhubli.in'
PHONE_DISPLAY = '+91 82175 77849'
TEL = 'tel:+918217577849'
WA = 'https://wa.me/918217577849'

HEAD = '''<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-P92G7GNP');</script>
<!-- End Google Tag Manager -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{canonical}" />

  <meta name="geo.region" content="IN-KA" />
  <meta name="geo.placename" content="Hubballi" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{domain}/assets/og-image.jpg" />
  <meta property="og:site_name" content="Trishika Car Rental Hubli" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&family=Inter:wght@400;500;600&display=swap"
    rel="stylesheet" />
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="/style.css" />
</head>

<body class="subpage">
    <!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P92G7GNP"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

  <div class="cursor-dot" id="cursorDot"></div>
  <div class="cursor-ring" id="cursorRing"></div>

  <header class="site-header" id="siteHeader">
    <div class="container header-inner">
      <a href="/" class="header-logo">
        <span class="logo-name">Trishika <span>Car Rental</span></span>
        <span class="logo-sub">Taxi Service in Hubli &amp; Dharwad</span>
      </a>
      <nav aria-label="Main navigation">
        <ul class="nav-links">
          <li><a href="/#cabForm">Book a Cab</a></li>
          <li><a href="/services/airport-taxi-hubli/">Airport Taxi</a></li>
          <li><a href="/#pricing">Pricing</a></li>
          <li><a href="/#estimator">Rate Estimator</a></li>
          <li><a href="/#routes">Routes</a></li>
          <li><a href="/vehicles/tempo-traveller-hubli/">Tempo Traveller</a></li>
          <li><a href="/#faq">FAQ</a></li>
        </ul>
      </nav>
      <div class="header-cta">
        <a href="{tel}" class="header-phone">{phone}</a>
        <a href="{wa}" target="_blank" rel="noopener" class="btn btn-primary">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M20.4 3.6A11.93 11.93 0 0012 0C5.4 0 .1 5.3.1 11.9c0 2.1.5 4.1 1.6 5.9L0 24l6.4-1.7c1.7.9 3.6 1.4 5.6 1.4C18.6 23.7 24 18.4 24 11.8c0-3.2-1.2-6.2-3.6-8.2z" /></svg>
          <span>WhatsApp</span>
        </a>
      </div>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
    <nav class="mobile-menu" id="mobileMenu" aria-label="Mobile navigation">
      <a href="/#cabForm">Book a Cab</a>
      <a href="/services/airport-taxi-hubli/">Airport Taxi</a>
      <a href="/#pricing">Pricing</a>
      <a href="/#estimator">Rate Estimator</a>
      <a href="/#routes">Routes</a>
      <a href="/vehicles/tempo-traveller-hubli/">Tempo Traveller</a>
      <a href="{tel}">📞 {phone}</a>
      <a href="{wa}" target="_blank" rel="noopener">💬 WhatsApp</a>
    </nav>
  </header>
'''

FOOTER = '''
  <footer class="site-footer">
    <div class="container">
      <div class="footer-top">
        <div>
          <div class="footer-logo-name">Trishika <span>Car Rental</span></div>
          <div class="footer-tagline">Taxi Service in Hubli &amp; Dharwad</div>
          <address class="footer-address-block">
            Shop No 37, Yashasvi Apt,<br>
            Gokul Rd, Gandhi Nagar,<br>
            Hubballi, Karnataka – 580030<br>
            <a href="{tel}">{phone}</a>
          </address>
        </div>
        <div>
          <div class="footer-col-title">Quick Links</div>
          <ul class="footer-links">
            <li><a href="/#cabForm">Book a Cab</a></li>
            <li><a href="/services/airport-taxi-hubli/">Airport Taxi Hubli</a></li>
            <li><a href="/vehicles/tempo-traveller-hubli/">Tempo Traveller Hubli</a></li>
            <li><a href="/services/outstation-cabs-hubli/">Outstation Cabs</a></li>
            <li><a href="/fare/hubli-taxi-fare/">Taxi Fares &amp; Rates</a></li>
            <li><a href="/#faq">FAQ</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-col-title">Popular Routes</div>
          <ul class="footer-links">
            <li><a href="/routes/hubli-to-goa-taxi/">Hubli to Goa Taxi</a></li>
            <li><a href="/routes/hubli-to-gokarna-taxi/">Hubli to Gokarna Cab</a></li>
            <li><a href="/routes/hubli-to-bangalore-taxi/">Hubli to Bangalore Cab</a></li>
            <li><a href="/routes/hubli-to-dandeli-taxi/">Hubli to Dandeli Cab</a></li>
            <li><a href="/routes/hubli-to-belgaum-taxi/">Hubli to Belgaum Taxi</a></li>
            <li><a href="/services/airport-taxi-hubli/">Hubli Airport Taxi</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 Trishika Car Rental, Hubballi, Karnataka. All rights reserved.</span>
        <span>Car Rental in Hubli | Taxi Service Hubli</span>
      </div>
    </div>
  </footer>

  <div class="float-call-pulse"></div>
  <a href="{tel}" class="float-call" aria-label="Call Trishika Car Rental">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z" /></svg>
  </a>

  <script src="/script.js" defer></script>
</body>

</html>
'''

def hero(tag, h1, desc, chips):
    chips_html = ''.join(f'<span class="r-chip">{c}</span>' for c in chips)
    return f'''
  <section class="page-hero">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> <span>›</span> {tag}</nav>
      <span class="tag">{tag}</span>
      <h1 class="display-heading">{h1}</h1>
      <p class="page-hero-desc">{desc}</p>
      <div class="page-hero-actions">
        <a href="{TEL}" class="btn btn-primary"><span>Call Now — {PHONE_DISPLAY}</span></a>
        <a href="{WA}" target="_blank" rel="noopener" class="btn btn-outline"><span>WhatsApp Us</span></a>
      </div>
      <div class="trust-chips">{chips_html}</div>
    </div>
  </section>
'''

def fare_section(heading, rows, note):
    rows_html = ''.join(
        f'<div class="summary-row"><span class="s-lbl">{l}</span><span class="s-val">{v}</span></div>' for l, v in rows)
    return f'''
  <section class="section-pad">
    <div class="container">
      <span class="tag">Fares</span>
      <h2 class="body-heading" style="margin-top:0.8rem;">{heading}</h2>
      <div class="fare-table-wrap" style="margin-top:1.6rem;">{rows_html}</div>
      <p class="fare-note">{note}</p>
    </div>
  </section>
'''

def sample_cost(title, body):
    return f'''
      <div class="sample-cost">
        <div class="sc-title">{title}</div>
        <p>{body}</p>
      </div>
'''

def cards_section(tag, heading, cards):
    cards_html = ''.join(f'''
        <div class="why-card">
          <div class="why-num">— 0{i+1}</div>
          <h3 class="why-title">{t}</h3>
          <p class="why-desc">{d}</p>
        </div>''' for i, (t, d) in enumerate(cards))
    return f'''
  <section class="section-pad">
    <div class="container">
      <span class="tag">{tag}</span>
      <h2 class="body-heading" style="margin-top:0.8rem;">{heading}</h2>
      <div class="why-grid">{cards_html}</div>
    </div>
  </section>
'''

def faq_section(faqs):
    items = ''.join(f'''
          <div class="faq-item">
            <button class="faq-q" aria-expanded="false">
              {q}
              <span class="faq-arrow"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6" /></svg></span>
            </button>
            <div class="faq-a">{a}</div>
          </div>''' for q, a in faqs)
    return f'''
  <section>
    <div class="container section-pad">
      <div class="faq-layout">
        <div class="faq-left">
          <span class="tag">FAQ</span>
          <h2 class="display-heading" style="margin-top:0.8rem;">Got<br>Questions?</h2>
          <p class="faq-contact-note">
            Can't find your answer?<br>
            Call us at <a href="{TEL}">{PHONE_DISPLAY}</a><br>
            or <a href="{WA}" target="_blank" rel="noopener">WhatsApp us</a> anytime.
          </p>
        </div>
        <div class="faq-list">{items}</div>
      </div>
    </div>
  </section>
'''

CTA = f'''
  <section class="cta-band section-pad">
    <div class="container">
      <h2 class="body-heading">Ready to go?<br>Book in 2 minutes.</h2>
      <div class="page-hero-actions" style="justify-content:center;">
        <a href="{TEL}" class="btn btn-primary"><span>Call {PHONE_DISPLAY}</span></a>
        <a href="{WA}" target="_blank" rel="noopener" class="btn btn-outline"><span>WhatsApp</span></a>
        <a href="/#cabForm" class="btn btn-ghost"><span>Book via Form</span></a>
        <a href="/#estimator" class="btn btn-ghost"><span>Rate Estimator</span></a>
      </div>
    </div>
  </section>
'''

TRUST = ['★ 5.0 on Google (58 reviews)', '24/7 Available', 'Verified Local Drivers', 'No Hidden Charges']
FARE_NOTE_OUTSTATION = ('All outstation trips: minimum 300 km/day billing, driver batta per day as shown, tolls / parking / '
    'state taxes at actuals. AC rates shown; non-AC slightly lower. Use the <a href="/#estimator">rate estimator</a> '
    'for your exact trip or WhatsApp us for a fixed quote.')

PAGES = []

# ---------------- AIRPORT ----------------
PAGES.append({
    'path': 'services/airport-taxi-hubli/index.html',
    'title': 'Hubli Airport Taxi (HBX) | Fixed Rates, 24/7 | Trishika',
    'description': 'Hubli Airport taxi for pickup & drop — fixed transparent rates, flight tracking, 24/7. Dharwad to Hubli Airport cabs too. Call +91 82175 77849.',
    'canonical': f'{DOMAIN}/services/airport-taxi-hubli/',
    'body':
        hero('Airport Taxi', 'Hubli Airport<br>Taxi (HBX)',
             'On-time pickup and drop for every flight at Hubli Airport (Hubballi, HBX) on Gokul Road. '
             'We track your flight, the driver waits if it’s late, and the rate is agreed before you ride — '
             'no surge, no meter surprises. Serving Hubli city, Dharwad, and outstation connections 24/7. '
             'Our office is on Gokul Road, minutes from the terminal — the closest thing HBX has to an airport-based cab service.',
             ['Flight tracking', 'Driver waits free', '24/7 pickups', 'Clean AC cars'])
        + fare_section('Airport transfer rates',
            [('Sedan (Dzire / Etios) — city rate', '₹10–12 / km'),
             ('Ertiga (6–7 seater)', '₹14–16 / km'),
             ('Innova / Crysta (7 seater)', '₹17–20 / km'),
             ('Dharwad ⇄ Hubli Airport', 'Fixed quote on WhatsApp'),
             ('Outstation from the airport (Goa, Gokarna…)', 'Min 300 km/day + batta')],
            'Within Hubli-Dharwad, airport transfers are charged at the city per-km rate — share your pickup point on '
            '<a href="https://wa.me/918217577849" target="_blank" rel="noopener">WhatsApp</a> and we confirm a fixed fare in minutes. '
            'Early-morning and late-night flights: same rates, no night surcharge surprises — confirm while booking.')
        + cards_section('Why us for HBX', 'Airport runs are<br>our home ground', [
            ('We are ON Gokul Road', 'Hubli Airport sits on Gokul Road — so does our office. Short notice? We can usually still make your pickup.'),
            ('Flight-tracked pickups', 'Share your flight number. Delayed arrival? The driver adjusts — you don’t pay waiting games.'),
            ('Meet at Arrivals', 'Driver waits at the exit with your name. No hunting for autos with luggage.'),
            ('Dharwad connections', 'Regular airport runs to and from Dharwad — fixed quote, about 45 minutes door to door.'),
            ('Early flights, no stress', 'First flights out of HBX leave early. We do 4 AM pickups every week — on time, every time.'),
            ('Onward outstation', 'Landing at HBX and heading to Goa, Gokarna or Dandeli? Your cab is waiting at Arrivals.')])
        + faq_section([
            ('How do I book a Hubli airport taxi?',
             f'Call or WhatsApp {PHONE_DISPLAY} with your flight number and pickup point. We confirm the driver and a fixed fare before your trip.'),
            ('How far is Hubli Airport from the city centre?',
             'Hubli Airport (HBX) is on Gokul Road, roughly 8–10 km from central Hubli — about 20–25 minutes in normal traffic.'),
            ('Do you cover Dharwad to Hubli Airport?',
             'Yes, both directions, any flight time. It’s about a 45-minute drive; WhatsApp us for the fixed rate.'),
            ('What if my flight is delayed?',
             'We track the flight, not the clock. The driver adjusts to the actual arrival at no extra charge for normal delays.'),
            ('Can I book an outstation cab from the airport?',
             'Yes — many customers land at HBX and go straight to Goa, Gokarna, Hampi or Dandeli. Standard outstation billing applies (min 300 km/day + driver batta).')])
        + CTA,
})

# ---------------- TEMPO TRAVELLER ----------------
PAGES.append({
    'path': 'vehicles/tempo-traveller-hubli/index.html',
    'title': 'Tempo Traveller on Rent in Hubli | 12–17 Seater ₹19/km',
    'description': 'Tempo Traveller rent in Hubli from ₹19/km + batta. 12–17 seater AC for groups, weddings & tours. Mini bus 21–25 seats too. Call +91 82175 77849.',
    'canonical': f'{DOMAIN}/vehicles/tempo-traveller-hubli/',
    'body':
        hero('Group Vehicles', 'Tempo Traveller<br>on Rent in Hubli',
             'AC Tempo Traveller (12+1 seater) with an experienced driver for group trips from Hubli-Dharwad — '
             'weddings, corporate outings, temple tours and weekend getaways to Goa, Gokarna and Dandeli. '
             'Need more seats? Our Mini Bus takes 21–25 passengers. Transparent per-km pricing, no middlemen.',
             ['12+1 Seater AC', 'Mini Bus 21–25 seats', 'Experienced hill drivers', 'Outstation specialists'])
        + fare_section('Tempo Traveller rent per km in Hubli',
            [('Tempo Traveller (12+1) — AC', '₹19 / km'),
             ('Tempo Traveller — Non-AC', '₹17 / km'),
             ('Driver batta', '₹500 / day'),
             ('Mini Bus (21–25 seater) — AC', '₹28 / km'),
             ('Mini Bus driver batta', '₹600 / day'),
             ('Minimum billing (outstation)', '300 km / day')],
            FARE_NOTE_OUTSTATION + ' Looking for a Force Urbania or Cruiser? Call us — we’ll tell you honestly what’s available for your dates.')
        + sample_cost('Sample costing — weekend Goa group trip',
            '2 days, Tempo Traveller AC: 600 km (2 × 300 km min) × ₹19 = ₹11,400 + batta ₹1,000 = '
            '<strong>≈ ₹12,400</strong> + tolls at actuals. Split between 12 people, that’s about ₹1,035 a head — '
            'cheaper than most bus + local-taxi combinations, door to door.')
        + cards_section('Popular uses', 'One vehicle,<br>whole group together', [
            ('Weddings & functions', 'Guest pickups across Hubli-Dharwad, baraat movements, outstation guests from HBX airport.'),
            ('Temple & pilgrimage tours', 'Savadatti Yellamma, Mantralaya, Murudeshwar, Gokarna — day trips and multi-day yatras.'),
            ('Corporate & college trips', 'Offsites, industrial visits and study tours with one bill and one responsible driver.'),
            ('Weekend getaways', 'Goa, Dandeli rafting, Jog Falls — the group travels together, luggage and all.'),
            ('Airport groups', 'Flight-timed pickups at Hubli Airport for delegations and wedding parties.'),
            ('School & family outings', 'Clean, maintained vehicles with verified drivers who know every ghat road in North Karnataka.')])
        + faq_section([
            ('What is the Tempo Traveller rent per km in Hubli?',
             '₹19/km for AC and ₹17/km for non-AC, plus ₹500/day driver batta. Outstation trips bill a minimum of 300 km per day; tolls and parking at actuals.'),
            ('How many seats does the Tempo Traveller have?',
             '12+1 standard. For 13–25 passengers we run a Mini Bus at ₹28/km (AC).'),
            ('Can I book it for a one-day local function in Hubli?',
             'Tempo Traveller and Mini Bus are for outstation trips (min 300 km/day). For local functions within Hubli-Dharwad, call us — we’ll suggest the right combination of Ertigas/Innovas.'),
            ('Is the driver’s food and stay included?',
             'The ₹500/day batta covers the driver’s food and overnight expenses — you pay it with the bill, nothing separately.'),
            ('Do you have Force Urbania or Cruiser?',
             f'Availability varies by date. Call {PHONE_DISPLAY} and we’ll confirm honestly what we can arrange for your dates.')])
        + CTA,
})

# ---------------- ROUTE PAGE FACTORY ----------------
def route_page(slug, dest, km, hrs, via, title, desc, intro, chips, fare_rows, note, sample, cards, faqs):
    return {
        'path': f'routes/{slug}/index.html',
        'title': title, 'description': desc,
        'canonical': f'{DOMAIN}/routes/{slug}/',
        'body': hero(f'Hubli → {dest}', f'Hubli to {dest}<br>Taxi', intro, chips)
        + fare_section(f'Hubli to {dest} cab fare', fare_rows, note)
        + sample
        + cards_section('Route facts', f'The Hubli–{dest} run,<br>from drivers who do it weekly', cards)
        + faq_section(faqs) + CTA,
    }

PAGES.append(route_page(
    'hubli-to-goa-taxi', 'Goa', 160, '4–4.5', 'Dharwad → Alnavar → Anmod Ghat → Mollem → Ponda',
    'Hubli to Goa Taxi | 160 km Cab Fare & Route | Trishika',
    'Hubli to Goa taxi with driver — 160 km, ~4.5 hrs via Anmod Ghat. Round-trip fares from ₹7,800 (Sedan, 2 days). AC cabs, 24/7. Call +91 82175 77849.',
    'Door-to-door cab from Hubli to Goa — about 160 km to Panaji, 4 to 4.5 hours via Dharwad, Alnavar and the '
    'Anmod Ghat forest stretch. Beach hotels in North Goa (Calangute/Baga) add roughly 20–30 km. Your driver '
    'handles the ghat bends; you watch the Western Ghats roll by.',
    ['160 km · 4–4.5 hrs', 'Via Anmod Ghat', 'AC cars & Tempo', 'Hotel-door drop'],
    [('Sedan (Dzire/Etios) — AC', '₹12 / km'),
     ('Ertiga (6–7 seater) — AC', '₹16 / km'),
     ('Innova Crysta — AC', '₹20 / km'),
     ('Tempo Traveller (12+1) — AC', '₹19 / km'),
     ('Driver batta', '₹300–500 / day by vehicle'),
     ('Minimum billing', '300 km / day')],
    FARE_NOTE_OUTSTATION,
    sample_cost('Sample costing — weekend in Goa (2 days, Sedan AC)',
        '600 km billed (2 × 300 km min) × ₹12 = ₹7,200 + batta ₹600 = <strong>≈ ₹7,800</strong> '
        '+ tolls/parking at actuals. Innova Crysta for the family: ≈ ₹12,800. One-way drops available on request — WhatsApp for a quote.'),
    [('The route', 'NH-748 via Dharwad and Alnavar, over the Anmod Ghat into Mollem, then Ponda to Panaji. Scenic, forested, and winding on the ghat section.'),
     ('Best departure time', 'Leave Hubli by 6–7 AM: you clear the ghat before traffic builds and reach your hotel by lunch.'),
     ('Where in Goa?', 'Panaji ~160 km; Calangute/Baga ~185 km; Madgaon ~175 km. The fare is per actual km — tell us your hotel and we quote exactly.'),
     ('Monsoon note', 'June–September the ghat is misty and slow but spectacular. Add 30–45 minutes and let the driver set the pace.'),
     ('What’s included', 'Car + fuel + driver. Batta covers the driver’s food/stay. Tolls, parking and any Goa entry charges at actuals on the bill.'),
     ('Group option', 'Tempo Traveller (12+1) makes Goa about ₹1,000/head for a weekend — see the group vehicles page.')],
    [('How much does a taxi from Hubli to Goa cost?',
      'A 2-day round trip in a Sedan is about ₹7,800 all-in except tolls (600 km min billing + batta). Ertiga ≈ ₹10,300, Innova Crysta ≈ ₹12,800. One-way drops on request.'),
     ('How long does Hubli to Goa take by cab?',
      'About 4 to 4.5 hours to Panaji in normal conditions; add 30–45 minutes in monsoon or for North Goa beaches.'),
     ('Which route does the cab take?',
      'Via Dharwad → Alnavar → Anmod Ghat (NH-748) → Mollem → Ponda. It’s the shortest, most scenic road from Hubli.'),
     ('Can we stop on the way?',
      'Yes — Dudhsagar viewpoint turnoffs, spice farms near Ponda, chai stops on the ghat. Reasonable sightseeing stops are part of the trip.'),
     ('Is one-way Hubli to Goa drop available?',
      f'Yes, on request, subject to driver return logistics. WhatsApp {PHONE_DISPLAY} with your date for a one-way quote.')]))

PAGES.append(route_page(
    'hubli-to-bangalore-taxi', 'Bangalore', 420, '7', 'NH-48 via Davangere → Chitradurga → Tumakuru',
    'Hubli to Bangalore Cab | 420 km One-Way & Round Trip',
    'Hubli to Bangalore taxi — 420 km, ~7 hrs on NH-48. One-way Sedan ≈ ₹5,340 + tolls. Doorstep pickup, AC cars, 24/7. Call +91 82175 77849.',
    'Comfortable AC cab from Hubli to Bengaluru — about 420 km, 6.5 to 7.5 hours on the four-lane NH-48 through '
    'Davangere, Chitradurga and Tumakuru. Door-to-door with luggage, no station queues, no transfer headaches. '
    'Popular for medical visits, airport connections and family relocations.',
    ['420 km · ~7 hrs', 'NH-48 four-lane', 'One-way available', 'Doorstep to doorstep'],
    [('Sedan (Dzire/Etios) — AC', '₹12 / km'),
     ('Ertiga (6–7 seater) — AC', '₹16 / km'),
     ('Innova Crysta — AC', '₹20 / km'),
     ('Driver batta', '₹300–400 / day by vehicle'),
     ('Minimum billing', '300 km / day')],
    FARE_NOTE_OUTSTATION,
    sample_cost('Sample costing — one-way drop (Sedan AC)',
        '420 km × ₹12 = ₹5,040 + batta ₹300 = <strong>≈ ₹5,340</strong> + tolls at actuals '
        '(NH-48 has several plazas — budget ₹600–800). Round trip over 2 days ≈ ₹10,680 + tolls.'),
    [('The route', 'NH-48 all the way: Hubli → Ranebennur → Davangere → Chitradurga → Tumakuru → Bengaluru. Four-lane, divided, well-lit.'),
     ('Best departure time', 'Leave by 5–6 AM to cross Tumakuru before Bengaluru’s morning peak; evening departures hit city traffic at entry.'),
     ('Tolls', 'Multiple plazas on NH-48, charged at actuals with receipts on the final bill.'),
     ('Where in Bengaluru?', 'Whitefield or Electronic City add 20–40 km across the city — per-km billing means you only pay what you ride.'),
     ('Airport connection', 'Kempegowda Airport (BLR) is on the far side — tell us your flight time and we plan the departure with buffer.'),
     ('Overnight halts', 'Prefer a break? Davangere and Chitradurga have good highway hotels — your call, driver adjusts.')],
    [('How much is a cab from Hubli to Bangalore?',
      'One-way Sedan drop ≈ ₹5,340 plus tolls. Ertiga ≈ ₹7,020, Innova Crysta ≈ ₹8,700. Round trips bill 300 km minimum per day.'),
     ('How long is the drive?',
      '6.5–7.5 hours for the 420 km depending on breaks and Bengaluru entry traffic.'),
     ('Is it cheaper than the train?',
      'For one person, no. For a family of four with luggage needing door-to-door — comparable, and you keep your own schedule.'),
     ('Do you do Bangalore to Hubli return pickups?',
      'Yes, both directions, including BLR airport pickups timed to your flight.'),
     ('Night driving?',
      'NH-48 is safe and lit, and our highway drivers do this run weekly. Overnight trips carry the standard batta.')]))

PAGES.append(route_page(
    'hubli-to-dandeli-taxi', 'Dandeli', 75, '2', 'Kalghatgi → Haliyal',
    'Hubli to Dandeli Cab | 75 km Taxi, Day Trips & Groups',
    'Hubli to Dandeli taxi — 75 km, ~2 hrs via Kalghatgi. Day-trip cab ≈ ₹3,900 (Sedan). Rafting groups by Tempo Traveller. 24/7. Call +91 82175 77849.',
    'Quick 75-km hop from Hubli to Dandeli — about 2 hours through Kalghatgi and Haliyal into the Kali river '
    'forests. White-water rafting, jungle stays and safaris; we drop you at the resort or the rafting point '
    'and wait if it’s a day trip.',
    ['75 km · 2 hrs', 'Day trips ideal', 'Rafting groups', 'Forest-road drivers'],
    [('Sedan (Dzire/Etios) — AC', '₹12 / km'),
     ('Ertiga (6–7 seater) — AC', '₹16 / km'),
     ('Tempo Traveller (12+1) — AC', '₹19 / km'),
     ('Driver batta', '₹300–500 / day by vehicle'),
     ('Minimum billing', '300 km / day')],
    FARE_NOTE_OUTSTATION,
    sample_cost('Sample costing — Dandeli day trip (Sedan AC)',
        'Round trip ≈150 km driven, billed at the 300 km/day minimum: 300 × ₹12 = ₹3,600 + batta ₹300 = '
        '<strong>≈ ₹3,900</strong>. Rafting group of 12 by Tempo Traveller ≈ ₹6,200 — about ₹520 a head, '
        'and the cab waits through your rafting slot.'),
    [('The route', 'Hubli → Kalghatgi → Haliyal → Dandeli. Smooth state highway, forest canopy for the last stretch. Almost no tolls.'),
     ('Day trip friendly', 'Leave 7 AM, raft by 10, jungle lunch, back in Hubli for dinner. The cab stays with you all day.'),
     ('Rafting timing', 'Rafting slots run on river-release timings — morning slots are safest. We time the pickup so you never miss one.'),
     ('Wildlife extras', 'Add Syntheri Rocks or a Kali river coracle ride — 20–30 km extra, billed per km, worth it.'),
     ('Group logistics', 'One Tempo Traveller beats a convoy of cars on forest roads — everyone arrives together, on time.'),
     ('Stay overnight?', 'Multi-day trips bill 300 km/day minimum with the driver staying at your resort’s driver quarters (batta covers it).')],
    [('How much is a taxi from Hubli to Dandeli?',
      'A full day trip is about ₹3,900 by Sedan (300 km minimum billing + batta). Groups: Tempo Traveller ≈ ₹6,200 for the day.'),
     ('How long does it take?',
      'About 2 hours for the 75 km — forest roads, so mornings are quickest.'),
     ('Will the cab wait during rafting?',
      'Yes. Day-trip bookings include the driver waiting at the rafting point or resort.'),
     ('Best season for Dandeli?',
      'October to May for rafting (dam-release dependent); monsoon is lush but some activities close.'),
     ('Can you pick up from Dharwad?',
      'Of course — Dharwad is on the way. Same billing, pickup from your doorstep.')]))

PAGES.append(route_page(
    'hubli-to-gokarna-taxi', 'Gokarna', 150, '3.5', 'Yellapur → Ankola → NH-66',
    'Hubli to Gokarna Cab | 150 km Taxi Fare & Timings',
    'Hubli to Gokarna taxi — 150 km, ~3.5 hrs via Yellapur & Ankola. Temple + beach day trip ≈ ₹3,900 (Sedan). AC cabs 24/7. Call +91 82175 77849.',
    'Cab from Hubli to Gokarna — about 150 km, 3.5 hours via Yellapur’s forest ghats down to Ankola and the '
    'coastal NH-66. Mahabaleshwar Temple darshan, Om Beach sunsets, or both in one well-planned day. '
    'We handle the ghat driving; you handle the beach.',
    ['150 km · 3.5 hrs', 'Temple + beaches', 'Day trips possible', 'Ghat-experienced drivers'],
    [('Sedan (Dzire/Etios) — AC', '₹12 / km'),
     ('Ertiga (6–7 seater) — AC', '₹16 / km'),
     ('Innova Crysta — AC', '₹20 / km'),
     ('Tempo Traveller (12+1) — AC', '₹19 / km'),
     ('Minimum billing', '300 km / day')],
    FARE_NOTE_OUTSTATION,
    sample_cost('Sample costing — Gokarna day trip (Sedan AC)',
        'Round trip ≈300 km — right at the daily minimum: 300 × ₹12 = ₹3,600 + batta ₹300 = '
        '<strong>≈ ₹3,900</strong> + parking at actuals. Add Murudeshwar (+110 km round) for a temple-coast '
        'double — billed per km beyond the minimum.'),
    [('The route', 'Hubli → Yellapur → Ankola → NH-66 south to Gokarna. Forest ghats till Ankola, then the coast road.'),
     ('Best departure time', 'Out by 6 AM: temple darshan before the queue, beach by afternoon, sunset at Om Beach, home by night.'),
     ('Temple etiquette', 'Mahabaleshwar Temple has a dress code (traditional preferred). The driver drops you at the temple street — vehicles stop short of the inner lanes.'),
     ('The beaches', 'Om, Kudle, Half Moon and Paradise. Om Beach has road access + parking; Half Moon and Paradise are boat/trek only.'),
     ('Combine with Murudeshwar', 'Another ~55 km south — the giant Shiva statue plus Gokarna in one long, brilliant day. Tell us in advance and we plan the timing.'),
     ('Overnight option', 'Beach stays are cheap on weekdays. Two-day trips bill the 300 km/day minimum with the driver on batta.')],
    [('How much is a cab from Hubli to Gokarna?',
      'A day trip runs about ₹3,900 by Sedan (300 km minimum + batta). Family Innova ≈ ₹6,400. Parking at actuals.'),
     ('How long is the drive?',
      'About 3.5 hours each way — ghat section till Ankola, then quick coastal road.'),
     ('Can we do Gokarna and Murudeshwar in one day?',
      'Yes, with a 6 AM start — roughly 410 km total, billed per km beyond the 300 km minimum. Long day, very doable.'),
     ('Is the ghat road safe?',
      'Yes — it’s a regular route for our drivers. Monsoon adds mist and time; we drive to conditions.'),
     ('Where does the cab park at the beach?',
      'Om Beach and the temple area have parking; the driver stays with the vehicle — call when you’re ready to move.')]))

PAGES.append(route_page(
    'hubli-to-belgaum-taxi', 'Belgaum', 100, '2', 'NH-48 via Kittur',
    'Hubli to Belgaum Taxi | 100 km Cab Service 24/7',
    'Hubli to Belgaum (Belagavi) taxi — ~100 km, 2 hrs on NH-48 via Kittur. Business, medical & airport runs, 24/7. Call +91 82175 77849.',
    'Direct cab from Hubli to Belgaum (Belagavi) — about 100 km, 2 hours on NH-48 through Kittur. Business '
    'meetings, KLE hospital visits, Belagavi airport (IXG) connections and family functions — both directions, '
    'any hour.',
    ['~100 km · 2 hrs', 'NH-48 via Kittur', 'Medical & business runs', 'IXG airport drops'],
    [('Sedan (Dzire/Etios) — AC', '₹12 / km'),
     ('Ertiga (6–7 seater) — AC', '₹16 / km'),
     ('Innova Crysta — AC', '₹20 / km'),
     ('Driver batta (full-day trips)', '₹300–400 / day'),
     ('Minimum billing (outstation)', '300 km / day')],
    FARE_NOTE_OUTSTATION,
    sample_cost('Sample costing — Belgaum same-day return (Sedan AC)',
        'Round trip ≈200 km driven, billed at the 300 km/day outstation minimum: 300 × ₹12 = ₹3,600 + '
        'batta ₹300 = <strong>≈ ₹3,900</strong> + NH-48 tolls at actuals. The cab stays with you in '
        'Belgaum through your work.'),
    [('The route', 'NH-48 north through Kittur (stop at Kittur Rani Chennamma’s fort if you’re early) into Belagavi. Four-lane most of the way.'),
     ('Medical trips', 'KLE Hospital and Belagavi’s specialists draw patients from Hubli weekly — the cab waits through appointments.'),
     ('Airport runs', 'Belagavi Airport (IXG, Sambra) has metro connections HBX doesn’t — we do flight-timed drops both ways.'),
     ('Business day', 'Morning meeting, cab on standby, back by evening — one fixed day rate, no auto-hunting in a new city.'),
     ('Both directions', 'Belgaum to Hubli pickups too — same rates, local driver knowledge on both ends.'),
     ('Onward to Goa', 'Belgaum sits on the Goa road — combine a Belgaum stop with a Goa trip and we bill the actual route.')],
    [('How much is a taxi from Hubli to Belgaum?',
      'Same-day return ≈ ₹3,900 by Sedan (300 km outstation minimum + batta) plus tolls. One-way drops on request — WhatsApp for a quote.'),
     ('How long does Hubli to Belgaum take?',
      'About 2 hours for the ~100 km on NH-48, a little more in Belagavi city traffic.'),
     ('Will the cab wait during my hospital appointment?',
      'Yes — full-day bookings include the driver staying with you; that’s the point of the day rate.'),
     ('Do you drop at Belagavi airport (IXG)?',
      'Yes, flight-timed, both directions. Share the flight number when booking.'),
     ('Belgaum or Belagavi?',
      'Same city — official name Belagavi. Our drivers answer to both.')]))

# ---------------- OUTSTATION HUB ----------------
PAGES.append({
    'path': 'services/outstation-cabs-hubli/index.html',
    'title': 'Outstation Cabs in Hubli | Goa, Bangalore, Gokarna & More',
    'description': 'Outstation taxi from Hubli — Goa, Bangalore, Gokarna, Dandeli, Belgaum & beyond. From ₹10/km + batta, AC cars & Tempo. Call +91 82175 77849.',
    'canonical': f'{DOMAIN}/services/outstation-cabs-hubli/',
    'body':
        hero('Outstation Cabs', 'Outstation Taxi<br>from Hubli',
             'Round trips and one-way drops from Hubli-Dharwad to anywhere in Karnataka, Goa and Maharashtra — '
             'with a driver who does these highways every week. Transparent per-km rates, driver batta stated '
             'upfront, tolls at actuals with receipts. No surge, no renegotiation at the drop point.',
             ['Any destination', 'One-way on request', 'AC fleet + Tempo', 'Transparent billing'])
        + fare_section('Outstation rates from Hubli',
            [('Sedan (Dzire / Etios) — AC', '₹10–12 / km'),
             ('Ertiga (6–7 seater) — AC', '₹14–16 / km'),
             ('Innova / Crysta — AC', '₹17–20 / km'),
             ('Tempo Traveller (12+1) — AC', '₹19 / km'),
             ('Mini Bus (21–25) — AC', '₹28 / km'),
             ('Driver batta', '₹300–600 / day by vehicle'),
             ('Minimum billing', '300 km / day')],
            FARE_NOTE_OUTSTATION)
        + cards_section('Popular routes', 'Where Hubli<br>actually travels', [
            ('Goa — 160 km', 'Weekend classic over the Anmod Ghat. Sedan round trip ≈ ₹7,800 for 2 days. <a href="/routes/hubli-to-goa-taxi/" class="route-link">Fares & details →</a>'),
            ('Bangalore — 420 km', 'NH-48 door-to-door. One-way Sedan ≈ ₹5,340 + tolls. <a href="/routes/hubli-to-bangalore-taxi/" class="route-link">Fares & details →</a>'),
            ('Gokarna — 150 km', 'Temple + Om Beach in a day. ≈ ₹3,900 Sedan day trip. <a href="/routes/hubli-to-gokarna-taxi/" class="route-link">Fares & details →</a>'),
            ('Dandeli — 75 km', 'Rafting day trips, resort drops. ≈ ₹3,900 Sedan. <a href="/routes/hubli-to-dandeli-taxi/" class="route-link">Fares & details →</a>'),
            ('Belgaum — 100 km', 'Business, KLE hospital, IXG airport. <a href="/routes/hubli-to-belgaum-taxi/" class="route-link">Fares & details →</a>'),
            ('Hampi, Murudeshwar, Jog Falls…', 'Any route in the region — Hampi 165 km, Murudeshwar 205 km, Jog 170 km. Call for a fixed quote on your dates.')])
        + faq_section([
            ('How does outstation billing work?',
             'Per-km rate × km driven (minimum 300 km/day) + driver batta per day + tolls/parking at actuals. The estimator on our homepage shows your number before you book.'),
            ('Do you do one-way drops?',
             f'Yes, on request, subject to return logistics — WhatsApp {PHONE_DISPLAY} with the date and destination for a one-way quote.'),
            ('Can I keep the cab for multiple days?',
             'Yes — multi-day tours are our specialty. Each day bills the 300 km minimum; the driver stays on batta.'),
            ('Are tolls included?',
             'Tolls, parking and state entry fees are at actuals, with receipts, added to the final bill. The per-km rate never changes mid-trip.'),
            ('Which vehicle should I pick?',
             'Couples: Sedan. Family of 5–6: Ertiga. Comfort for 6–7: Innova Crysta. Groups of 8+: Tempo Traveller or Mini Bus — see the group vehicles page.')])
        + CTA,
})

# ---------------- FARE PAGE ----------------
PAGES.append({
    'path': 'fare/hubli-taxi-fare/index.html',
    'title': 'Hubli Taxi Fare & Car Rental Rates | ₹10/km Rate Card',
    'description': 'Hubli taxi rate card — car rental from ₹10/km, Ertiga ₹14, Innova ₹17, Tempo ₹19. Local 8hr/80km packages & outstation rules. Call +91 82175 77849.',
    'canonical': f'{DOMAIN}/fare/hubli-taxi-fare/',
    'body':
        hero('Rate Card', 'Hubli Taxi Fares<br>&amp; Rental Rates',
             'The complete Trishika rate card — the same numbers our drivers bill by. Per-km rates, driver batta, '
             'local packages and the outstation rules, all on one page. If a rate isn’t here, it doesn’t exist: '
             'no surge, no hidden charges, no drop-point renegotiation.',
             ['Published rates', 'No surge pricing', 'Tolls at actuals', 'Same rates 24/7'])
        + fare_section('Outstation — per km (AC)',
            [('Sedan (Swift Dzire / Toyota Etios), 4+1', '₹12 / km · batta ₹300'),
             ('Maruti Ertiga, 6–7+1', '₹16 / km · batta ₹350'),
             ('Toyota Innova, 7+1', '₹18 / km · batta ₹400'),
             ('Innova Crysta, 7+1', '₹20 / km · batta ₹400'),
             ('Tempo Traveller, 12–17+1', '₹19 / km · batta ₹500'),
             ('Mini Bus, 21–25+1', '₹28 / km · batta ₹600')],
            'Minimum 300 km billed per day on outstation trips. Non-AC rates are ₹1–3/km lower by vehicle. '
            'Tolls, parking and state taxes at actuals with receipts.')
        + fare_section('Local Hubli-Dharwad — 8 hr / 80 km package',
            [('Sedan — package base', '80 km × ₹12 = ₹960'),
             ('Ertiga — package base', '80 km × ₹16 = ₹1,280'),
             ('Innova / Crysta — package base', '80 km × ₹18–20 = ₹1,440–1,600'),
             ('Extra hours beyond 8', '₹100 / hour'),
             ('Extra km beyond 80', 'at the vehicle’s per-km rate')],
            'Local packages suit weddings, shopping days and city errands. Tempo Traveller and Mini Bus are '
            'outstation-only. For airport transfers see the <a href="/services/airport-taxi-hubli/">airport taxi page</a>.')
        + sample_cost('Work out your own trip in 30 seconds',
            'Outstation: km (min 300/day) × rate + batta × days + tolls. Local: package base + extras. '
            'Or skip the math — the <a href="/#estimator"><strong>rate estimator</strong></a> does it live, '
            'and sends the estimate straight to WhatsApp.')
        + faq_section([
            ('What is the taxi rate per km in Hubli?',
             'Sedans start at ₹10–12/km, Ertiga ₹14–16, Innova ₹17–20, Tempo Traveller ₹19, Mini Bus ₹28 — AC rates, driver included.'),
            ('Is there a minimum charge?',
             'Outstation trips bill a minimum of 300 km per day. Local runs use the 8hr/80km package as the base.'),
            ('What is driver batta?',
             'A fixed daily amount (₹300–600 by vehicle) covering the driver’s meals and overnight stay on outstation trips. It’s on the rate card, never a surprise.'),
            ('Are night trips costlier?',
             'The per-km rate stays the same 24/7. Confirm timing when booking so we assign a rested driver.'),
            ('Why do aggregator apps show cheaper base fares?',
             'App base fares exclude surge, waiting and drop-point extras. Our rate is the whole rate — compare final bills, not first screens.')])
        + CTA,
})

# ---------------- write ----------------
for p in PAGES:
    full = os.path.join(SO, p['path'].replace('/', os.sep))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    html = HEAD.format(title=p['title'], description=p['description'], canonical=p['canonical'],
                       domain=DOMAIN, tel=TEL, wa=WA, phone=PHONE_DISPLAY) + p['body'] + FOOTER.format(tel=TEL, wa=WA, phone=PHONE_DISPLAY)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"{p['path']:48s} {len(html)//1024} KB  title:{len(p['title'])}ch desc:{len(p['description'])}ch")
print(f'\n{len(PAGES)} pages written.')
