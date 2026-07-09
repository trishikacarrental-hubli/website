# ASSUMPTIONS — inferred, not confirmed. Verify each.

1. **This repo is the exact source of the live site** at trishikacarrentalhubli.in (matched sitemap domain + content; not diffed against production byte-for-byte).
2. **Fares published on the site are current** — used as fact in baseline; flagged in HANDOFF for confirmation.
3. **SERP/map-pack checks reflect Hubballi users** — Google showed "Hubballi, Karnataka" as search location on 2026-07-08. Rankings vary by exact location within the city.
4. ~~GBP name field assumption~~ **VERIFIED 2026-07-08:** name field is clean "Trishika Car Rental".
5. ~~Conversions meaningless assumption~~ **VERIFIED 2026-07-08:** the only firing conversion action is a test tag "V2_Auto_Success_Test" (counting Every, 30-day window); "Submit lead form" is Inactive with 0 ever. Conversion data confirmed junk.
5a. ~~Which number is canonical~~ **CONFIRMED 2026-07-09: canonical = +91 82175 77849** (matches site/GBP/schema — those are correct). JustDial's 98452 06189 and Instagram's 7019618668 are the out-of-sync ones to fix.
6. **"Other search terms" (₹30.4k hidden) behaves like the visible junk** in Campaign #1 (broad match waste) — unverifiable by definition; tightening match types is the mitigation either way.
7. **Route distances/times on the site are roughly correct** — not independently verified against Maps yet (Phase 3 will verify per route page).
8. **hero_bg.png (2.5 MB) is unreferenced dead weight** — no reference found in index.html or style.css; confirm before deleting. (Excluded from site-optimized deploy copy.)

## Phase 3 content facts (general knowledge, used on pages — Sayed to verify)
9. Routes/roads: Goa via Dharwad→Alnavar→Anmod Ghat (NH-748)→Mollem→Ponda; Bangalore via NH-48 (Davangere–Chitradurga–Tumakuru); Dandeli via Kalghatgi–Haliyal; Gokarna via Yellapur–Ankola; Belgaum via NH-48 (Kittur), ~100 km / 2 hrs (not on site's own routes list).
10. NH-48 Hubli→Bangalore tolls stated as "budget ₹600–800" — verify actual current total.
11. Hubli Airport distance from city centre stated as 8–10 km / 20–25 min.
12. Sample trip costs are pure arithmetic on the published rate card (300 km/day min × rate + batta) — no invented prices; airport fixed rates NOT published (page says "fixed quote on WhatsApp").
13. Force Urbania/Cruiser: pages say "availability varies by date, call to confirm" — does NOT claim ownership. Confirm what Trishika can actually arrange.
14. One-way drops stated as "on request, subject to return logistics" — confirm this is offered.
