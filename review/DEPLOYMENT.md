# Review funnel — LIVE deployment record

**Status:** 🟢 LIVE since 2026-07-09
**URL:** https://trishikacarrentalhubli.in/review/
**Host:** Hostinger (Business plan, account `u330519110`), site `trishikacarrentalhubli.in`

## What's on the server
`public_html/review/`
- `index.html`
- `api/db.php`  ← real MySQL credentials (NOT in git — gitignored)
- `api/next.php`, `api/copied.php`, `api/stats.php`
- `api/seed_reviews.txt` (249 reviews, blocked from HTTP by .htaccess)
- `api/.htaccess`

`setup.php` and `reset.php` were used once during deploy and **deleted** (both return 404 now).

## Database
- **DB name / user:** `u330519110_reviews`
- **Host:** `localhost`
- **Password:** stored only in `review/api/db.php` on the server (gitignored). If you need it, read that file via hPanel File Manager, or reset it in hPanel → Databases.
- **Seeded:** 249 reviews (189×5★, 60×4★), all `available`.

## Secret keys (in the committed PHP source)
- `stats.php` key: `st-3Hn6Pj4wRbQy8` → check pool health:
  `https://trishikacarrentalhubli.in/review/api/stats.php?key=st-3Hn6Pj4wRbQy8`
- (setup.php key was `su-7Fq2Kd9mXtZr4` — file deleted, key now moot)

## How it behaves (verified live)
- Scan QR → pick stars.
- **4–5★:** serves one unique review from the pool (`next.php`), marks it `served`. On **Copy**, `copied.php` marks it `used` — it is never shown again (serve-and-burn, no duplicates). Then the Google review page opens.
- **1–3★:** routed to private WhatsApp to the owner (`wa.me/918217577849`) — not public.
- Abandoned (served-but-not-copied) reviews auto-recycle to `available` after 30 min.

## Topping up the pool later
1. Add lines to `review/api/seed_reviews.txt` (format `5|text` or `4|text`).
2. Re-create `setup.php` on the server (copy from git history), set a fresh `$KEY`.
3. Re-upload `seed_reviews.txt` + `setup.php`, visit `setup.php?key=...` once (duplicates auto-skip).
4. **Delete `setup.php`** again.

## Redeploying files (how it was done)
The Chrome extension **cannot upload local files** to Hostinger. Files were created via
hPanel File Manager → New file → Ace editor, with content injected byte-exact through the
editor's JS API. The File Manager also exposes a same-origin save API
(`PUT /<token>/api/resources/<path>`) but it requires the session auth token, so the editor
route is the reliable path.

## Analytics (GA4) — wired 2026-07-09
- gtag.js for **GA4 property `G-DCRPBD1L2J`** ("Trishika Car Rental Hubli") is in `index.html` `<head>`.
- Verified live: `gtag/js` loads, and hits reach the property — GA4 **Realtime showed 1 active user** during the test.
- Events the page sends (all via `gtag('event', …)`):
  - `page_view` (auto)
  - `stars_selected` (param `stars`)
  - `suggest_another`
  - `review_copied` (params `stars`, `id`) ← the money event (customer copied a review)
  - `left_review` (clicked through to Google)
  - `low_rating` (param `stars`) — 1–3★ path
  - `feedback_sent` — sent private WhatsApp feedback
- **Suggested next step (GA4 admin):** once these events show under Admin → Events (usually within 24h), mark
  `review_copied` and `left_review` as **Key events** so they count as conversions.
- Note: in a browser with an ad/privacy blocker the `/g/collect` beacons may show a 5xx/blocked status — that's
  client-side only; real mobile visitors (QR scans) collect normally (Realtime confirmed data lands).

## QR code
`review/qr/trishika-review-qr.png` / `.svg` → points to `https://trishikacarrentalhubli.in/review/`.
