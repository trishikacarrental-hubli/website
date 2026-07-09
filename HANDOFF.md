# HANDOFF — Trishika Car Rental growth engine

**Last updated: 2026-07-09 (evening) — Ads restructure applied & posted, tracking wired, assets added.**
This is the master continuation doc. Read this first, then `CHANGELOG.md` (what changed), `RISKS.md` (watch-outs), `ASSUMPTIONS.md` (facts to verify). Detailed phase reports are in `/reports`. Ad build in `/ads`. GBP copy in `/gbp`.

---

## 0. Where things stand in one paragraph
Website SEO build is ~90% done and **live** (fast site, 9 new pages, schema, rental-first titles). **Conversion tracking fires two ways** — GTM `GTM-P92G7GNP` v9 *and* a direct gtag fire now built into `track-conversions.js` (resilient to the FortuneMarq Automator breaking GTM); verified live (real Call click → 200-OK conversion ping, correct ID/label). **The full Google Ads restructure is APPLIED and POSTED** to account 983-550-8200 (4 clean campaigns / 10 ad groups / 44 keywords / 10 RSAs / 196 negatives / Hubli-Dharwad geo) — **all PAUSED**, plus account-level assets (callouts, sitelinks, structured snippet, call). The old "03/22/2026 New Campaign" is now **paused** too, so account spend = ₹0/day. **The account is launch-ready: Sayed just recharges + enables the 4 new campaigns.** On GBP, service descriptions + secondary-category services are added; posts cadence is designed. The biggest remaining levers are **reviews, citations/NAP, and backlinks** — all off-page.

> **⚡ NEXT ACTION (Sayed, tomorrow):** top up the Ads prepaid balance → Campaigns → select the 4 new campaigns (Core Local / Airport / Outstation Routes / Vehicles) → **Enable**. That's the launch. Tracking will attribute real Call/WhatsApp leads from day one. (Optionally leave one small campaign as a day-1 fallback, but the old "03/22" one should stay paused — it optimizes toward the old broken signal.)

---

## 1. Access & accounts (no API keys — everything is manual / via Chrome extension)
- **Google account (owns everything):** `trishikacarrentalhubli@gmail.com` — Chrome profile named **"trishika workspace"**. Owns: Google Ads **983-550-8200** (active), GTM `GTM-P92G7GNP`, GBP "Trishika Car Rental", GSC property.
- **Canonical phone (CONFIRMED):** **+91 82175 77849** (site/GBP/schema all correct).
- **Hosting:** Hostinger — `hpanel.hostinger.com` → File Manager. Deploy = upload zip → extract → move-replace into `public_html`. (Direct File-Browser URLs 403 after a while; re-enter via hPanel to refresh the session token.)
- **GitHub:** repo `github.com/trishikacarrental-hubli/website`. ⚠️ **The token in the git remote URL is exposed in plaintext — ROTATE IT** (GitHub → Settings → Developer settings → Personal access tokens → revoke + regenerate).
- **This repo = the live site source.** `site-optimized/` is the deployable copy.

