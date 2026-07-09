# Phase 0 — Recon & Baseline

**Project:** Trishika Car Rental — Organic + Paid Growth Engine
**Date:** 2026-07-08
**Site:** https://trishikacarrentalhubli.in/
**Data window:** 6 August 2025 – 8 July 2026 (11 months, not 12 — noted)

---

## 1. Business facts (confirmed)

| Field | Value | Source |
|---|---|---|
| Business name (GBP, public) | Trishika Car Rental | Google Maps listing |
| GBP rating / reviews | **5.0 ★ / 58 reviews** | Google Maps listing |
| GBP primary category | **Car rental agency** | Google Maps listing |
| Hours | Open 24 hours | GBP |
| Address | Shop No 37, Yashasvi Apt, Gokul Rd, Gandhi Nagar, Hubballi, Karnataka 580030 | GBP = site footer = schema ✔ NAP consistent |
| Phone | +91 82175 77849 (GBP shows 082175 77849 — same number, format differs) | GBP / site |
| Services | With-driver rental, outstation routes, airport transfers. **No self-drive.** | Sayed |
| Ads budget forward | ₹10k–25k/month | Sayed |
| Conversion tracking | **Never deliberately configured — conversion data untrusted (P0)** | Sayed |
| GTM | **GTM-P92G7GNP installed** on the site | index.html |
| Socials | Instagram + Facebook linked in schema | index.html |

### Published fares (from live site — verify current)
| Vehicle | Rate/km | Driver batta | Notes |
|---|---|---|---|
| Sedan (Etios/Dzire) | ₹10–12 | ₹300/day | |
| Ertiga | ₹14–16 | ₹350/day | |
| Innova / Crysta | ₹17–20 | ₹400/day | |
| Tempo Traveller (12+1) | ₹19 | ₹500/day | Outstation only |
| Mini Bus (21–25) | ₹28 | ₹600/day | Outstation only |

Min 300 km/day outstation; local package 8 hrs/80 km; tolls/parking extra.

### Routes already promoted on site (with distances)
Gokarna 150 km · Goa 160 km · Dandeli 75 km · Murudeshwar 205 km · Hampi 165 km · Sirsi 105 km · Shimoga/Jog 170 km · Bengaluru 420 km · Davangere 150 km

---

## 2. Page inventory

The site is a **single-page static site**. There are no service, route, vehicle, or area pages — the entire Phase 3 architecture is greenfield.

| Property | Value | Assessment |
|---|---|---|
| URL | `/` (only indexable page; 404.html, robots.txt, sitemap.xml with 1 URL) | — |
| Title | "Taxi Service in Hubli \| Trishika Car Rental – 24/7 Cab Booking" | 62 chars, slightly long; targets taxi term |
| Meta description | Present, ~155 chars, includes phone + differentiators | OK |
| H1 | "Reliable Taxi Service Hubli" | OK, single H1 |
| Word count | 1,447 | Healthy for a home page |
| Schema | LocalBusiness+TaxiService (full NAP, geo, 24/7, sameAs) + FAQPage (5 Qs) | Good foundation; no BreadcrumbList (single page, N/A yet) |
| Click-to-call | Header, hero, floating button, footer — all `tel:` | ✔ above the fold |
| WhatsApp | wa.me links throughout; booking form submits to WhatsApp | ✔ |
| Trust signals | "24/7", "6+ vehicles", "₹10/km", verified drivers | No review count/years-in-business yet |
| Images | 29 `<img>` tags, all have alt (gallery alts generic "Trishika Fleet Vehicle"), **all 29 missing width/height** (CLS risk) | P1 |
| Kannada content | None | hreflang N/A |

### Page weight (P0 for mobile 4G)
| Asset | Size | Issue |
|---|---|---|
| `images/hero-bg.png` | **2.5 MB** | Desktop hero background = likely LCP element, PNG |
| `images/hero-mobile.mp4` | **4.9 MB** | Autoplay video on mobile hero |
| `images/hero_bg.png` | 2.5 MB | Apparent duplicate of hero-bg.png; not referenced in HTML/CSS found — dead weight in repo |
| `assets/og-image.jpg` | 2.5 MB | OG image (not render-blocking, but absurd for a social card) |
| Fleet PNGs (sedan/ertiga/innova/tempo/minibus) | 454–490 KB each | All > 200 KB threshold |
| `Fleet Gallery/…34.58.jpeg` | 1.33 MB | Largest gallery image |
| GSAP + ScrollTrigger CDN, Google Fonts (7 weights Poppins + 5 Inter) | external | Render-blocking / heavy font payload |

