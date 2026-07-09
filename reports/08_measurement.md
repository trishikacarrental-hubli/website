# Phase 8 — Measurement & Cadence

The goal of this phase is to make the whole engine maintainable after handoff — so it keeps working without a strategist babysitting it. Opinionated on purpose.

## The 8 metrics that matter

Track these. Everything else is a distraction.

| # | Metric | Where | Why it's on the list |
|---|---|---|---|
| 1 | **Leads (calls + WhatsApp + form)** | Ads conversions + GBP calls/messages | The only output that pays the bills. Count them all — this business converts on the phone. |
| 2 | **Cost per lead (CPL)** | Ads (spend ÷ leads) | The single number that says if paid is working. Target: set one once tracking is trustworthy. |
| 3 | **Phone calls from GBP** | GBP → Performance → Calls | Your map-pack listing drives calls the website never sees. Free demand. |
| 4 | **GBP review count & rating** | GBP → Reviews | The #1 map-pack lever. Watch it climb week over week. |
| 5 | **Map-pack presence** for "car rental in hubli" / "taxi service in hubli" | Manual search from Hubli (or a rank tracker) | Are you *in* the 3-pack? That's where the local clicks are. |
| 6 | **GBP profile views / searches** | GBP → Performance | Top-of-funnel local demand and whether it's growing. |
| 7 | **Organic clicks & top queries** | Search Console (now verified) | Are the new route/service pages ranking and pulling traffic? |
| 8 | **Wasted spend %** (junk clicks ÷ spend) | `report.js` weekly | The leak. Should trend toward zero as negatives hold. |

## The ~30 that don't (stop reporting on these)

Impressions (vanity), raw CTR (without conversion context), average position/"impression share" obsession, bounce rate on a one-page-intent site, time-on-page, Ads "optimisation score" (it pushes you toward broad match + PMax), Display/YouTube view metrics (you're not running them), keyword *count*, social followers, "engagements", page-load score chased below what users feel, cost-per-click in isolation (a ₹40 click that converts beats a ₹5 click that doesn't), and every automated "recommendation" email that isn't a negative keyword. If a number doesn't change what you *do* this week, don't track it.

## Weekly routine — 20 minutes

1. **Export** the Google Ads *Search terms* report (last 7 days) → run `node scripts/report.js <export.csv>`. It prints: spend, leads, CPL, top converters, bleeders, and **new junk to negative**.
2. **Add the flagged negatives** (1 click each in the shared negative list).
3. **Shift budget** a notch from bleeders toward top converters. Don't over-tune — one change per week.
4. **GBP:** reply to every new review (<48h), and confirm at least 2–3 review asks went out (the drop-off routine). Post the week's GBP update (from `gbp/posts_90day.md`).
5. **If CPL is blank or 0 → stop and fix tracking.** Never bid on a broken signal.

## Monthly routine — 45 minutes

1. **Rankings:** manual map-pack + organic check from Hubli for the core terms; note movement.
2. **GBP Insights:** views, calls, direction requests — trend vs last month. Add fresh photos (staleness hurts).
3. **Search Console:** which queries/pages are gaining? Any route page with impressions but no clicks = rewrite its title/meta. Any query with demand but no page = candidate for the next route/vehicle page (data-gated, same as Phase 3).
4. **Content refresh:** update fares if they changed; add one new route page if the data now justifies it (Hampi/Murudeshwar/Sirsi were held pending demand).
5. **Bidding review:** enough real conversions to move Manual CPC → Maximize Conversions? (See `ads/import/README.md` thresholds.)

## The report script

`scripts/report.js` (Node, no dependencies) ingests a raw Google Ads search-terms export (handles the UTF-16 tab-delimited format as-is) and writes a one-page summary to `reports/latest_report.md`. It's the weekly routine's engine — tested against the baseline export. Run it, act on the three "do this week" lines, done.

## 90-day expectation curve — realistic, no fairy tales

| When | What to expect | What moves it |
|---|---|---|
| **Week 1** | **Ad waste drops immediately** once negatives + exact/phrase go live. CPL should fall as junk clicks stop. This is the fastest, most certain win. | Negatives + structure (built, pending enable) |
| **Weeks 1–2** | New route/service pages **indexed** by Google (sitemap submitted). CRO fixes lift form/call rate. | Deploys #1–3 (done/pending) |
| **Weeks 4–8** | **Map-pack movement** — but only if review velocity is real. This is on the review engine, not the website. 2–3 reviews/week is the lever. | Review engine + categories (categories live) |
| **Weeks 8–16** | Route/service pages start **ranking** for their long-tail terms; organic leads begin trickling. | Content + backlinks/citations |
| **Ongoing** | Compounding: more reviews → higher pack rank → more calls → more reviews. | The weekly routine, held consistently |

**Said plainly:** "page 2 → page 1" for a competitive head term is *not* something anyone can promise by a date — it depends on review velocity and competitors who've had 10–15 years and 100s of reviews. What **is** promisable: the ad waste stops in week one, the pages get indexed in weeks, and the map pack moves *if and only if* the reviews come. The engine is built; the fuel is review velocity + the 20-minute weekly habit.

## The one thing that decides whether any of this works

**Consistency on two habits:** (1) ask every rider for a review at drop-off, (2) run the 20-minute weekly routine. Everything else — the pages, the schema, the ad structure, the CRO — is scaffolding. These two habits are the engine. Skip them and the scaffolding just sits there.

**Phase 8 complete. This finishes the phased brief (0–8).**
