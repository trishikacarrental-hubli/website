/* ============================================================
   TRISHIKA CAR RENTAL — script.js
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ===== CUSTOM CURSOR ===== */
  const cursorDot  = document.getElementById('cursorDot');
  const cursorRing = document.getElementById('cursorRing');

  if (cursorDot && cursorRing) {
    let mouseX = 0, mouseY = 0;
    let ringX  = 0, ringY  = 0;

    document.addEventListener('mousemove', function (e) {
      mouseX = e.clientX;
      mouseY = e.clientY;
      cursorDot.style.left = mouseX + 'px';
      cursorDot.style.top  = mouseY + 'px';
    });

    function animateRing() {
      ringX += (mouseX - ringX) * 0.12;
      ringY += (mouseY - ringY) * 0.12;
      cursorRing.style.left = ringX + 'px';
      cursorRing.style.top  = ringY + 'px';
      requestAnimationFrame(animateRing);
    }
    animateRing();

    document.querySelectorAll('a, button').forEach(function (el) {
      el.addEventListener('mouseenter', function () {
        cursorRing.style.transform = 'translate(-50%, -50%) scale(1.8)';
        cursorRing.style.borderColor = '#E05500';
        cursorRing.style.opacity = '1';
        cursorDot.style.transform = 'translate(-50%, -50%) scale(0.5)';
      });
      el.addEventListener('mouseleave', function () {
        cursorRing.style.transform = 'translate(-50%, -50%) scale(1)';
        cursorRing.style.borderColor = '#E05500';
        cursorRing.style.opacity = '0.6';
        cursorDot.style.transform = 'translate(-50%, -50%) scale(1)';
      });
    });
  }

  /* ===== STICKY HEADER ===== */
  const header = document.getElementById('siteHeader');
  if (header) {
    window.addEventListener('scroll', function () {
      header.classList.toggle('scrolled', window.scrollY > 30);
    });
  }

  /* ===== HAMBURGER MENU ===== */
  const hamburger  = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function () {
      const isOpen = mobileMenu.classList.toggle('open');
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

  /* ===== SCROLL REVEAL ===== */
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    const revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    reveals.forEach(function (el) { revealObserver.observe(el); });
  }

  /* ===== FAQ ACCORDION ===== */
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const item = btn.parentElement;
      const wasOpen = item.classList.contains('open');
      // close all
      document.querySelectorAll('.faq-item').forEach(function (i) {
        i.classList.remove('open');
        i.querySelector('.faq-q').setAttribute('aria-expanded', false);
      });
      // toggle this one
      if (!wasOpen) {
        item.classList.add('open');
        btn.setAttribute('aria-expanded', true);
      }
    });
  });

  /* ===== ROUTE FILTER ===== */
  document.querySelectorAll('.filter-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      document.querySelectorAll('.filter-btn').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      const filter = btn.dataset.filter;
      document.querySelectorAll('.route-row').forEach(function (row) {
        const cats = row.dataset.cat || '';
        if (filter === 'all' || cats.indexOf(filter) !== -1) {
          row.classList.remove('hidden-route');
        } else {
          row.classList.add('hidden-route');
        }
      });
    });
  });

  /* ===== BOOKING FORM → WHATSAPP ===== */
  const cabForm = document.getElementById('cabForm');
  if (cabForm) {
    cabForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const name    = document.getElementById('fName').value.trim();
      const phone   = document.getElementById('fPhone').value.trim();
      const pickup  = document.getElementById('fPickup').value.trim();
      const drop    = document.getElementById('fDrop').value.trim();
      const vehicle = document.getElementById('fVehicle').value;
      const date    = document.getElementById('fDate').value;
      if (!name || !phone || !pickup || !drop || !vehicle || !date) {
        alert('Please fill all fields before submitting.');
        return;
      }
      var msg = encodeURIComponent(
        'Cab Booking Request – Trishika Car Rental\n' +
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

  /* ===== RATE ESTIMATOR ===== */
  var DATA = [
    { name:'Swift Dzire',    seats:'4+1',    rate:{ ac:12, nonac:10 }, local:{ available:true,  rate:{ ac:12,  nonac:10 } } },
    { name:'Toyota Etios',   seats:'4+1',    rate:{ ac:12, nonac:10 }, local:{ available:true,  rate:{ ac:12,  nonac:10 } } },
    { name:'Maruti Ertiga',  seats:'6-7+1',  rate:{ ac:16, nonac:14 }, local:{ available:true,  rate:{ ac:16,  nonac:14 } } },
    { name:'Toyota Innova',  seats:'7+1',    rate:{ ac:18, nonac:16 }, local:{ available:true,  rate:{ ac:18,  nonac:16 } } },
    { name:'Innova Crysta',  seats:'7+1',    rate:{ ac:20, nonac:18 }, local:{ available:true,  rate:{ ac:20,  nonac:18 } } },
    { name:'Tempo Traveller',seats:'12-17+1',rate:{ ac:19, nonac:17 }, local:{ available:false } },
    { name:'Mini Bus',       seats:'21-25+1',rate:{ ac:28, nonac:25 }, local:{ available:false } }
  ];
  var MIN_KM   = 300;
  var DAY_DUTY = 300;
  var isOutstation = true;
  var isAC         = true;

  function fmt(n) {
    return '₹' + n.toLocaleString('en-IN');
  }
  function getVeh() {
    var sel = document.getElementById('estVeh');
    if (!sel) return DATA[0];
    return DATA.find(function (d) { return d.name === sel.value; }) || DATA[0];
  }

  function setTrip(out) {
    isOutstation = out;
    var btnOut   = document.getElementById('tripOut');
    var btnLocal = document.getElementById('tripLocal');
    var kmCtl    = document.getElementById('kmCtl');
    var hrsCtl   = document.getElementById('hrsCtl');
    var daysCtl  = document.getElementById('daysCtl');
    if (btnOut)   btnOut.setAttribute('aria-pressed', out ? 'true' : 'false');
    if (btnLocal) btnLocal.setAttribute('aria-pressed', out ? 'false' : 'true');
    if (kmCtl)    kmCtl.classList.toggle('hidden', !out);
    if (hrsCtl)   hrsCtl.classList.toggle('hidden', out);
    if (daysCtl)  daysCtl.style.display = out ? '' : 'none';

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
    var btnNo  = document.getElementById('acNo');
    if (btnYes) btnYes.setAttribute('aria-pressed', ac ? 'true' : 'false');
    if (btnNo)  btnNo.setAttribute('aria-pressed', ac ? 'false' : 'true');
    calc();
  }

  function calc() {
    var v    = getVeh();
    var rate = isAC ? v.rate.ac : v.rate.nonac;

    var sVeh  = document.getElementById('sVeh');
    var sRate = document.getElementById('sRate');
    var sElbl = document.getElementById('sEnteredLbl');
    var sEnt  = document.getElementById('sEntered');
    var sMlbl = document.getElementById('sMinLbl');
    var sMin  = document.getElementById('sMin');
    var sBlbl = document.getElementById('sBaseLbl');
    var sBase = document.getElementById('sBase');
    var sExt  = document.getElementById('sExtraCharge');
    var sDlbl = document.getElementById('sDayLbl');
    var sDay  = document.getElementById('sDay');
    var sTot  = document.getElementById('sTotal');
    var waBtn = document.getElementById('waEstBtn');

    if (isOutstation) {
      var kmInput = document.getElementById('estKm');
      var daysInput = document.getElementById('estDays');
      var enteredKm = Math.max(0, Number((kmInput && kmInput.value) || 0));
      var days      = Math.max(1, Number((daysInput && daysInput.value) || 1));
      var baseFare  = MIN_KM * rate;
      var extraKm   = Math.max(0, enteredKm - MIN_KM);
      var extraCharge = extraKm * rate;
      var dayDuty   = days * DAY_DUTY;
      var total     = baseFare + extraCharge + dayDuty;

      if (sVeh)  sVeh.textContent  = v.name + ' (' + v.seats + ') ' + (isAC ? 'AC' : 'Non-AC');
      if (sRate) sRate.textContent = '₹' + rate + '/km';
      if (sElbl) sElbl.textContent = 'Entered distance';
      if (sEnt)  sEnt.textContent  = (enteredKm || 0) + ' km';
      if (sMlbl) sMlbl.textContent = 'Minimum billed';
      if (sMin)  sMin.textContent  = MIN_KM + ' km';
      if (sBlbl) sBlbl.textContent = 'Base fare (' + MIN_KM + '×₹' + rate + ')';
      if (sBase) sBase.textContent = fmt(baseFare);
      if (sExt)  sExt.textContent  = fmt(extraCharge);
      if (sDlbl) sDlbl.textContent = 'Driver duty (' + days + ' day' + (days > 1 ? 's' : '') + ')';
      if (sDay)  sDay.textContent  = fmt(dayDuty);
      if (sTot)  sTot.textContent  = fmt(total);

      var km  = enteredKm || MIN_KM;
      var msg = encodeURIComponent(
        'Outstation estimate – Trishika Car Rental\n' +
        'Vehicle: ' + v.name + ' (' + v.seats + ') ' + (isAC ? 'AC' : 'Non-AC') + '\n' +
        'Distance: ' + km + ' km (min billed ' + MIN_KM + ' km)\n' +
        'Rate: ₹' + rate + '/km\n' +
        'Base: ' + fmt(baseFare) + '\n' +
        'Extra km: ' + fmt(extraCharge) + '\n' +
        'Driver duty: ' + fmt(dayDuty) + '\n' +
        'Estimated total: ' + fmt(total) + '\n\n' +
        'Note: Tolls & parking extra.'
      );
      if (waBtn) waBtn.href = 'https://wa.me/918217577849?text=' + msg;

    } else {
      var hrsInput  = document.getElementById('estHrs');
      var hrs       = Math.max(8, Number((hrsInput && hrsInput.value) || 8));
      var localRate = isAC ? (v.local.rate ? v.local.rate.ac : rate) : (v.local.rate ? v.local.rate.nonac : rate);
      var base      = MIN_KM * localRate;
      var hrExtra   = hrs > 8 ? (hrs - 8) * 50 : 0;
      var total2    = base + hrExtra;

      if (sVeh)  sVeh.textContent  = v.name + ' (' + v.seats + ') ' + (isAC ? 'AC' : 'Non-AC');
      if (sRate) sRate.textContent = '₹' + localRate + '/km';
      if (sElbl) sElbl.textContent = 'Package';
      if (sEnt)  sEnt.textContent  = hrs + ' hrs / 80 km';
      if (sMlbl) sMlbl.textContent = 'Base distance';
      if (sMin)  sMin.textContent  = '80 km';
      if (sBlbl) sBlbl.textContent = 'Package base fare';
      if (sBase) sBase.textContent = fmt(base);
      if (sExt)  sExt.textContent  = hrExtra > 0 ? fmt(hrExtra) : '₹0';
      if (sDlbl) sDlbl.textContent = 'Extra hours';
      if (sDay)  sDay.textContent  = hrExtra > 0 ? fmt(hrExtra) : 'None';
      if (sTot)  sTot.textContent  = fmt(total2);

      var msg2 = encodeURIComponent(
        'Local estimate – Trishika Car Rental\n' +
        'Vehicle: ' + v.name + ' ' + (isAC ? 'AC' : 'Non-AC') + '\n' +
        'Package: ' + hrs + ' hrs / 80 km\n' +
        'Estimated total: ' + fmt(total2) + '\n\n' +
        'Note: Extra km ₹' + localRate + '/km. Tolls extra.'
      );
      if (waBtn) waBtn.href = 'https://wa.me/918217577849?text=' + msg2;
    }
  }

  // Wire up estimator controls
  var tripOut   = document.getElementById('tripOut');
  var tripLocal = document.getElementById('tripLocal');
  var acYes     = document.getElementById('acYes');
  var acNo      = document.getElementById('acNo');
  if (tripOut)   tripOut.addEventListener('click',   function () { setTrip(true); });
  if (tripLocal) tripLocal.addEventListener('click', function () { setTrip(false); });
  if (acYes)     acYes.addEventListener('click',     function () { setAC(true); });
  if (acNo)      acNo.addEventListener('click',      function () { setAC(false); });

  ['estVeh','estKm','estHrs','estDays'].forEach(function (id) {
    var el = document.getElementById(id);
    if (el) {
      el.addEventListener('input',  calc);
      el.addEventListener('change', calc);
    }
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
    c.addEventListener('click', function (e) {
      if (e.target.dataset.hrs) {
        var hrsInput = document.getElementById('estHrs');
        if (hrsInput) { hrsInput.value = e.target.dataset.hrs; calc(); }
      }
    });
  });

  // Initial calc
  calc();

}); // end DOMContentLoaded
