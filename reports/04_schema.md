# Phase 4 — Structured Data & Local Signals

All JSON-LD lives in `/site-optimized/` pages, injected by [`scripts/add_schema.py`](../scripts/add_schema.py) (idempotent — safe to re-run after any page rebuild). Every block machine-validated (JSON parse) locally; run Google's Rich Results Test on the live URLs right after deploy (listed below).

## What was implemented

### Homepage — LocalBusiness + TaxiService (upgraded, was already present)
- Added **`@id`: `https://trishikacarrentalhubli.in/#business`** — the entity anchor every subpage's Service schema now references via `provider`.
- Added **Google Maps listing to `sameAs`** (`https://maps.google.com/?cid=8818876635617962630`, derived from the GBP place id) alongside Instagram + Facebook — explicit website↔GBP entity link.
- Already correct and kept: full PostalAddress, `geo`, 24/7 `openingHoursSpecification`, `priceRange`, telephone in E.164 (`+918217577849`), FAQPage.

### All 9 subpages
| Schema | Coverage | Notes |
|---|---|---|
| **BreadcrumbList** | 9/9 | Home → section → page, matching the visible breadcrumb |
| **Service** | 8/9 (all except the fare rate-card page, which is not a service) | `serviceType` per page (airport taxi / outstation taxi / group vehicle rental), `provider: {@id: #business}`, `areaServed` Hubballi+Dharwad, `availableChannel` with phone |
| **FAQPage** | 9/9, 5 questions each | Extracted from each page's visible FAQ HTML — the same Q&As, sourced from real informational queries in the Phase 1 data ("how much does a cab from hubli to goa cost", "tempo traveller rent per km in hubli", "taxi rates in hubli"…). Schema always mirrors on-page content — no invisible-content risk |

### Deliberately NOT implemented (per brief §Phase 4 and Google guidelines)
- **`Review` / `AggregateRating`: refused.** There are no reviews collected on the website itself. Importing GBP review counts/stars into schema violates Google's self-serving review markup guidelines and risks a manual action. If you want on-site ratings later, we build a genuine on-site review collection flow first — then mark up only those.

## NAP verification (byte-level, scripted)

| Surface | Address | Phone | Verdict |
|---|---|---|---|
| Schema (homepage) | Shop No 37, Yashasvi Apt, Gokul Rd, Gandhi Nagar / Hubballi / 580030 | +918217577849 (E.164) | ✔ |
| Footer — all 10 indexable pages | identical string | tel:+918217577849 ×7–9 per page, display +91 82175 77849 | ✔ |
| GBP (checked Phase 0) | matches | 082175 77849 (same number, local format) | ✔ |
| Stray numbers on site (98452 06189 / 7019618668) | — | **0 occurrences** | ✔ |
| **JustDial** | matches | **+91 98452 06189 — MISMATCH** | ❌ P0, already in RISKS 1a / HANDOFF (canonical-number decision pending) |
| Instagram posts | — | 7019618668 "Madhu Car Rentals" | ❌ flagged in HANDOFF |

## Post-deploy validation checklist (do together at deploy)
1. Rich Results Test: `/` (LocalBusiness+FAQ), `/services/airport-taxi-hubli/` (Service+FAQ+Breadcrumb), one route page.
2. GSC → verify property → submit sitemap → Enhancements report picks up FAQ/Breadcrumb within days.
3. After Sayed decides the canonical phone: fix JustDial (or GBP+site) so all citations match — the schema is ready either way (one string to change).

**Phase 4 complete. Stopped. Everything is staged in `/site-optimized/` — ready to deploy together: log into hpanel.hostinger.com in the trishika Chrome profile and say go.**
