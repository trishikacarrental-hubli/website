# HANDOFF — Trishika Car Rental growth engine

**Last updated: 2026-07-09 (end of Windows session, before handoff to Mac mini).**
This is the master continuation doc. Read this first, then `CHANGELOG.md` (what changed), `RISKS.md` (watch-outs), `ASSUMPTIONS.md` (facts to verify). Detailed phase reports are in `/reports`. Ad build in `/ads`. GBP copy in `/gbp`.

---

## 0. Where things stand in one paragraph
Website SEO build is ~90% done and **live** (fast site, 9 new pages, schema, rental-first titles). **Conversion tracking is rebuilt and VERIFIED firing** (GTM container `GTM-P92G7GNP` v9). Google Ads is cleaned up: junk conversions removed, one real "Contact" conversion is the account-default, and the **active campaign is optimized** (negatives list, AI Max off, CPC ≤ ₹24). A **new clean Search campaign is 95% built as a draft** — it only needs you to pass Google's "Confirm it's you" check, set the ₹300/day budget, and publish. On GBP, 8 primary-category service descriptions + 5 secondary-category services are being added; posts cadence is designed. The biggest remaining levers are **reviews, citations/NAP, and backlinks** — all off-page.

---

## 1. Access & accounts (no API keys — everything is manual / via Chrome extension)
- **Google account (owns everything):** `trishikacarrentalhubli@gmail.com` — Chrome profile named **"trishika workspace"**. Owns: Google Ads **983-550-8200** (active), GTM `GTM-P92G7GNP`, GBP "Trishika Car Rental", GSC property.
- **Canonical phone (CONFIRMED):** **+91 82175 77849** (site/GBP/schema all correct).
- **Hosting:** Hostinger — `hpanel.hostinger.com` → File Manager. Deploy = upload zip → extract → move-replace into `public_html`. (Direct File-Browser URLs 403 after a while; re-enter via hPanel to refresh the session token.)
- **GitHub:** repo `github.com/trishikacarrental-hubli/website`. ⚠️ **The token in the git remote URL is exposed in plaintext — ROTATE IT** (GitHub → Settings → Developer settings → Personal access tokens → revoke + regenerate).
- **This repo = the live site source.** `site-optimized/` is the deployable copy.

## 2. LIVE / DONE
### Ads & tracking
- ✅ GTM **v9 published & verified**: 3 Custom Event triggers (`call_click`, `whatsapp_click`, `form_submit_whatsapp`) → one Google Ads Conversion tag **"Google Ads - Contact (Call/WhatsApp/Form)"** (ID `17442020753`, label `_imzCNTi_MwcEJG7gP1A`) + base Google tag. Broken `btn` conversion tag deleted. Verified live: firing events sends real 200-OK conversion pings.
- ✅ `track-conversions.js` deployed on all 11 pages.
- ✅ Google Ads conversions cleaned: removed `Submit lead form` + `V2_Auto_Success_Test`; **"Contact – Call & WhatsApp"** is the sole action and the **account-default goal** (4/4 campaigns).
- ✅ **Active campaign "03/22/2026 New Campaign"** optimized: shared negative list **"Trishika Master Negatives"** (37 competitor/junk terms) applied, **AI Max OFF**, **Max CPC ₹24**, conversion goal = Contact. Budget ₹700/day.
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
4. **Finish the new Ads campaign** — see §4 (needs your "Confirm it's you" first).
5. **GBP content** — post the weekly cadence (calendar in `gbp/posts_90day.md` + the 3×/week Jul batch drafted this session); Q&A seeding is **parked** (needs a 2nd Google account — owners can't ask questions on their own listing).
6. **GSC health** — confirm all 10 pages indexed (submitted ≠ indexed); investigate the "1 other site moving to this site" note; set a query/rank baseline.
7. **New pages** — more routes (Hubli→Hampi/Mysuru/Murudeshwar/Bengaluru airport), vehicle pages (Innova Crysta, Ertiga, Sedan), a couple of guide posts.
8. **Install GA4** — currently NO analytics (only ads conversion tracking). Big blind spot; ~10-min setup.

### 🔴 Sayed-only (facts / photo uploads / payments)
9. **GBP products (6)** — photo upload blocker (extension can't upload local files). Copy in `gbp/products.csv`; fleet photos in `site-optimized/images/*.webp`.
10. **Fresh GBP photos** — profile photos 110+ days stale.
11. **Ads balance top-up** — prepaid; decide before campaigns spend heavily.
12. **Verify facts** — years in business, vehicle count, "no advance payment" true?, and confirm route distances/tolls/fares on the pages (`ASSUMPTIONS.md` #9–14).

## 4. Finishing the new Ads campaign (draft is ready)
Campaign **"Search - Core Local (Rebuild)"** is built as a draft in account 983-550-8200 (Campaigns → Drafts, `draftId=10203609343`). Settings already in: Search-only (no Display/Search-Partners), AI Max off, Hubli-Dharwad, EN/KN/HI, Maximize clicks + CPC ₹24, 16 exact+phrase keywords (car rental + taxi in Hubli), RSA (9 headlines/4 descriptions), Contact conversion goal.
**To finish:** open the draft → Google throws a **"Confirm it's you"** identity check (needs your password/2FA — Claude can't do this) → set **budget ₹300/day** → Review → **Publish**. Then apply the **"Trishika Master Negatives"** list to it (shared list already exists). Keep total spend ≈ ₹1,000/day (active ₹700 + new ₹300).

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
