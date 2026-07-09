# Phase 1 — Search Term Mining

**Source:** `data/search_terms_12mo.csv` (1,340 rows, 6 Aug 2025 – 8 Jul 2026) → **`data/keyword_master.csv`** (725 normalized terms; built by `scripts/build_keyword_master.py`, deterministic and re-runnable).
**Reconciliation:** master totals = report totals exactly (18,648 impr / 1,414 clicks / ₹27,713.13 / 44.01 conv).

> **Standing caveat on every conversion number:** the account's only firing conversion action is a leftover test tag (`V2_Auto_Success_Test`, counts every fire). Conversions here are treated as a *weak directional signal* — good enough to rank themes, not good enough to set bids. Nothing in this report should be used for tCPA until tracking is rebuilt.

Intent split of the ₹27.7k visible spend: transactional ₹25,246 (91%) · navigational/brand ₹1,221 · irrelevant ₹1,074 · informational ₹169 · job-seeker ₹4.

---

## 1. The money terms

**Where conversions actually came from (top of 29 converting terms):**

| Term | Clicks | Cost | Conv | CPA |
|---|---|---|---|---|
| car rental in hubli | 214 | ₹4,821 | 11.65 | ₹414 |
| taxi service in hubli | 102 | ₹2,242 | 5.00 | ₹448 |
| car for rent hubli | 17 | ₹434 | 3.00 | **₹145** |
| taxi service in hubli airport | 8 | ₹141 | 2.01 | **₹70** |
| car rental hubli | 87 | ₹1,951 | 2.00 | ₹976 |
| rental car in hubli | 72 | ₹1,386 | 2.00 | ₹693 |
| car rent hubli | 42 | ₹849 | 2.00 | ₹425 |
| cab service in hubli | 55 | ₹1,510 | 1.33 | ₹1,136 |
| hubli car rental | 47 | ₹1,039 | 1.00 | ₹1,039 |
| + 20 more single-conversion variants of the same two themes | | | | |

**By conversion *rate*** (threshold: ≥5 clicks — chosen because only 12 converting terms clear even that bar; this account is too small for a top-30 CVR list to exist honestly):

| Term | Clicks | CVR | Cluster |
|---|---|---|---|
| taxi service in hubli airport | 8 | **25.1%** | airport |
| hubli car rent | 5 | 20.0% | core-local |
| car for rent hubli | 17 | 17.6% | core-local |
| hubli car travels | 8 | 12.5% | travels-local |
| cab service hubli | 16 | 6.3% | core-local |
| car rental in hubli | 214 | 5.4% | core-local |
| taxi service in hubli | 102 | 4.9% | core-local |

The two lists agree on the shape: **one core cluster ("car/cab rental/taxi in hubli", 132 term variants, ₹22,974 = 83% of visible spend, 34 of 44 conversions) plus an airport cluster that converts 5× better than anything else.** Everything else is noise at current spend levels.

Note "hubli car travels" converting — **"travels" is the North-Karnataka word for a car-hire firm**. 49 travels-language terms spent ₹638 with 2 conversions. Keep them; they're customers, not agencies.

## 2. The bleeders

Two honest numbers, because the tracking is junk:

- **Hard waste (wrong intent, would never convert): ₹2,233** across 229 terms — self-drive ₹839, non-converting competitor/app queries ₹1,110, wrong-city ₹101, auto-repair ₹76, jobs ₹4, misc ₹103. This is certain, and the negative lists in §6 remove it permanently.
- **Zero-recorded-conversion spend: ₹9,871** — but most of it sits on terms *identical in intent* to converting ones ("rental car hubli" ₹780/0 conv vs "car rental in hubli" ₹4,821/11.65 conv). That split is tracking noise, not term quality. Do NOT prune these until tracking is fixed.

The multiplier: these figures cover only the **visible 47% of search spend**. The hidden "other search terms" bucket (₹30,415) was fed mostly by Campaign #1's broad match — the campaign whose *visible* terms were 54% junk. Conservative estimate of total recoverable waste including the hidden bucket: **₹6k–10k of the ₹58k search-term spend (10–17%)**, realized via match-type tightening + negatives, not term-by-term surgery.

Fastest ROI in the project, in order: (1) fix conversion tracking, (2) import negatives, (3) kill broad match. All Phase 6, all executable within a day of go-ahead.

## 3. Route demand map

**The data does not support the outstation-first thesis.** All outward routes combined, over 11 months: **47 terms, 216 impressions, 24 clicks, ₹515 (1.9% of visible spend), 2 conversions.**

| Route | Impr | Clicks | Cost | Conv | Read |
|---|---|---|---|---|---|
| Hubli → Goa | 105 | 11 | ₹222 | 0 | Most volume; heavy price-intent ("price/fare" in 5 of 11 terms) |
| Hubli → Bangalore | 39 | 5 | ₹108 | 1 | Converted |
| Hubli → Dandeli | 33 | 5 | ₹79 | 0 | Real clicks |
| Hubli → Gokarna | 29 | 2 | ₹82 | 0 | Impressions without clicks — ad copy never matched |
| Hubli → Belgaum | 8 | 1 | ₹25 | 1 | 1 click → 1 conversion |
| Hubli → Hampi | 6 | 0 | ₹0 | 0 | Monitor |
| Hubli → Murudeshwar | 4 | 0 | ₹0 | 0 | Monitor |

Caveat before you abandon outstation: the old campaigns barely *targeted* route keywords, so low spend partly reflects low coverage, not just low demand. But impressions don't lie about search volume: these are single-digit-per-month queries in Hubli. **Routes are an organic play (cheap pages that own the query forever), not a paid-budget priority.**

## 4. Vehicle demand map

