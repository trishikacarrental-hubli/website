# Phase 6a — Google Ads Diagnosis

**Account:** 983-550-8200 (Trishika Car Rental Hubli). Period analysed: 6 Aug 2025 – 8 Jul 2026.
Sources: live dashboard (Phase 0) + `keyword_master.csv` (Phase 1).

## The headline problem: you are optimising toward a test event

The account has spent **₹92,481** and every rupee of "performance" traces to a single conversion action, **`V2_Auto_Success_Test`** — a leftover test tag that counts *every* fire (62 "conversions"), 30-day window, status "Needs attention". The real lead action, **`Submit lead form`, is Inactive with 0 conversions ever.** The currently-active campaign **LEADS 11/04** is running a bid strategy that is *learning from this test event.*

**Nothing else in this diagnosis matters until this is fixed.** No smart bidding, no CPA target, no "let the algorithm optimise" — because the algorithm is optimising toward noise. Section 6e rebuilds tracking first.

## Current waste

| Source | Spend | Read |
|---|---|---|
| **Campaign #1** (paused) | ₹46,942 | 2,045 clicks, **0 real leads.** 54% of its visible search terms were junk (ola/uber/rapido/jobs). Its broad match also fed Google's hidden "other search terms" bucket. This one campaign is ~half of all account spend and produced nothing traceable. |
| Self-drive clicks (account-wide) | ~₹839 visible (more hidden) | A service you don't offer. Pure waste. |
| Ride-hailing / app / job / wrong-city queries | ~₹1,400 visible | Broad-match spillover. |
| **Hard, certain waste** | **≈ ₹2,200 visible** + an unknown slice of the ₹30.4k hidden bucket | Removed permanently by the negative lists below. |

Match-type distribution (visible terms): broad match = 504 terms but only ₹1,358 spend — cheap individually, but it's the intake valve for the junk and the hidden bucket. **Killing broad match is the structural fix.**

Estimated recoverable spend once negatives + exact/phrase-only are applied: **₹6k–10k of the ₹58k search-term spend (10–17%)** — realised in week one, redeployed to the converting core.

## Search-term → ad-group mapping failures

The old account had ~everything in one "Ad group 1" per campaign. So "hubli to goa cab", "tempo traveller rent", "self drive car hubli" and "car rental in hubli" all shared one ad and one landing page (the homepage). Result: ad copy never matched the query, and route/vehicle searchers hit a generic page. The rebuild fixes this with tight, single-theme ad groups each mapped to the *specific* Phase-3 landing page.

## What actually converts (where the budget should go)

From the data, in priority order:
1. **Core local — "car rental / taxi / cab in hubli"** — 132 term variants, 83% of converting volume. "car rental in hubli" alone = 11.65 conv. This gets the most budget.
2. **Airport** — "taxi service in hubli airport" converted at **25% CVR / ₹70 CPA**, the best in the account. Tiny volume, huge efficiency — deserves its own campaign so it's never starved.
3. **Outstation routes** — thin but real (Goa, Bangalore, Belgaum each converted). Cheap to run; one ad group per route mapped to its route page.
4. **Tempo Traveller / group vehicles** — the only vehicle with demand; Urbania even converted.

## Recommendations on the brief's optional campaigns

- **Performance Max — argue AGAINST, for now.** PMax needs reliable conversion data to optimise; you have none. It would spend across Display/YouTube/Gmail with a broken signal and cannibalise brand/core. Revisit only after 30+ real conversions are tracked. (Verdict: no.)
- **Competitor campaign — skip as a standalone.** Only one competitor term ever converted ("tt travels", and it's arguably a mis-spelled own-brand-adjacent query). Not worth a separate budget at ₹10–25k/mo. Keep competitor terms as *negatives* instead (below).
- **Brand campaign — skip.** Near-zero brand search volume ("trishika…" = 6 clicks all year). Not worth defending yet; revisit as brand grows.
- **Call-Only — recommend as a fast-follow, not day one.** Calls are how this business converts, so call-only is genuinely promising. But launch it *after* call-conversion tracking is live (6e), so you can judge it. Meanwhile, call assets are attached to the search campaigns.

## The new structure (detail in `/ads/import/`)

| Campaign | Daily budget | Ad groups | Landing page(s) |
|---|---|---|---|
| **Search — Core Local** | ₹300 | Car Rental Hubli · Taxi & Cab Hubli · Travels Hubli | `/` (rental-first homepage) |
| **Search — Airport** | ₹80 | Airport Taxi HBX | `/services/airport-taxi-hubli/` |
| **Search — Outstation Routes** | ₹120 | Goa · Bangalore · Dandeli · Gokarna · Belgaum | matching `/routes/…` page each |
| **Search — Vehicles** | ₹60 | Tempo Traveller & Group | `/vehicles/tempo-traveller-hubli/` |

≈ **₹560/day ≈ ₹16.8k/month** — inside the ₹10–25k band, weighted to what converts. To reach ₹25k, scale Core Local first (it has the demand headroom). Match types: **Phrase + Exact only. No broad.** Every ad group: 5–8 keywords, one theme, one RSA, one landing page.

**Deliverables:** this diagnosis + `/ads/import/` (Ads Editor CSVs) + `/ads/import/README.md` (exact import order & rollback) + conversion-tracking rebuild in 6e.
**Then stop.**
