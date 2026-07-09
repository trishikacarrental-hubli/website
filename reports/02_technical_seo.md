# Phase 2 — Technical SEO Audit

**Site:** https://trishikacarrentalhubli.in/ (single page + 404.html) · **Server:** LiteSpeed, Brotli on, TTFB 50–80 ms (healthy)
**Measured** (not guessed): Lighthouse 12 runs on the live site, 2026-07-08 — full data in [`02_cwv.json`](02_cwv.json), re-runnable via [`scripts/audit.js`](../scripts/audit.js).

| Live scores | Perf | LCP | FCP | Speed Index | TBT | CLS | Page weight |
|---|---|---|---|---|---|---|---|
| **Mobile** | **60** | **5.7 s** ❌ | 3.8 s | 6.4 s | 280 ms | 0.005 ✔ | **9,803 KiB** |
| **Desktop** | 64 | 4.2 s ❌ | 1.9 s | 3.3 s | 40 ms | 0.011 ✔ | 12,625 KiB |

SEO 100 · Best-practices 100 · Accessibility 97. **The site's problem is not SEO hygiene — it's weight and render delay.** CLS and TTFB are excellent; every second of LCP pain is self-inflicted by assets and the preloader. Brief target: sub-2-second load on 4G. Currently 5.7 s.

---

## P0 — fix before spending another rupee on clicks

### P0-1 · Preloader hides the page for a hard-coded 2.2 s
- **Where:** [script.js:14-19](../script.js) (`setTimeout(..., 2200)`), markup [index.html:153-163](../index.html)
- Every visitor — including every ₹20 paid click — stares at an animated logo for 2.2 s + 0.5 s fade before seeing the phone number. Measured "element render delay" is 1.4 s of mobile LCP; the preloader is the biggest single contributor.
- **Fix:** delete the preloader entirely (recommended for a lead-gen page), or dismiss on `window load` with a 300 ms cap.
- **Impact:** −1.5 to −2 s LCP/FCP for free. The single highest-ROI line change on the site.
- **Verify:** re-run `node scripts/audit.js`; LCP should drop below ~3.5 s from this alone.

### P0-2 · 9.4 MB of images/video on a 4G audience (measured savings: 4,403 KiB mobile / 6,805 KiB desktop)
| Asset | Served | Wasted (LH) | Where | Fix |
|---|---|---|---|---|
| `images/hero-mobile.mp4` | **5,005 KB** — autoplay on mobile hero | (all of it, on 4G) | [index.html:237-239](../index.html) | Replace with a ≤80 KB WebP poster + optional tap-to-play; at minimum `preload="none"` + `poster` |
| `images/hero-bg.png` | 2,585 KB — desktop LCP background | 2,322 KB | [style.css:598](../style.css) | Convert to WebP/AVIF ≤200 KB at 1920w; add `<link rel="preload">` for it |
| `Fleet Gallery/…20.34.58.jpeg` | 1,364 KB | 1,361 KB | index.html:401 | Resize to 480w WebP (~40 KB) — it renders in a ~300 px card |
| 5 fleet PNGs (tempo/sedan/ertiga/innova/minibus) | 465–502 KB each | ~450 KB each | index.html:488-548 | These are cut-out car renders — WebP at 640w ≈ 30–50 KB each |
| 11 more gallery JPEGs | 120–250 KB each | ~60–90% each | index.html:397-462 | Batch-resize to 480w WebP |
| `assets/og-image.jpg` | 2,585 KB (on share only) | ~2,400 KB | index.html:37 | 1200×630 JPEG ≤150 KB |
- **Impact:** mobile page 9.8 MB → ~1.5 MB; desktop 12.6 MB → ~2 MB. On 4G this is the difference between a bounce and a call.
- **Note:** all conversions happen via `tel:`/WhatsApp in the first viewport — every byte below the fold is pure decoration. It must never compete with the fold for bandwidth.

### P0-3 · Render-blocking chain: 2,110 ms measured savings (mobile)
- **The worst part:** [style.css:7](../style.css) has `@import url('fonts.googleapis.com/…Poppins:ital…')` — a **second, duplicate** Google-Fonts stylesheet (adds italic + extra weights) discovered only after style.css downloads. HTML → CSS → fonts-CSS → fonts is a 4-hop critical chain.
- Also blocking: the first fonts CSS ([index.html:133-135](../index.html), 12 font variants requested, most unused), GSAP + ScrollTrigger from CDN ([index.html:1215-1216](../index.html)), style.css, script.js.
- **Fix:** delete the `@import` line (already covered by the HTML link); trim Poppins to the 3 weights actually used + Inter to 2; add `defer` to both GSAP scripts and script.js (all code is DOM-ready-gated, safe to defer); GSAP is used only for the hero entrance — consider replacing with CSS animations and deleting 43 KB of JS (GSAP scripting alone measured 347 ms + 138 ms on mobile main thread).
- **Impact:** −1.5 to −2 s FCP mobile.