Also: footer "Popular Routes" links (Hubli to Goa Cab, etc.) all point to `#cabForm` — keyword anchor text pointing at a form fragment, no destination pages. Preloader + custom cursor add JS work on low-end mobiles.

---

## 3. Search terms report profile

**File:** original UTF-16 export → canonical UTF-8 at `data/search_terms_12mo.csv` (1,340 term rows); totals rows split to `data/search_terms_totals.csv`. Verified: re-parse matches report totals exactly.

**Columns present:** Search term, Match type, Added/Excluded, Campaign, Ad group, Clicks, Impr., CTR, Currency (INR), Avg. CPC, Cost, Campaign type, Conv. rate, Conversions, Cost/conv.
**Not present:** conversion value, date segmentation, device, match-triggering keyword. All rows Campaign type = Search.

### Account totals (from report's own total rows)
| Scope | Clicks | Cost | Conversions |
|---|---|---|---|
| Visible search terms (the 1,340 rows) | 1,414 | ₹27,713 | 44.0 |
| "Other search terms" (hidden by Google) | 1,465 | ₹30,415 | 23.0 |
| **Total: Account / Search** | **4,365** | **₹92,481** | **67.0** |

Three structural findings:
1. **52% of search-terms spend (₹30.4k) is invisible** — Google's "Other search terms" bucket. Driven by broad match + PMax-style matching. We can't mine what we can't see; tightening match types shrinks this bucket.
2. **₹34.4k of account spend (37%) isn't in the search-terms report at all** (92.5k − 27.7k − 30.4k). Needs the campaign-level view to explain (paused campaigns' other channels, Display expansion, etc.). Pending Ads dashboard access.
3. **Conversion column is untrusted** — tracking was never deliberately set up (Sayed). Every CPA/CVR judgement in Phase 1 must carry this caveat, and fixing measurement is the first executable win.

### Per-campaign breakdown (visible terms only)
| Campaign | Terms | Clicks | Cost | Conv | Read |
|---|---|---|---|---|---|
| LEADS 11/04 | 214 | 617 | ₹13,109 | 15.0 | Biggest spender |
| 03/22/2026 New Campaign | 176 | 374 | ₹6,238 | 12.0 | Best conv density |
| New Campaign 05/03 | 231 | 244 | ₹5,573 | 17.0 | Has themed ad groups ("Car Rental With Driver", "Taxi Service") |
| Campaign #1 | 719 | 179 | ₹2,793 | 0.0 | **54% of all terms, zero conversions** — broad-match junk collector (ola/uber/rapido/job/app queries) |

Naming is date-based, ad groups almost all "Ad group 1". Structure rebuild (Phase 6) fully justified.

### Match type (visible terms)
Exact + close variants carry the money: ₹23.6k of ₹27.7k. Broad match: 504 terms, only ₹1,358 — cheap junk but it pollutes data and feeds the hidden bucket.

### Early signal — what converts (preview, full mining in Phase 1)
"car rental in hubli" and close variants dominate conversions (5 + 3 + 2.65 + 2 + 2 …), followed by "taxi service in hubli" (4 + 1), airport terms, and single-conversion route terms (hubli to bangalore/belgaum). **The business converts on "car rental" language at least as much as "taxi" language** — the site's title tag leads with "Taxi Service in Hubli". To quantify properly in Phase 1.

---

## 4. Live SERP & map-pack baseline (checked from Hubballi location, 2026-07-08)

### "taxi service in hubli"
- **Map pack:** Balaji cab (5.0★/335), SAI CABS (5.0★/203), Queens Car Rental (4.7★/611) + sponsored pack slot: Nikhil Travels (4.8★/258). All primary-categoried "Taxi service", 5–15+ years in business. **Trishika absent.**
- **Organic p.1:** MakeMyTrip, Uber, Justdial, Goibibo, Savaari (aggregators) + locals: Suman Cabs, queenscarrental.com (also running search ads), hublicabs.com, AK Tour. **Trishika absent** (consistent with "page 2" brief).

### "car rental in hubli" (the top-converting term)
- **Map pack:** Raahiz Travels (4.9★/486), Hubli self drive (4.1★/141), Queens Car Rental (4.7★/611). **Trishika absent — even in its own primary category.**
- **Organic p.1:** Swadeshi Car Rentals, Justdial, Savaari, Raahiz Travels (site + Instagram), self-drive players, TransRentals. **Trishika absent.**