| Vehicle | Terms | Impr | Clicks | Cost | Conv |
|---|---|---|---|---|---|
| **Tempo Traveller** | 19 | 171 | 15 | ₹267 | 0 |
| Force Urbania | 4 | 22 | 4 | ₹100 | 0.5 |
| Force Cruiser | 1 | 18 | 2 | ₹40 | 0 |
| Innova / Crysta | 13 | 18 | 1 | ₹14 | 0 |
| Ertiga / Sedan / Eeco / SUV / luxury | 18 | 21 | 0 | ₹0 | 0 |

One real vehicle market: **group vehicles.** Tempo Traveller is the only vehicle with meaningful volume (and "tempo traveller rent per km in hubli" — 42 impressions — is a pricing page begging to exist). Urbania even converted. Innova demand is surprisingly thin in paid search; sedan/Ertiga demand is effectively zero as standalone queries — people search the service, not the car.

## 5. Content gaps → the organic build list (data-gated, cite = cluster row in keyword_master.csv)

| Priority | Page | Evidence (11 mo) |
|---|---|---|
| **P0** | `/services/airport-taxi-hubli/` | airport cluster: 219 impr, 12 clicks, ₹223, **3.01 conv @ 25% CVR** |
| **P0** | `/vehicles/tempo-traveller-hubli/` (cover Urbania+Cruiser on-page or as sibling) | tempo 171 impr + urbania 22 + cruiser 18; per-km price queries |
| **P1** | `/routes/hubli-to-goa-taxi/` | 105 impr, 11 clicks; price-intent → needs fare table |
| **P1** | `/routes/hubli-to-bangalore-taxi/` | 39 impr, converted |
| **P1** | `/routes/hubli-to-dandeli-taxi/` | 33 impr, 5 clicks |
| **P1** | `/routes/hubli-to-gokarna-taxi/` | 29 impr; CTR failure in ads = SERP opportunity |
| **P2** | `/routes/hubli-to-belgaum-taxi/` | thin (8 impr) but converted; cheap to add |
| **P2** | `/fare/hubli-taxi-fare/` | "car rental hubli price" 50 impr, "taxi rates in hubli" 21, "car rent per km in hubli" 18 |
| Monitor, don't build yet | Hampi, Murudeshwar, Sirsi, local-package, corporate, wedding | <10 impr each in data (wedding has zero paid queries but a DreamWeddingHub citation exists — revisit with GSC data once verified) |

**Not justified by this data:** the brief's neighbourhood pages (`/areas/vidyanagar-taxi/` — zero queries), per-sedan/Ertiga vehicle pages, Sirsi/Shimoga/Davangere route pages. GSC data (once verified) gets a veto/revive vote in Phase 3.

## 6. Negative keyword list (ready to import)

**Campaign-level (account-wide, all campaigns):**

```
# Self-drive (₹839 waste) — phrase match negatives
"self drive"
"self driven"
"self driving"
"without driver"
"self car"
"self rental"
# Ride-hailing apps (₹1,000+ incl. hidden) — phrase
"rapido"
"ola"
"uber"
"zoom car"
"zoomcar"
"namma yatri"
"blusmart"
"red taxi"
"bharat taxi"
"bharath taxi"
"taxisafar"
# Job/commerce/irrelevant — phrase
"job"
"salary"
"vacancy"
"attachment"
"olx"
"second hand"
"driving school"
"car wash"
"car repair"
"car servicing"
# Wrong-geo (exact-match negatives — do NOT phrase-block these cities; they are route destinations)
[car rental rishikesh]
[hassan cab service]
[guwahati to tezpur car fare]
[car service in hubli]
[hubli car service]
```

**Ad-group-level** (structural — becomes real at Phase 6 restructure): cross-negatives so themes don't cannibalize — e.g. "tempo traveller"/"urbania"/"cruiser" negatived in Core-Local, "airport" negatived in Core-Local and routes, route destination names negatived in Core-Local. Local competitor brands (sai cabs, shiva cabs, tt travels, khushi, nikhil…, ₹300 visible) are **withheld from the negative list** pending the Phase 6 competitor-campaign decision — one of them (tt travels) recorded 2.5 conversions.

## 7. The uncomfortable finding

**You are marketing a taxi company, but your customers are shopping for a car rental — and your outstation-routes belief has almost no paid demand behind it.**

Two numbers:
1. Among transactional terms, **rental-language ("car rental / rent a car / car hire") outweighs taxi/cab-language 2:1 in clicks (814 vs 390) and 25.2 vs 14.4 in conversions.** Yet the site's title tag, H1, logo strapline and ticker all lead with "Taxi Service in Hubli". The single best thing in the account — "car rental in hubli", 11.65 conversions — is the term the site treats as secondary. (Silver lining: the GBP primary category "Car rental company" that looked wrong yesterday is actually aligned with where the demand is. The taxi-pack fight can be won with a *secondary* category + the airport/routes pages.)
2. **Outward routes are 1.7% of clicks and 1.9% of spend over 11 months.** The margin story for outstation may be true per-trip, but the demand pipeline for it in Hubli paid search is a trickle. Routes belong in cheap, permanent organic pages; the paid budget belongs on core-local + airport.

---

**Deliverables:** `data/keyword_master.csv` (725 rows, 17 columns per brief spec; `conv_value` empty — not present in the source report) · this report · classification scripts in `/scripts/` for re-runs on fresh exports.

**Phase 1 complete. Stopped. Next: Phase 2 (technical SEO audit + CWV measurement) on your go. Note: Phase 2's live CWV measurement and Phase 3's architecture both benefit from the deploy-method answer and GSC verification (still open in HANDOFF).**