## P1 — structural correctness

### P1-1 · www duplicate host serves the full site with 200
- Measured: `https://www.trishikacarrentalhubli.in/` → 200 (no redirect). Only the canonical tag disambiguates.
- **Fix** ([.htaccess](../.htaccess), after the HTTPS block):
  ```apache
  RewriteCond %{HTTP_HOST} ^www\.(.+)$ [NC]
  RewriteRule ^(.*)$ https://%1/$1 [R=301,L]
  ```
- **Impact:** consolidates crawl + any stray www links; removes a whole duplicate site from Google's view.

### P1-2 · 404 serves the homepage instead of the built 404 page
- [.htaccess:24](../.htaccess): `ErrorDocument 404 /index.html` — status code is correctly 404 (verified live), but users get the full homepage as the error page and the crafted [404.html](../404.html) is never used.
- **Fix:** `ErrorDocument 404 /404.html`.

### P1-3 · Search Console property unverified → the site is flying blind organically
- Verified in Phase 0: property exists, never verified. **Fix:** add the HTML-tag verification to index.html `<head>` (needs the token from GSC, 1 minute once deploy access exists) → unlocks queries/pages/indexing data and sitemap submission. Everything in Phase 3 wants this data.

### P1-4 · Font payload: 162 KB, 12+ variants for a site that uses ~5
- Poppins 300–900 + Inter 300–700 via link, PLUS italics via the duplicate @import. Trim to used weights (audit shows headings 700/800, body 400/500). ~100 KB and 2 requests saved.

## P2 — hygiene

| # | Finding | Where | Fix |
|---|---|---|---|
| P2-1 | `/index.html` serves 200 (duplicate of `/`) | live check | Optional 301 to `/`; canonical already mitigates |
| P2-2 | Repo contains unreferenced 2.5 MB `images/hero_bg.png` (underscore twin of hero-bg.png) + `Fleet Gallery/hero_bg.jpeg`, `mobile_hero.jpeg` unused | file listing vs references | Delete from repo at next deploy (verify no reference first — flagged in ASSUMPTIONS #8) |
| P2-3 | Footer "Popular Routes" links are keyword anchors pointing at `#cabForm` | index.html:1186-1193 | Phase 3 turns these into real route-page links — do not remove, re-point |
| P2-4 | 29 `<img>` lack width/height attributes | index.html | CLS is fine (CSS sizes them; LH unsized-images passes) — add during Phase 3 template work, not urgent |
| P2-5 | No HSTS / CSP headers | .htaccess | Add `Strict-Transport-Security` after confirming no HTTP subresources; CSP optional at this scale |
| P2-6 | Sitemap `lastmod` stale (2026-03-03) | sitemap.xml | Update when Phase 3 ships; add new pages to sitemap |
| P2-7 | GTM container loads but pushes no conversion events (no tel/WhatsApp/form dataLayer events anywhere in script.js) | script.js | Phase 6e wires this — listed here for completeness |
| P2-8 | Custom cursor + 17 reveal-animation groups add ~185 ms scripting on mobile where the cursor doesn't even exist | script.js:137-168 | Gate cursor code behind `pointer: fine` earlier (it is), consider dropping reveal animations on `saveData`/low-end |

## Clean bill of health (checked, no action)
- robots.txt valid, sitemap present & referenced, canonical correct, no noindex accidents (404.html correctly `noindex`), no orphan pages (single-page site), old WordPress URLs 301 correctly (`/contact/`, `/wp-admin/` → `/` verified live), HTTPS forced, Brotli active on text assets, cache headers sane (1y images / 1mo CSS / 1d HTML), viewport correct, `tel:` links everywhere including a floating call button, tap targets pass, no hreflang needed (no Kannada content yet), DOM size fine (708 nodes), schema present (validation deferred to Phase 4 where it's the deliverable).

---

## Priority order & expected outcome
1. P0-1 preloader (one line) → LCP ~3.5 s
2. P0-3 @import + defer (three lines) → FCP ~2 s
3. P0-2 image/video pipeline (batch job) → LCP ≤ 2.5 s, page ~1.5 MB
4. P1-1/P1-2 .htaccess (two lines) · P1-3 GSC verification (one tag)

All of these are Claude-executable in `/site-optimized/` per ground rule 3 — **blocked only on the deploy method** (HANDOFF, still open) to ship and verify live.

**Deliverables:** this report + [`02_cwv.json`](02_cwv.json) + [`scripts/audit.js`](../scripts/audit.js) (re-runnable; add Phase 3 pages to its URL list as they ship).

**Phase 2 complete. Stopped. Next: Phase 3 (architecture + content build) on your go.**
