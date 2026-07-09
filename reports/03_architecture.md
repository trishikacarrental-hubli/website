# Phase 3 — Information Architecture (proposal for approval)

Every page below is justified by rows in [`keyword_master.csv`](../data/keyword_master.csv) (cluster totals cited). Pages the brief's skeleton suggests but the data does **not** support are listed at the end with reasons — per ground rule: data-gated, no thin template pages.

## Target architecture

```
/                                    (exists — re-titled, see meta rewrites)
/services/airport-taxi-hubli/        P0  · airport cluster: 219 impr, 12 clicks, 3.01 conv @ 25% CVR
/vehicles/tempo-traveller-hubli/     P0  · tempo 171 impr + urbania 22 (0.5 conv) + cruiser 18 — one group-vehicles page
/routes/hubli-to-goa-taxi/           P1  · 105 impr, 11 clicks — heavy price intent → fare table front-and-centre
/routes/hubli-to-bangalore-taxi/     P1  · 39 impr, 1 conv
/routes/hubli-to-dandeli-taxi/       P1  · 33 impr, 5 clicks
/routes/hubli-to-gokarna-taxi/       P1  · 29 impr — ads never matched these (2 clicks); SERP gap
/routes/hubli-to-belgaum-taxi/       P2  · 8 impr but 1 click → 1 conv; cheap to add with the same template
/services/outstation-cabs-hubli/     P2  · thin query data (5 terms, ₹45) — included as the ROUTES HUB:
                                           parent for internal linking, targets "outstation cabs/taxi hubli"
/fare/hubli-taxi-fare/               P2  · "car rental hubli price" 50 impr + "taxi rates in hubli" 21 + "car rent per km in hubli" 18
```

9 new pages total: 2 × P0, 4 × P1, 3 × P2. Recommended build order: P0 pair → Goa → Bangalore/Dandeli/Gokarna → P2 trio.

## Primary keyword per page — cannibalization matrix

| Page | Primary cluster (exclusive) | Secondary/supporting | Explicitly does NOT target |
|---|---|---|---|
| `/` | car rental in hubli · taxi service in hubli (core-local) | cab booking hubli, travels in hubli, Hubballi variants | airport, routes, vehicles, fares-generic |
| `/services/airport-taxi-hubli/` | hubli airport taxi / taxi service in hubli airport | HBX transfers, dharwad–airport, flight pickup | core-local terms |
| `/vehicles/tempo-traveller-hubli/` | tempo traveller rent in hubli | tempo traveller rent per km, urbania on rent hubli, force cruiser, mini bus, 12/17-seater | sedan/ertiga (no demand — stays on /) |
| `/routes/hubli-to-goa-taxi/` | hubli to goa taxi/cab | hubli to goa cab fare/price, one-way | other routes |
| `/routes/hubli-to-bangalore-taxi/` | hubli to bangalore cab | …cab price, bengaluru spelling | — |
| `/routes/hubli-to-dandeli-taxi/` | hubli to dandeli cab | rafting group travel angle | — |
| `/routes/hubli-to-gokarna-taxi/` | hubli to gokarna cab | …cab price/fare, temple + beach angle | — |
| `/routes/hubli-to-belgaum-taxi/` | hubli to belgaum taxi | belagavi spelling | — |
| `/services/outstation-cabs-hubli/` | outstation cabs hubli / taxi in hubli for outstation | round-trip, per-km outstation | specific route terms (each links down to its route page) |
| `/fare/hubli-taxi-fare/` | taxi rates in hubli / car rental hubli price | car rent per km in hubli, rate card | route-specific fares (tables live on route pages; this page links to them) |

No two pages share a primary term. The homepage keeps BOTH core heads ("car rental" + "taxi service") because the SERP treats them as one local intent (same map pack); splitting them across two pages would cannibalize, not help.

## Handling decisions baked into every page
- **Hubli/Hubballi split:** every page uses "Hubli" in URL/title (higher volume in the data: 1,132 vs ~40 hubballi-variant clicks) and "Hubballi" naturally in body copy, address, and one subheading. Never dropped.
- **Route pages carry real substance** (the moat, per brief): km, hours, route taken (NH-48/NH-748 etc.), toll count, fare band per vehicle from the site's published rates (Sedan ₹10–12/km … Mini Bus ₹28/km, batta table), best departure time, what's included (driver batta, min 300 km/day billing, tolls at actuals). Facts I can't verify (exact toll plazas/current toll cost per route) get flagged with `{{ASK-SAYED}}` placeholders before publish — **not invented**.
- Every page: click-to-call + WhatsApp in first viewport, fare table, trust strip (5.0★ 58 Google reviews, 24/7, verified drivers), FAQ block (from real informational queries), breadcrumb, canonical, and the existing design system (same style.css classes: `fleet-card`, `route-row`, `faq-item`, etc. — no new design language).
- Internal linking: header nav gains "Airport Taxi" + "Tempo Traveller"; footer "Popular Routes" links re-point from `#cabForm` to the real route pages; homepage route rows link to route pages; outstation hub lists all routes; sitemap.xml updated with all 9 URLs.
- **Real photos rule:** fleet gallery photos exist and will be reused (compressed per Phase 2). No stock New-York-cab imagery.

## Explicitly NOT building (and why)
| Brief skeleton page | Verdict | Evidence |
|---|---|---|
| `/services/local-taxi-hubli/` | Not yet | local-package cluster: 8 terms, 2 clicks, ₹38 — homepage section covers it; revisit with GSC data |
| `/services/corporate-cab-hubli/` | Not yet | 2 terms, 1 click, ₹0.81 |
| `/areas/vidyanagar-taxi/` etc. | No | zero neighbourhood queries in 11 months |
| `/vehicles/innova-crysta-hubli/` | Not yet | 13 terms but 18 impr total — folded as a section on / (fleet) |
| Routes: Hampi, Murudeshwar, Sirsi, Shimoga, Davangere | Not yet | ≤6 impr each; template makes adding one ~30 min once data (or GSC) justifies it |
| Wedding car rental page | Hold | zero paid queries; but a DreamWeddingHub citation exists — decide after GSC verification |

## Meta rewrites (existing pages) — `03_meta_rewrites.csv`
The Phase 1 finding drives this: rental-language demand is 2:1 over taxi, so the homepage title leads with **Car Rental** and keeps Taxi Service. Full old→new in the CSV; headline change:

- Title: `Taxi Service in Hubli | Trishika Car Rental – 24/7 Cab Booking` (62ch, taxi-first)
  → **`Car Rental & Taxi Service in Hubli | Trishika – 24/7`** (52ch, both heads, brand, differentiator)
- Description → includes ₹10/km price signal, with-driver clarity, airport/outstation scope, phone, Hubli-Dharwad. (155ch)

## Execution plan after your approval
1. Copy live site → `/site-optimized/` (ground rule 3; original preserved for diff)
2. Apply Phase 2 P0/P1 fixes there (preloader, @import, defer, .htaccess, image pipeline — images batch-converted to WebP)
3. Build the 9 pages in priority order, matching existing markup patterns; `{{ASK-SAYED}}` facts consolidated into ONE question list before publish
4. Meta rewrites applied to homepage
5. Updated sitemap.xml
6. Deploy via Hostinger hPanel (needs your one-time login in the trishika Chrome profile) → verify GSC → submit sitemap

---
**Approve the architecture (or edit it) and I start writing pages. Per the brief, nothing gets written until you say so.**
