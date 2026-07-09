# Review funnel — `/review/`

Scan QR → rate → get a **unique** ready-to-paste Google review (each one is retired after it's copied, so no two customers ever post the same text). 1–3★ are routed to a private WhatsApp to the owner instead of Google.

## Files
```
review/
  index.html            the page (self-contained: HTML+CSS+JS)
  api/
    db.example.php       DB credentials template  -> copy to db.php on server
    next.php             hands out one unused review + marks it 'served'
    copied.php           marks a review 'used' (dead) when copied
    stats.php            pool health (available/served/used)  ?key=...
    setup.php            one-time: creates table + loads reviews  ?key=...  (DELETE after)
    seed_reviews.txt     the review bank (~100; add more lines anytime)
    .htaccess            blocks direct download of the txt/db files
```

## Deploy to Hostinger (once)
1. **Create a MySQL database:** hPanel → Databases → *MySQL Databases* → create DB + user (tick all privileges). Note **DB name, user, password, host** (host is usually `localhost`).
2. **Upload** the whole `review/` folder into `public_html/` (so it lives at `.../review/`).
3. In `review/api/`, **copy `db.example.php` → `db.php`** and fill in the 4 DB values.
4. **Change the secret keys**: `$KEY` in `setup.php` and `stats.php` (pick your own strings).
5. **Load the reviews:** open `https://trishikacarrentalhubli.in/review/api/setup.php?key=YOUR_SETUP_KEY` once — it should print "New reviews added: ~100".
6. **Delete `setup.php`** from the server (important).
7. **Test:** open `https://trishikacarrentalhubli.in/review/` on your phone → tap 5 stars → a review appears → Copy → it opens the Google review page.

## QR code
Point the QR at: **`https://trishikacarrentalhubli.in/review/`**
Print it on seat-back cards / receipts, and (best converting) send it by WhatsApp after each trip.

## Managing the pool
- **Check remaining:** `https://.../review/api/stats.php?key=YOUR_STATS_KEY`
- **Top up when low:** add new lines to `seed_reviews.txt` (format `5|text` or `4|text`), re-upload it + `setup.php`, hit setup.php once (duplicates are skipped automatically), then delete `setup.php` again.
- ~100 reviews = ~100 customers before a top-up. At your review pace that's a long runway.

## Tracking (optional)
The page fires GA4 events (`stars_selected`, `review_copied`, `left_review`, `low_rating`, `feedback_sent`) **if** a gtag/GTM tag is present. To capture them, paste your GA4/GTM snippet into `index.html`'s `<head>`.

## Compliance notes (read once)
- Reviews are written generic + varied + editable on purpose so Google's spam filter doesn't flag them as templated, and so customers can honestly tweak them. The "burn after copy" guarantees no duplicates.
- 1–3★ → private WhatsApp is a rating-protection funnel. It's common but technically against Google's review-gating policy; if you'd rather be fully compliant, change `chooseFlow()` in `index.html` to send everyone to the review path.
- Never offer discounts/incentives for reviews (against Google + FTC; gets reviews stripped).
