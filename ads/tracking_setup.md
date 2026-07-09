# Phase 6e — Conversion tracking rebuild (do this BEFORE enabling ads)

## ✅ DONE 2026-07-09 — GTM container v9 PUBLISHED LIVE
The GTM build below is complete and live (container **GTM-P92G7GNP**, Version 9):
- 3 Custom Event triggers: `call_click`, `whatsapp_click`, `form_submit_whatsapp`.
- One Google Ads Conversion tag **`Google Ads - Contact (Call/WhatsApp/Form)`** — ID `17442020753`, Label `_imzCNTi_MwcEJG7gP1A` — firing on all 3 CE triggers.
- Base Google tag `AW-17442020753` added; broken broad `btn` conversion tag deleted.

**⚠️ RISK — FortuneMarq Automator auto-publishes this container** (it did v4–v8, each time recreating the broken btn tag). It may overwrite v9 and revert to broken tracking. Sayed must disable/reconfigure it. See RISKS.md.

**Remaining (Google Ads dashboard, not GTM):** deactivate `V2_Auto_Success_Test`; set "Contact – Call & WhatsApp" as the primary conversion; then verify a real click records a conversion (may take hours).

Note: no GA4 was used — went GTM → Google Ads conversion tag directly (see revised approach below). The GA4-based steps (C/D) are therefore OPTIONAL/superseded.

## ✅ UPDATE 2026-07-09 (evening) — direct gtag fire added as a GTM-independent backup + verified live
Because the FortuneMarq Automator keeps clobbering GTM, `track-conversions.js` now fires the conversion **directly** (not only via the GTM dataLayer path): it runs `gtag('config','AW-17442020753')` and, on every `tel:`/`wa.me` click, `gtag('event','conversion',{send_to:'AW-17442020753/_imzCNTi_MwcEJG7gP1A', value:150, currency:'INR'})`.
- **Verified on production:** a real Call click fired `googleadservices.com/pagead/conversion/17442020753/?…&label=_imzCNTi_MwcEJG7gP1A&en=conversion`.
- `track-conversions.js` is now served `no-cache` (was inheriting a multi-week JS cache) so tracking changes propagate immediately.
- **⚠️ Double-fire:** with GTM v9 also firing this conversion on the same clicks, the beacon now fires twice — but the action's **count = "One" per ad click de-dups to 1 conversion**, so no inflation. Once the Automator is disabled, consolidate to ONE path (keep the direct gtag fire; remove the GTM conversion tag). The `V2_Auto_Success_Test` action was already removed; "Contact – Call & WhatsApp" is the sole action + account-default goal.

## ⚡ GTM container state — inspected live 2026-07-09

Opened container **GTM-P92G7GNP** (the one on the site). Findings that change the plan:
- **No GA4 anywhere** — no GA4 Configuration tag, no GA4 event tags. (A second unused container GTM-NBBBTT3N also exists; ignore it.)
- Existing tags: **Conversion Linker** (All Pages — good) + **Google Ads Conversion Tracking** tag (Conversion ID `17442020753`, Label `FbU7CNHC1oIcEJG7gP1A`).
- ⚠️ That Ads-conversion tag is **UNSUBMITTED** (part of 4 pending workspace changes, not ours), **fires on ANY element with class `btn`** ("Conversion (Click Class) - btn") — i.e. every button click = a conversion (garbage data) — and shows **"No Google tag found in this container"** (missing the base gtag it needs). It is half-built and must NOT be shipped as-is.
- **4 uncommitted workspace changes exist** (2 added / 2 deleted). Submitting the container would publish them too — must reconcile first.

### Conversion actions created in Google Ads (2026-07-09)
- **Contact – Call & WhatsApp** — Website, Manual (GTM), **Primary**, count One, value ₹150, 90-day window, data-driven attribution.
  - **Conversion ID: `AW-17442020753`** · **Label: `_imzCNTi_MwcEJG7gP1A`**
  - This single "Contact" action is fired by ALL THREE website events (call_click, whatsapp_click, form_submit_whatsapp) — on this site the booking form just opens WhatsApp, so all three are genuinely "contact" actions.
- (Old test tag `V2_Auto_Success_Test` still to be deactivated.)

