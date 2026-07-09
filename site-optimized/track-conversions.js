/* Trishika Car Rental — conversion event tracking (GTM dataLayer)
   Framework-free. Pushes: call_click, whatsapp_click, form_submit_whatsapp.
   Deploy to site root and load with: <script src="/track-conversions.js" defer></script>
   Works alongside GTM-P92G7GNP (already on the site). */

/* GA4 (gtag.js) — property G-DCRPBD1L2J. Loaded here so every page that
   includes this script gets Analytics, without editing each page's <head>. */
(function () {
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=G-DCRPBD1L2J';
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', 'G-DCRPBD1L2J');
  /* Google Ads (AW-17442020753) — registers the Ads tag so conversions fire and
     the conversion linker works. Same gtag.js instance handles GA4 + Ads. */
  window.gtag('config', 'AW-17442020753');
})();

(function () {
  window.dataLayer = window.dataLayer || [];
  function push(event, detail) {
    window.dataLayer.push(Object.assign({ event: event }, detail || {}));
  }

  /* Google Ads conversion — "Contact – Call & WhatsApp"
     (send_to: AW-17442020753/_imzCNTi_MwcEJG7gP1A). Fires on any Call or WhatsApp
     click. The action counts "one" per ad click, so repeated taps don't inflate.
     Value ₹150 is sent explicitly (matches the action's per-lead value) so the
     beacon never records a zero-value conversion. */
  function adsContactConversion() {
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'conversion', {
        send_to: 'AW-17442020753/_imzCNTi_MwcEJG7gP1A',
        value: 150.0,
        currency: 'INR'
      });
    }
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a');
    if (!a) return;
    var href = (a.getAttribute('href') || '').toLowerCase();
    if (href.indexOf('tel:') === 0) {
      push('call_click', { link_url: href, link_text: (a.textContent || '').trim().slice(0, 60) });
      adsContactConversion();
    } else if (href.indexOf('wa.me') !== -1 || href.indexOf('whatsapp') !== -1 || href.indexOf('api.whatsapp') !== -1) {
      push('whatsapp_click', { link_url: href, link_text: (a.textContent || '').trim().slice(0, 60) });
      adsContactConversion();
    }
  }, true);

  // Booking form → opens WhatsApp in script.js. Fire once per successful submit.
  var form = document.getElementById('cabForm');
  if (form) {
    form.addEventListener('submit', function () {
      // script.js validates + opens WhatsApp; mirror the same required-field check (4 core fields) to avoid counting empties
      var ids = ['fName', 'fPhone', 'fPickup', 'fDrop'];
      var ok = ids.every(function (id) { var el = document.getElementById(id); return el && el.value.trim(); });
      if (ok) push('form_submit_whatsapp', { form_id: 'cabForm' });
    });
  }
})();