## 2. LIVE / DONE
### Ads & tracking
- ✅ **Conversion tracking fires TWO ways** (belt-and-suspenders, de-dup'd by count=One):
  1. GTM **v9**: 3 Custom Event triggers (`call_click`/`whatsapp_click`/`form_submit_whatsapp`) → Google Ads Conversion tag (ID `17442020753`, label `_imzCNTi_MwcEJG7gP1A`) + base tag.
  2. **Direct gtag** in `track-conversions.js` (added 2026-07-09 eve): `gtag('config','AW-17442020753')` + fires the conversion on every `tel:`/`wa.me` click (value ₹150). Survives GTM being clobbered by the FortuneMarq Automator.
  Verified live: real Call click → `pagead/conversion/17442020753/…&label=_imzCNTi_…&en=conversion`. `track-conversions.js` set to `no-cache` so tracking edits roll out instantly. *(Consolidate to one mechanism once the Automator is disabled — see CHANGELOG.)*
- ✅ `track-conversions.js` deployed on all 11 pages.
- ✅ Google Ads conversions cleaned: removed `Submit lead form` + `V2_Auto_Success_Test`; **"Contact – Call & WhatsApp"** is the sole action and the **account-default goal** (all campaigns).
- ✅ **FULL RESTRUCTURE APPLIED + POSTED** (via Google Ads Editor) to account 983-550-8200 — **all PAUSED**:
  - 4 campaigns (Core Local ₹300 / Airport ₹80 / Outstation ₹120 / Vehicles ₹60), Manual CPC, Search-only, **location Hubli-Dharwad** (fixed from Editor's accidental US default), EU-political=No.
  - 10 ad groups · 44 keywords (phrase/exact) · 10 RSAs (H1 pinned) · 196 negatives (152 campaign + 44 ad-group).
  - Editor Check = 0 errors; Post = 100% of every entity type.
- ✅ **Old "03/22/2026 New Campaign" PAUSED** (was ₹700/day enabled). Account total budget now **₹0/day**. The shared negative list "Trishika Master Negatives" and its AI-Max-off/CPC-₹24 tweaks are moot now that it's paused and replaced by the 4 new campaigns.
- ✅ **Account-level assets** (web UI, "Under review"): 6 callouts, 6 sitelinks (each with 2 descriptions + landing page), 1 structured snippet (Service catalog, 6 values), + the pre-existing call asset (082175 77849; call reporting left OFF to keep the real number showing).
### Website SEO
- ✅ 9 pages live (airport, tempo, 5 routes, outstation hub, fare) + rental-first titles/H1; schema (LocalBusiness/TaxiService + FAQPage); WebP images (page 9.8 MB → 909 KiB, paint ~1.7s); mobile hero video removed.
- ✅ GSC verified + 10-URL sitemap submitted.
### GBP
- ✅ Primary category kept "Car rental company" + **5 secondary categories** live (Taxi service, Airport shuttle service, Chauffeur service, Van rental agency, Transportation service).
- ✅ Description rewritten (self-drive claim removed). 8 service descriptions being added under primary + 5 flagship services under the secondary categories (copy in `gbp/services.csv` + secondary-category copy pasted from this session).
- ✅ 7 recent reviews responded. Review link live: `g.page/r/CYYqAGCT8WJ6EBM/review`.

## 3. PENDING — prioritized

### 🔴 Biggest levers (off-page — do these)
1. **Reviews / velocity** *(Sayed)* — 58 vs competitors 141–611 = the #1 map-pack bottleneck. Build a systematic ask: every trip → WhatsApp the review link. Target 8–12/mo. Reply to all (older 13+ week reviews still need replies).
2. **Citations / NAP** *(Claude-doable + Sayed for OTP)* — list identical NAP across JustDial, Sulekha, IndiaMART, Cybo, etc. Fix **JustDial** (lists wrong number 98452 06189 — needs OTP to your line). `gbp/citations.csv`.
3. **Backlinks** *(Sayed + Claude research)* — weakest area. Local partnerships (hotels, event planners, travel bloggers), tourism/route aggregators, business associations.

### 🟢 Claude-doable (queued for Mac mini continuation)
4. ~~Finish the new Ads campaign~~ **DONE** — the full 4-campaign restructure is applied + posted (paused). Only Sayed's recharge + Enable remains (§4).
5. **GBP content** — post the weekly cadence (calendar in `gbp/posts_90day.md` + the 3×/week Jul batch drafted this session); Q&A seeding is **parked** (needs a 2nd Google account — owners can't ask questions on their own listing).
6. **GSC health** — confirm all 10 pages indexed (submitted ≠ indexed); investigate the "1 other site moving to this site" note; set a query/rank baseline.
7. **New pages** — more routes (Hubli→Hampi/Mysuru/Murudeshwar/Bengaluru airport), vehicle pages (Innova Crysta, Ertiga, Sedan), a couple of guide posts.
8. **Install GA4** — currently NO analytics (only ads conversion tracking). Big blind spot; ~10-min setup.

### 🔴 Sayed-only (facts / photo uploads / payments)
9. **GBP products (6)** — photo upload blocker (extension can't upload local files). Copy in `gbp/products.csv`; fleet photos in `site-optimized/images/*.webp`.
10. **Fresh GBP photos** — profile photos 110+ days stale.
11. **Ads balance top-up** — prepaid; decide before campaigns spend heavily.
12. **Verify facts** — years in business, vehicle count, "no advance payment" true?, and confirm route distances/tolls/fares on the pages (`ASSUMPTIONS.md` #9–14).

## 4. Launching the Ads (restructure is posted — just enable)
The full restructure is **already posted** to account 983-550-8200 as **4 paused campaigns** with all keywords/ads/negatives/geo (no more drafts; the old `draftId=10203609343` "Search - Core Local (Rebuild)" and the single-campaign optimization are both superseded).
**To launch (Sayed):**
1. **Top up** the Ads prepaid balance (Billing).
2. **Campaigns** → tick the 4 new campaigns (Core Local / Airport / Outstation Routes / Vehicles) → **Edit → Enable**.
3. Leave the old campaigns paused (Campaign #1, LEADS 11/04, New Campaign 05/03, **03/22/2026 New Campaign**). Total budget of the 4 new = **≈₹560/day (~₹16.8k/mo)** — inside the ₹10–25k band; scale Core Local first to reach ₹25k.
4. **Pre-launch sanity check** (2 min): confirm each new campaign's Location = Hubli-Dharwad only, Networks = Search only, and that a test Call/WhatsApp click has recorded a Contact conversion (Goals → Conversions; the action clears "no recent conversions" once a real click fires).
- **Bidding path:** start Manual CPC (as posted) → after ~2–3 wks AND ≥15 real tracked conversions → Maximize Conversions → later tCPA. Do NOT jump to tCPA/PMax on thin data.

## 5. ⚠️ CRITICAL — FortuneMarq Automator
An app Sayed built ("FortuneMarq Automator") auto-published GTM container versions 4–8, and **each run deletes & re-adds the broken `btn` conversion tag + a test conversion**. If you re-run it against this container it will **clobber the clean v9 + the Ads cleanup**. Fix or disable that app before running it here again. (RISKS.md #4a.)

## 6. GBP content assets (where the ready-to-paste copy lives)
- `gbp/services.csv` — 8 service descriptions.
- `gbp/posts_90day.md` — 12-week post calendar (+ a 3×/week Jul batch was drafted in the session with Gemini image-poster prompts).
- `gbp/qa_seed.md` — 10 Q&A (parked; Q6 advance-policy blocked).
- `gbp/citations.csv` — citation targets.
- `gbp/review_engine.md` — review-ask templates.
- `gbp/categories.md` — category rationale.
- **Post rule learned this session:** GBP rejects posts with a **phone number in the text/image**. Keep the number out of captions and posters — the **Call now button** carries it.

## 7. Continuing on the Mac mini
1. **Clone:** `git clone https://github.com/trishikacarrental-hubli/website.git trishika_car_rental` (use a fresh token after you rotate the old one).
2. **Tools:** no build step / no node deps required for the site (static HTML/CSS/JS). Python 3 is used by `/scripts/*.py` (report generation, image optimization); Node is used by `scripts/audit.js`/`report.js` (optional).
3. **Sign in** to the "trishika workspace" Google profile in Chrome for Ads/GTM/GBP access; log into Hostinger hPanel for deploys.
4. Pick up the 🟢 Claude-doable list above, or the 🔴 levers. Recommended order: finish Ads campaign → GSC indexing check → citations → new route pages → GA4.

## 8. Change log pointer
Full chronological detail in `CHANGELOG.md` (newest entries at top cover: GBP services, conversion-tracking rebuild + verification, Ads cleanup, active-campaign optimization, new-campaign build).