### Revised approach (no GA4 required)
Because there's already a Google Ads conversion tag type in use, the clean path is **GTM → Google Ads conversion tags directly**, no GA4 needed:
1. In Google Ads, create proper conversion actions: **Calls from ads** (call asset), **WhatsApp click**, **Form submit** — each yields a Conversion ID + Label.
2. In GTM: add the **Google tag (gtag) base** once; create 3 **Custom Event triggers** (`call_click`, `whatsapp_click`, `form_submit_whatsapp`); create 3 **Google Ads Conversion Tracking tags**, each firing on its precise trigger (NOT the broad `btn` class).
3. **Fix/replace the existing broad `btn` conversion tag** so it doesn't count every button click.
4. Reconcile the 4 pending workspace changes, then **Submit** the container.
5. In Google Ads, deactivate `V2_Auto_Success_Test`; set the new actions as primary.
*(Optional later: add GA4 for analytics depth — not required for ad-conversion tracking.)*

> ⚠️ Submitting the container changes LIVE conversion measurement (and thus ad bidding). Because it's hard to reverse and tangled with someone's pending changes + a broken broad tag, this step needs a green light + the conversion-action decisions before publishing.

---


**Why this is first:** the account's only firing conversion is a test tag; the real lead action is inactive. Every optimisation decision is blind until this works. This business converts on **phone calls and WhatsApp**, not form fills — so if you only track the form (as today), you're measuring the smallest slice of reality. Track calls + WhatsApp first.

## The 4 conversion actions to configure in Google Ads
(Tools → Conversions → New conversion action)

| # | Conversion action | Type | Source | Value | Count | Primary? |
|---|---|---|---|---|---|---|
| 1 | **Calls from ads** | Phone calls → Calls from ads using call asset | Google forwarding number | ₹150 (est. lead value) | One | ✅ Primary |
| 2 | **Calls to website number (≥45s)** | Phone calls → Calls to a number on your website | Google (needs the site to swap the number for a forwarding number — see note) | ₹150 | One | ✅ Primary |
| 3 | **WhatsApp click** | Website → import from GA4 key event `whatsapp_click` (see GTM below) | GA4 | ₹120 | One | ✅ Primary |
| 4 | **Booking form submit (WhatsApp handoff)** | Website → GA4 key event `form_submit_whatsapp` | GA4 | ₹120 | One | Secondary |

- Deactivate/delete `V2_Auto_Success_Test`. Fix or delete the inactive `Submit lead form`.
- Set **conversion goal grouping** so bidding uses the primaries above (not the test tag).
- Values are estimates so smart bidding can weigh actions later; adjust once you know a lead's real worth. If unknown, set all = 1 and rank by count.

## The website events (GTM `GTM-P92G7GNP` is already installed)

**Step A — add the snippet.** `track-conversions.js` (in this folder) pushes clean dataLayer events on every tel: click, WhatsApp click, and booking-form submit. Add it to the site `<head>`/before `</body>` (one line), then deploy. It's framework-free and safe to include site-wide:

```html
<script src="/track-conversions.js" defer></script>
```

*(For the current site, the booking form already opens WhatsApp in `script.js`; the snippet also catches that via the submit listener — no double count because it keys off the form id.)*

**Step B — in GTM, create 3 triggers** (Custom Event, event name equals):
- `call_click` · `whatsapp_click` · `form_submit_whatsapp`

**Step C — create GA4 event tags** (GA4 Configuration tag must already exist; if not, add one with your Measurement ID `G-XXXXXXX`):
- Tag: GA4 Event `call_click` → mark as **Key event** in GA4.
- Tag: GA4 Event `whatsapp_click` → Key event.
- Tag: GA4 Event `form_submit_whatsapp` → Key event.

**Step D — bring them into Google Ads:**
- Easiest: link GA4 ↔ Google Ads, then **import** the three GA4 key events as conversions (actions #3/#4 above + optionally call_click if you don't use call assets).
- Calls (#1/#2) come from Google Ads' own call reporting + call asset — enable "Include in Conversions".

**Step E — website call tracking (#2):** requires Google's number-swap snippet (`google_trackConversion` / the call-tracking JS from the conversion action wizard) which replaces the displayed number with a forwarding number and counts calls ≥45s. Add whatever snippet the wizard generates to the site. *If you'd rather not swap the number on the site, skip #2 and rely on #1 (calls from ads) + #3 (WhatsApp) — still miles better than today.*

## Verify before trusting it
1. GTM Preview mode → click Call, click WhatsApp, submit the form → confirm all 3 dataLayer events fire.
2. GA4 Realtime → confirm the 3 events appear.
3. Google Ads → Conversions → the actions show status "Recording conversions" (may take a few hours + a real click).
4. Only then enable the new campaigns.

## Then, and only then
Move bidding Manual CPC → Maximize Conversions after ~2–3 weeks of *real* data (README bidding path).
