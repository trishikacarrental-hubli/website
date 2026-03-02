/* ============================================================
   TRISHIKA CAR RENTAL — script.js
   Hero: GSAP timeline
   Scroll reveals: Native IntersectionObserver (100% mobile safe)
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ====================================================
     INTERSECTION OBSERVER REVEAL SETUP
     Elements stay fully visible by default (no opacity:0 in CSS).
     JS adds .will-reveal class (makes them invisible), then
     IntersectionObserver adds .revealed to animate them in.
  ==================================================== */

  // Define which elements to animate on scroll and their delays
  var revealGroups = [
    { selector: '.tag', delay: 0, transform: 'translateX(-20px)' },
    { selector: '.body-heading', delay: 0.05, transform: 'translateY(30px)' },
    { selector: '.display-heading', delay: 0.05, transform: 'translateY(30px)' },
    { selector: '.booking-context', delay: 0, transform: 'translateX(-40px)' },
    { selector: '.form-wrap', delay: 0.1, transform: 'translateX(40px)' },
    { selector: '.contact-row', delay: 0, transform: 'translateY(18px)', stagger: true },
    { selector: '.fleet-card', delay: 0, transform: 'translateY(40px)', stagger: true },
    { selector: '.fleet-cta-card', delay: 0.2, transform: 'translateY(30px)' },
    { selector: '.est-panel', delay: 0, transform: 'translateY(36px)', stagger: true },
    { selector: '.svc-card', delay: 0, transform: 'translateY(38px)', stagger: true },
    { selector: '.route-row', delay: 0, transform: 'translateX(-30px)', stagger: true },
    { selector: '.why-card', delay: 0, transform: 'translateY(36px)', stagger: true },
    { selector: '.faq-left', delay: 0, transform: 'translateX(-36px)' },
    { selector: '.faq-item', delay: 0, transform: 'translateY(24px)', stagger: true },
    { selector: '.map-info', delay: 0, transform: 'translateX(-36px)' },
    { selector: '.map-embed', delay: 0.1, transform: 'translateY(20px)' },
    { selector: '.footer-top > div', delay: 0, transform: 'translateY(28px)', stagger: true }
  ];

  // Inject the reveal styles once into <head>
  var revealStyle = document.createElement('style');
  revealStyle.textContent = [
    '.will-reveal {',
    '  opacity: 0;',
    '  transition: opacity 0.65s ease, transform 0.65s cubic-bezier(0.16,1,0.3,1);',
    '}',
    '.revealed {',
    '  opacity: 1 !important;',
    '  transform: none !important;',
    '}'
  ].join('\n');
  document.head.appendChild(revealStyle);

  // Skip elements inside the hero from scroll reveals
  function skipHero(el) {
    return el.closest('#hero') !== null;
  }

  // Apply will-reveal + transform to each element
  function initReveal(el, cfg, staggerIndex) {
    if (skipHero(el)) return;
    el.classList.add('will-reveal');
    el.style.transform = cfg.transform;
    var totalDelay = cfg.delay + (cfg.stagger ? staggerIndex * 0.1 : 0);
    el.dataset.revealDelay = totalDelay;
  }

  // Set up all the elements
  revealGroups.forEach(function (cfg) {
    var els = document.querySelectorAll(cfg.selector);
    els.forEach(function (el, i) { initReveal(el, cfg, i); });
  });

  // Single IntersectionObserver for all
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        var el = entry.target;
        var delay = parseFloat(el.dataset.revealDelay || 0);
        setTimeout(function () {
          el.classList.add('revealed');
        }, delay * 1000);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

  // Observe every will-reveal element
  document.querySelectorAll('.will-reveal').forEach(function (el) {
    observer.observe(el);
  });

  /* ====================================================
     GSAP — HERO ENTRANCE ONLY
  ==================================================== */
  if (typeof gsap !== 'undefined') {
    var heroTl = gsap.timeline({ defaults: { ease: 'power3.out' } });
    heroTl
      .from('.eyebrow-line', { scaleX: 0, transformOrigin: 'left', duration: .7, delay: .15 })
      .from('.eyebrow-text', { opacity: 0, x: -16, duration: .5 }, '-=.35')
      .from('.hero-h1', { opacity: 0, y: 40, duration: .85 }, '-=.3')
      .from('.hero-desc', { opacity: 0, y: 24, duration: .6 }, '-=.5')
      .from('.hero-actions .btn', { opacity: 0, y: 18, duration: .5, stagger: .12 }, '-=.4')
      .from('.hero-stat', { opacity: 0, x: 36, duration: .55, stagger: .1 }, '-=.7')
      .from('.hero-scroll', { opacity: 0, y: 12, duration: .45 }, '-=.3');

    // Parallax hero bg (desktop only for perf)
    if (typeof ScrollTrigger !== 'undefined' && window.innerWidth > 768) {
      gsap.registerPlugin(ScrollTrigger);
      gsap.to('.hero-bg', {
        yPercent: 18, ease: 'none',
        scrollTrigger: { trigger: '#hero', start: 'top top', end: 'bottom top', scrub: true }
      });
    }

    // Float button spring entrance
    gsap.fromTo('.float-call, .float-call-pulse',
      { scale: 0, opacity: 0 },
      { scale: 1, opacity: 1, duration: .6, ease: 'back.out(1.8)', delay: 1.4 }
    );
  }

  /* ====================================================
     CUSTOM CURSOR (desktop only)
  ==================================================== */
  var cursorDot = document.getElementById('cursorDot');
  var cursorRing = document.getElementById('cursorRing');
  if (cursorDot && cursorRing && window.matchMedia('(pointer: fine)').matches) {
    var mouseX = 0, mouseY = 0, ringX = 0, ringY = 0;
    document.addEventListener('mousemove', function (e) {
      mouseX = e.clientX; mouseY = e.clientY;
      cursorDot.style.left = mouseX + 'px';
      cursorDot.style.top = mouseY + 'px';
    });
    (function animateRing() {
      ringX += (mouseX - ringX) * 0.11;
      ringY += (mouseY - ringY) * 0.11;
      cursorRing.style.left = ringX + 'px';
      cursorRing.style.top = ringY + 'px';
      requestAnimationFrame(animateRing);
    })();
    document.querySelectorAll('a, button, select, input').forEach(function (el) {
      el.addEventListener('mouseenter', function () {
        cursorRing.style.width = '48px'; cursorRing.style.height = '48px'; cursorRing.style.opacity = '1';
        cursorDot.style.transform = 'translate(-50%,-50%) scale(0)';
      });
      el.addEventListener('mouseleave', function () {
        cursorRing.style.width = '32px'; cursorRing.style.height = '32px'; cursorRing.style.opacity = '.6';
        cursorDot.style.transform = 'translate(-50%,-50%) scale(1)';
      });
    });
  } else {
    // Hide cursor elements on touch devices
    if (cursorDot) cursorDot.style.display = 'none';
    if (cursorRing) cursorRing.style.display = 'none';
    document.body.style.cursor = 'auto';
  }

  /* ====================================================
     STICKY HEADER
  ==================================================== */
  var header = document.getElementById('siteHeader');
  if (header) {
    window.addEventListener('scroll', function () {
      header.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });
    // Trigger once on load in case page starts scrolled
    header.classList.toggle('scrolled', window.scrollY > 40);
  }

  /* ====================================================
     HAMBURGER MENU
  ==================================================== */
  var hamburger = document.getElementById('hamburger');
  var mobileMenu = document.getElementById('mobileMenu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function () {
      var isOpen = mobileMenu.classList.toggle('open');
      hamburger.classList.toggle('open', isOpen);
      hamburger.setAttribute('aria-expanded', isOpen);
    });
    mobileMenu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('open');
        hamburger.setAttribute('aria-expanded', false);
      });
    });
  }

  /* ====================================================
     FAQ ACCORDION
  ==================================================== */
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.parentElement;
      var wasOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(function (i) {
        i.classList.remove('open');
        i.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
      });
      if (!wasOpen) {
        item.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ====================================================
     ROUTE FILTER
  ==================================================== */
  document.querySelectorAll('.filter-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      document.querySelectorAll('.filter-btn').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var filter = btn.dataset.filter;
      document.querySelectorAll('.route-row').forEach(function (row) {
        var cats = row.dataset.cat || '';
        if (filter === 'all' || cats.indexOf(filter) !== -1) {
          row.classList.remove('hidden-route');
        } else {
          row.classList.add('hidden-route');
        }
      });
    });
  });

  /* ====================================================
     BOOKING FORM → WHATSAPP
  ==================================================== */
  var cabForm = document.getElementById('cabForm');
  if (cabForm) {
    cabForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = document.getElementById('fName').value.trim();
      var phone = document.getElementById('fPhone').value.trim();
      var pickup = document.getElementById('fPickup').value.trim();
      var drop = document.getElementById('fDrop').value.trim();
      var vehicle = document.getElementById('fVehicle').value;
      var date = document.getElementById('fDate').value;
      if (!name || !phone || !pickup || !drop || !vehicle || !date) {
        alert('Please fill all fields before submitting.');
        return;
      }
      var msg = encodeURIComponent(
        'Cab Booking Request \u2013 Trishika Car Rental\n' +
        'Name: ' + name + '\n' +
        'Phone: ' + phone + '\n' +
        'Pickup: ' + pickup + '\n' +
        'Drop: ' + drop + '\n' +
        'Vehicle: ' + vehicle + '\n' +
        'Date: ' + date
      );
      window.open('https://wa.me/918217577849?text=' + msg, '_blank');
      var success = document.getElementById('formSuccess');
      if (success) success.style.display = 'block';
    });
  }

  /* ====================================================
     RATE ESTIMATOR
  ==================================================== */
  var DATA = [
    { name: 'Swift Dzire', seats: '4+1', rate: { ac: 12, nonac: 10 }, local: { available: true, rate: { ac: 12, nonac: 10 } }, dayDuty: 300 },
    { name: 'Toyota Etios', seats: '4+1', rate: { ac: 12, nonac: 10 }, local: { available: true, rate: { ac: 12, nonac: 10 } }, dayDuty: 300 },
    { name: 'Maruti Ertiga', seats: '6-7+1', rate: { ac: 16, nonac: 14 }, local: { available: true, rate: { ac: 16, nonac: 14 } }, dayDuty: 350 },
    { name: 'Toyota Innova', seats: '7+1', rate: { ac: 18, nonac: 16 }, local: { available: true, rate: { ac: 18, nonac: 16 } }, dayDuty: 400 },
    { name: 'Innova Crysta', seats: '7+1', rate: { ac: 20, nonac: 18 }, local: { available: true, rate: { ac: 20, nonac: 18 } }, dayDuty: 400 },
    { name: 'Tempo Traveller', seats: '12-17+1', rate: { ac: 19, nonac: 17 }, local: { available: false }, dayDuty: 500 },
    { name: 'Mini Bus', seats: '21-25+1', rate: { ac: 28, nonac: 25 }, local: { available: false }, dayDuty: 600 }
  ];
  var MIN_KM = 300;
  var isOutstation = true;
  var isAC = true;

  function fmt(n) { return '\u20b9' + n.toLocaleString('en-IN'); }
  function getVeh() {
    var sel = document.getElementById('estVeh');
    if (!sel) return DATA[0];
    return DATA.find(function (d) { return d.name === sel.value; }) || DATA[0];
  }

  function setTrip(out) {
    isOutstation = out;
    var btnOut = document.getElementById('tripOut');
    var btnLocal = document.getElementById('tripLocal');
    var kmCtl = document.getElementById('kmCtl');
    var hrsCtl = document.getElementById('hrsCtl');
    var daysCtl = document.getElementById('daysCtl');
    if (btnOut) btnOut.setAttribute('aria-pressed', out ? 'true' : 'false');
    if (btnLocal) btnLocal.setAttribute('aria-pressed', out ? 'false' : 'true');
    if (kmCtl) kmCtl.classList.toggle('hidden', !out);
    if (hrsCtl) hrsCtl.classList.toggle('hidden', out);
    if (daysCtl) daysCtl.style.display = out ? '' : 'none';
    var sel = document.getElementById('estVeh');
    if (sel) {
      Array.from(sel.options).forEach(function (opt) {
        var v = DATA.find(function (x) { return x.name === opt.value; });
        opt.disabled = (!out && v && v.local.available === false);
      });
      if (sel.options[sel.selectedIndex] && sel.options[sel.selectedIndex].disabled) {
        var en = Array.from(sel.options).find(function (o) { return !o.disabled; });
        if (en) sel.value = en.value;
      }
    }
    calc();
  }

  function setAC(ac) {
    isAC = ac;
    var btnYes = document.getElementById('acYes');
    var btnNo = document.getElementById('acNo');
    if (btnYes) btnYes.setAttribute('aria-pressed', ac ? 'true' : 'false');
    if (btnNo) btnNo.setAttribute('aria-pressed', ac ? 'false' : 'true');
    calc();
  }

  function calc() {
    var v = getVeh();
    var rate = isAC ? v.rate.ac : v.rate.nonac;
    var duty = v.dayDuty || 300;

    var ids = ['sVeh', 'sRate', 'sEnteredLbl', 'sEntered', 'sMinLbl', 'sMin', 'sBaseLbl', 'sBase', 'sExtraCharge', 'sDayLbl', 'sDay', 'sTotal'];
    var els = {};
    ids.forEach(function (id) { els[id] = document.getElementById(id); });

    if (isOutstation) {
      var kmInput = document.getElementById('estKm');
      var daysInput = document.getElementById('estDays');
      var entKm = Math.max(0, Number((kmInput && kmInput.value) || 0));
      var days = Math.max(1, Number((daysInput && daysInput.value) || 1));
      var baseFare = MIN_KM * rate;
      var extraKm = Math.max(0, entKm - MIN_KM);
      var extraChg = extraKm * rate;
      var dayDuty = days * duty;
      var total = baseFare + extraChg + dayDuty;

      if (els.sVeh) els.sVeh.textContent = v.name + ' (' + v.seats + ') ' + (isAC ? 'AC' : 'Non-AC');
      if (els.sRate) els.sRate.textContent = '\u20b9' + rate + '/km';
      if (els.sEnteredLbl) els.sEnteredLbl.textContent = 'Entered distance';
      if (els.sEntered) els.sEntered.textContent = (entKm || 0) + ' km';
      if (els.sMinLbl) els.sMinLbl.textContent = 'Minimum billed';
      if (els.sMin) els.sMin.textContent = MIN_KM + ' km';
      if (els.sBaseLbl) els.sBaseLbl.textContent = 'Base fare (' + MIN_KM + '\u00d7\u20b9' + rate + ')';
      if (els.sBase) els.sBase.textContent = fmt(baseFare);
      if (els.sExtraCharge) els.sExtraCharge.textContent = fmt(extraChg);
      if (els.sDayLbl) els.sDayLbl.textContent = 'Driver duty (' + days + ' day' + (days > 1 ? 's' : '') + ')';
      if (els.sDay) els.sDay.textContent = fmt(dayDuty);
      if (els.sTotal) els.sTotal.textContent = fmt(total);

      var waBtn = document.getElementById('waEstBtn');
      if (waBtn) {
        var km = entKm || MIN_KM;
        waBtn.href = 'https://wa.me/918217577849?text=' + encodeURIComponent(
          'Outstation estimate \u2013 Trishika Car Rental\nVehicle: ' + v.name + ' (' + v.seats + ') ' + (isAC ? 'AC' : 'Non-AC') +
          '\nDistance: ' + km + ' km\nRate: \u20b9' + rate + '/km\nBase: ' + fmt(baseFare) +
          '\nExtra km: ' + fmt(extraChg) + '\nDriver duty: ' + fmt(dayDuty) +
          '\nEstimated total: ' + fmt(total) + '\n\nNote: Tolls & parking extra.'
        );
      }
    } else {
      var hrsInput = document.getElementById('estHrs');
      var hrs = Math.max(8, Number((hrsInput && hrsInput.value) || 8));
      var localRate = isAC ? (v.local.rate ? v.local.rate.ac : rate) : (v.local.rate ? v.local.rate.nonac : rate);
      var base = 80 * localRate;
      var hrExtra = hrs > 8 ? (hrs - 8) * 100 : 0;
      var total2 = base + hrExtra;

      if (els.sVeh) els.sVeh.textContent = v.name + ' (' + v.seats + ') ' + (isAC ? 'AC' : 'Non-AC');
      if (els.sRate) els.sRate.textContent = '\u20b9' + localRate + '/km';
      if (els.sEnteredLbl) els.sEnteredLbl.textContent = 'Package';
      if (els.sEntered) els.sEntered.textContent = hrs + ' hrs / 80 km';
      if (els.sMinLbl) els.sMinLbl.textContent = 'Base distance';
      if (els.sMin) els.sMin.textContent = '80 km';
      if (els.sBaseLbl) els.sBaseLbl.textContent = 'Package base fare';
      if (els.sBase) els.sBase.textContent = fmt(base);
      if (els.sExtraCharge) els.sExtraCharge.textContent = hrExtra > 0 ? fmt(hrExtra) : '\u20b90';
      if (els.sDayLbl) els.sDayLbl.textContent = 'Extra hours';
      if (els.sDay) els.sDay.textContent = hrExtra > 0 ? fmt(hrExtra) : 'None';
      if (els.sTotal) els.sTotal.textContent = fmt(total2);

      var waBtn2 = document.getElementById('waEstBtn');
      if (waBtn2) {
        waBtn2.href = 'https://wa.me/918217577849?text=' + encodeURIComponent(
          'Local estimate \u2013 Trishika Car Rental\nVehicle: ' + v.name + ' ' + (isAC ? 'AC' : 'Non-AC') +
          '\nPackage: ' + hrs + ' hrs / 80 km\nEstimated total: ' + fmt(total2) +
          '\n\nNote: Extra km \u20b9' + localRate + '/km. Tolls extra.'
        );
      }
    }
  }

  // Wire estimator controls
  ['tripOut', 'tripLocal', 'acYes', 'acNo'].forEach(function (id) {
    var el = document.getElementById(id);
    if (!el) return;
    if (id === 'tripOut') el.addEventListener('click', function () { setTrip(true); });
    if (id === 'tripLocal') el.addEventListener('click', function () { setTrip(false); });
    if (id === 'acYes') el.addEventListener('click', function () { setAC(true); });
    if (id === 'acNo') el.addEventListener('click', function () { setAC(false); });
  });

  ['estVeh', 'estKm', 'estHrs', 'estDays'].forEach(function (id) {
    var el = document.getElementById(id);
    if (el) { el.addEventListener('input', calc); el.addEventListener('change', calc); }
  });

  var kmChips = document.getElementById('kmChips');
  if (kmChips) {
    kmChips.addEventListener('click', function (e) {
      if (e.target.dataset.km) {
        var kmInput = document.getElementById('estKm');
        if (kmInput) { kmInput.value = e.target.dataset.km; calc(); }
      }
    });
  }
  document.querySelectorAll('[data-hrs]').forEach(function (c) {
    c.addEventListener('click', function () {
      if (c.dataset.hrs) {
        var hrsInput = document.getElementById('estHrs');
        if (hrsInput) { hrsInput.value = c.dataset.hrs; calc(); }
      }
    });
  });

  calc();

}); // end DOMContentLoaded