### The blunt read
Trishika has a perfect 5.0 rating but **58 reviews vs 141–611 for every pack occupant**. Review count/velocity — not website work — is the primary map-pack bottleneck (per brief §Phase 5 honesty clause, stated now rather than later). Second factor: primary category "Car rental agency" while every "taxi service in hubli" pack occupant is "Taxi service" — category decision needed in Phase 5 (which query family do we want the pack for? The conversion data will answer this in Phase 1).

Also observed: **Queens Car Rental sits in BOTH packs** (611 reviews) and runs paid ads — that's the local benchmark competitor to model.

---

## 5. Live dashboard baseline (via trishikacarrentalhubli@gmail.com, 2026-07-08)

### Google Ads — account 983-550-8200 "Trishika Car Rental Hubli"
(A second account 497-218-8611 exists under the same login: **0 clicks, ₹0 lifetime — dormant**, ignore.)

| Campaign | Budget | Status | Clicks | Cost (Aug 6 25 – Jun 10 26) |
|---|---|---|---|---|
| Campaign #1 | ₹500/day | **Paused** | 2,045 | ₹46,942 |
| LEADS 11/04 | ₹500/day | Active — "Bid strategy learning" | 1,321 | ₹26,058 |
| New Campaign 05/03 | ₹917.74/day | **Paused** | 422 | ₹9,155 |
| 03/22/2026 New Campaign | ₹700/day | Active — "Bid setting limited", opt score 82% | 370 | ₹6,327 |

- Active daily budget **₹1,200/day ≈ ₹36k/month — above the stated ₹10–25k budget.**
- The ₹34k "unexplained" spend from the CSV is now explained: it's Campaign #1's broad-match spend whose search terms Google hid. All spend is Search; no other channels.
- **⚠ Account balance is getting low** (prepaid billing). When it hits zero, all ads stop. Top-up decision needed.
- Live RSA example: "Hubli Airport Taxi 24/7 – Safe & Clean Cabs Hubli – Trishika Car Rental" → ad strength "Good"; account has **no sitelinks, no callouts, no images** (per Google's own recommendations panel).

### Conversion actions (the P0, now with receipts)
| Action | Source | Status | Counting | Conversions |
|---|---|---|---|---|
| **V2_Auto_Success_Test** | Website | Needs attention | **Every**, 30-day window | 62.02 — this is what the account calls "conversions" |
| Submit lead form | Website | **Inactive** | One, 90-day | **0.00 ever** |
| Page views / Store visits (auto goals) | — | — | — | 28 / 28 (not primary) |

The entire ₹92k of history — and LEADS 11/04's *currently learning* bid strategy — optimizes toward a leftover **test event**. No call tracking, no WhatsApp tracking, no working form tracking. Fixing this is executable win #1.

### Search Console
Property `https://trishikacarrentalhubli.in/` exists under this login but is **Not verified** → no organic query data available. Fix: add the verification meta tag to index.html (or DNS record) and verify — Claude can do the tag once deploy access exists.

### GBP (manager access confirmed)
- Name field: **"Trishika Car Rental"** — clean ✔ (old stuffed name survives only in third-party echoes, e.g. a WorkIndia job post)
- Verified ✔ · 5.0★ / 58 reviews · **3 unread reviews**
- **Categories: primary "Car rental company" — and NOT A SINGLE secondary category.** Not even "Taxi service". Easiest high-leverage GBP fix available.
- Description claims **"self-drive and chauffeur-driven options"** — self-drive is false; must be rewritten (Phase 5).
- Performance: 862 monthly views, 468 customer interactions; **photos last added 110 days ago**; profile strength "incomplete".
- No products configured; services state not yet audited (Phase 5).

### Citations & brand ecosystem (found in passing)
- **JustDial listing exists with 4.9★ / ~131 reviews — under phone +91-98452 06189**, not the site/GBP number 82175 77849. **NAP mismatch = P0 per Phase 4.** (Which number is the real business line?)
- Facebook page + Instagram exist. **Instagram is posting "Self-drive & rental options … Contact Madhu Car Rentals … 7019618668"** — a different brand name, a third phone number, and a service Trishika doesn't offer, on Trishika's own handle.
- DreamWeddingHub lists them for wedding car rental (untapped service angle).
- Brand-confusion note: trishikatravels.in is an unrelated Hyderabad company ranking for "Trishika" queries.

## 6. Data-quality flags

- **P0:** conversions = a test tag counting every fire; treat all CPA/CVR as directional only until tracking is rebuilt.
- Report window is 11 months, not 12.
- GSC unverified → zero organic visibility data for now.

---

**Phase 0 complete. Stopped, per ground rules. Phase 1 (search-term mining) needs nothing further from anyone — say go.**
