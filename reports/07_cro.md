# Phase 7 — Conversion Rate Optimisation

Audited the live pages (homepage + representative route/service pages) against the brief's checklist: time-to-first-CTA, phone prominence, mobile tap targets, form field count, trust signals, fare transparency, 4G load. Fixes are in `/site-optimized/` (need **deploy #3**).

## Scorecard

| Factor | Homepage (before) | Route/service pages | Verdict |
|---|---|---|---|
| Time-to-first-CTA | Call + WhatsApp above the fold ✓ | Call + WhatsApp in hero ✓ | Good |
| Phone prominence | Header (desktop), Call Now button, floating call button ✓ | Call Now button with number, floating button ✓ | Good |
| Mobile tap targets | Buttons ~49px ✓; form inputs ~40px (slightly under 44px ideal) | Buttons ✓ | Minor |
| **Form field count** | **6 required fields** ❌ | n/a (CTA-led) | **Fixed** |
| **Trust signals** | **No star rating shown** ❌ — the 5.0★/58 asset was absent from the top page | Trust chips incl. "5.0 on Google (58)" ✓ | **Fixed** |
| Fare transparency | Pricing section + live rate estimator ✓ | Fare tables + sample costing ✓ | Excellent |
| 4G load | 909 KiB (Phase 2) ✓ | Lightweight ✓ | Good |

**The core finding:** the highest-traffic page was the *weakest* on trust and had the *most* form friction — the opposite of what you want. The route/service pages I built in Phase 3 were already CRO-solid; the homepage lagged them.

## Fixes applied (in `/site-optimized/`)

### P0-1 · Added Google rating social proof to the hero
- **What:** a gold-star pill "★★★★★ 5.0 · 58 Google reviews", linking to the review page, placed immediately *above* the Call/WhatsApp buttons.
- **Why:** social proof right before the CTA is one of the highest-leverage CRO moves, and you have a genuine 5.0★/58 — it was simply not on the page. Verified rendering on mobile + desktop.
- Files: `index.html` (hero), `style.css` (`.hero-rating`).

### P0-2 · H1 now rental-first
- **What:** "Reliable Taxi Service Hubli" → **"Car Rental & Taxi Hubli"**.
- **Why:** headline-to-intent relevance. Rental-language demand is 2:1 over taxi (Phase 1) and the paid landing pages now match the ads. Keeps "Taxi" so nothing is lost. Aligns with the already-live rental-first title tag.

### P1-1 · Cut the booking form from 6 required fields to 4
- **What:** Vehicle Type and Travel Date are now **optional** (labelled "(optional)"); only Name, Phone, Pickup, Drop are required. The WhatsApp message still includes vehicle/date when provided.
- **Why:** every extra required field drops completion. For a WhatsApp-handoff form, name + phone + route is enough to start the conversation; the rest gets sorted in chat. Note: Call/WhatsApp remain the *primary* CTAs (above the form) — the form is the fallback, per the brief's "no forms as primary CTA" rule.
- Files: `index.html` (form), `script.js` (validation + message), `ads/import/track-conversions.js` (mirror validation for the `form_submit_whatsapp` event).

## Recommendations that need your input (not yet applied)
- **Real vehicle count & years in business:** the hero mini-stat says "6+ Vehicles" — confirm the true number, and add "X years in Hubli" as a trust stat (age is a strong local trust signal). Give me the numbers and I'll wire them in.
- **"No advance payment" badge** — if true, this is a top-3 CRO signal for Indian cab booking (kills the "will I be scammed" hesitation). Confirm and I'll add it to the hero + route pages. (Still open in HANDOFF.)
- **Respond to the 3 unread GBP reviews + add fresh photos** — off-site but directly affects the click-through from the map pack to these pages.

## Deliberately NOT changed (would cost more than they'd gain)
- Form input height ~40px vs 44px ideal — a 4px bump; negligible impact, skipped to avoid touching the form grid rhythm. Can add later.
- Custom cursor (`cursor: none` on desktop) — a brand choice; pointer-fine gated, doesn't affect mobile conversions.
- No sticky mobile call bar added — the floating call button already covers persistent phone access.

## Verification
Preview-tested at mobile (375px) and desktop: rating pill renders (gold stars, styled pill), H1 reads rental-first, form reports `required=false` on Vehicle/Date and `required=true` on Name, 2 "(optional)" labels present, zero console errors. Ready for deploy #3 (index.html, style.css, script.js) + the tracking snippet.

**Phase 7 complete. Stopped.** Next: Phase 8 (measurement metrics, weekly/monthly cadence, a report script, the 90-day expectation curve).
