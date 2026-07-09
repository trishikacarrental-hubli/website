# /ads/import/ — Google Ads Editor import pack

> **✅ APPLIED & POSTED 2026-07-09 (evening).** This pack was imported into account 983-550-8200 via Google Ads Editor and posted live — **4 campaigns / 10 ad groups / 44 keywords / 10 RSAs / 196 negatives**, all PAUSED, location set to **Hubli-Dharwad** (Editor had defaulted them to US — fixed). Conversion tracking is live and firing. Old "03/22/2026 New Campaign" paused. Account-level assets (callouts/sitelinks/structured snippet) added via the web UI. **Only remaining: Sayed recharges + enables the 4 campaigns.** See `CHANGELOG.md` (2026-07-09 evening) and `HANDOFF.md` §4. The notes below are the original build/import guide, kept for reference.
>
> **Import gotcha learned:** the campaign-level "Make multiple changes" only creates campaigns/ad groups; do ad groups in the **Ad Groups view**, keywords in the **Keywords view**, RSAs in the **Ads view**, negatives in the **Negative keywords view** (each renders the right field mapping). Account-level negatives/callouts pasted via Editor's "Make multiple changes" create a **junk blank campaign** — do those in the web UI instead.

Rebuild of account 983-550-8200 into intent-based campaigns. **Everything is created PAUSED — nothing spends until you review and enable it.**

## ⚠️ Do this FIRST — before importing anything

**Fix conversion tracking (see `ads/tracking_setup.md`).** The account currently optimises toward a leftover test tag. If you import + enable these campaigns before tracking is real, you'll keep flying blind. Order: (1) tracking, (2) import structure below, (3) enable campaigns, (4) after 2–3 weeks of real conversion data, move bidding from Manual CPC → Maximize Conversions.

## Files

| File | What it is |
|---|---|
| `campaigns.csv` | 4 search campaigns + daily budgets + Manual CPC |
| `ad_groups.csv` | 10 ad groups + max CPC |
| `keywords.csv` | 44 keywords, Phrase/Exact only (no broad) |
| `negatives_campaign.csv` | Shared negative list applied to all 4 campaigns (self-drive, apps, jobs, wrong-city, auto-repair) |
| `negatives_adgroup.csv` | Cross-theme negatives so ad groups don't cannibalise each other |
| `rsa.csv` | 1 responsive search ad per ad group (15 headlines, 4 descriptions, H1 pinned) |
| `sitelinks.csv` | 8 sitelinks |
| `callouts.csv` | 10 callouts |
| `structured_snippets.csv` | Service-catalog snippet |
| `ad_group_landing_pages.csv` | The ad group → landing page map (reference) |

## Why 1 RSA per ad group (not 3)

The brief asked for 3 RSAs per ad group. **Deliberately giving you 1 strong RSA each instead.** Google now serves ~1 RSA per ad group and rotates assets *within* it; three near-duplicate RSAs split data, slow learning, and don't beat one well-built RSA with 15 varied headlines. If you later want to A/B a genuinely different angle (e.g. price-led vs trust-led), add a 2nd RSA to the top 1–2 ad groups only. This is a pushback, per your own ground rule.

## Import order in Google Ads Editor

Google Ads Editor's whole-file import can be finicky about headers. **The reliable method is per-section paste** — do it in this order so parents exist before children:

1. **Account** → open account 983-550-8200 in Editor, download latest.
2. **Campaigns**: Campaigns view → *Make multiple changes* → paste rows from `campaigns.csv` (or add the 4 campaigns manually — only 4). Set type = Search, budget, Manual CPC, **Search Network only** (uncheck Display expansion), location = Hubballi + Dharwad (+ radius as you like), language English + Kannada + Hindi.
3. **Ad groups**: Ad Groups view → *Make multiple changes* → paste `ad_groups.csv`.
4. **Keywords**: Keywords view → *Make multiple changes* → paste `keywords.csv`. Confirm the Match Type column mapped (Phrase/Exact).
5. **Negatives (campaign)**: Negative keywords → Campaign-level → paste `negatives_campaign.csv`. *(Alternatively create ONE shared negative list in the web UI named "Trishika Master Negatives" and attach to all 4 — easier to maintain. The CSV duplicates the list per campaign for Editor.)*
6. **Negatives (ad group)**: Negative keywords → Ad-group level → paste `negatives_adgroup.csv`.
7. **Responsive search ads**: Ads view → *Make multiple changes* → paste `rsa.csv`. Verify H1 shows a pin to position 1.
8. **Assets**: Sitelinks / Callouts / Structured snippets → paste the three asset files at **account or campaign** level. Add these manually (not always CSV-pastable):
   - **Call asset**: +91 82175 77849 (enable call reporting → this becomes a conversion source).
   - **Location asset**: link the Google Business Profile (Trishika Car Rental).
   - **Price asset**: per-vehicle from `../../gbp/products.csv` numbers (Sedan from Rs 10/km, etc.).
9. **Check → Post.** Editor's *Check changes* flags any errors before upload. Fix, then Post.

### Header uncertainty (per the brief — flagged, not guessed)
Google Ads Editor occasionally versions these column names. If a paste warns on a header, these are the likely renames to try: `Campaign Daily Budget`↔`Budget`, `Max CPC`↔`Max. CPC`, `Match Type`↔`Type`, `Sitelink Text`↔`Link text`. The **safest fallback** for any file that won't map is to add that layer in the web UI (there are only 4 campaigns / 10 ad groups). A bad import is worse than a manual 10-minute entry.

## Before you enable (checklist)
- [ ] Conversion tracking live and firing on a *real* test call/WhatsApp (tracking_setup.md).
- [ ] Old campaigns (Campaign #1, LEADS 11/04, the two others) **paused** — don't delete yet; keep for reference/rollback.
- [ ] Budgets total ≈ ₹560/day. Confirm the prepaid balance is topped up (Phase 0 flagged it low).
- [ ] Location = Hubballi/Dharwad only; Search Network only; Display expansion OFF.
- [ ] Canonical phone decided (HANDOFF) — the call asset must use the number you actually answer.

## Rollback (if CPL rises or spend runs away)
1. Pause the new campaigns (one click each).
2. Re-enable the old **LEADS 11/04** temporarily (it at least had traffic).
3. Nothing was deleted — the old structure is intact.
4. Diagnose in the search-terms report before re-enabling; check the negative list caught the junk.

## Bidding path (6e)
- **Start: Manual CPC** (these CSVs) — because you have no trustworthy conversion history. Max CPCs are pre-set from the data (~₹22–25 core).
- **After ~2–3 weeks AND ≥15 real tracked conversions:** switch each campaign to **Maximize Conversions** (no tCPA yet).
- **After ~30–50 conversions/month sustained:** add a **Target CPA**, starting loose (e.g. ₹400–500, near the airport/best-term CPAs) and tightening slowly.
- **Do NOT** jump to tCPA/PMax on thin data — it optimises noise. (Diagnosis §PMax.)
