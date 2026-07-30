// Core Navigation, Sliders, Charts & Interactions
    // NAV SCROLL
    const nav = document.getElementById('mainNav');
    window.addEventListener('scroll', () => nav.classList.toggle('scrolled', scrollY > 30));

    // HAMBURGER
    const hamburger = document.getElementById('hamburger');
    const mobileNav = document.getElementById('mobileNav');
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('open');
      mobileNav.classList.toggle('open');
      document.body.style.overflow = mobileNav.classList.contains('open') ? 'hidden' : '';
    });
    document.querySelectorAll('.mobile-nav a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('open');
        mobileNav.classList.remove('open');
        document.body.style.overflow = '';
      });
    });

    // HERO PARTICLES
    (function () {
      const c = document.getElementById('heroParticles');
      if (!c) return;
      for (let i = 0; i < 22; i++) {
        const p = document.createElement('div');
        p.className = 'particle';
        const s = Math.random() * 2.5 + 1;
        p.style.cssText = `width:${s}px;height:${s}px;left:${Math.random() * 100}%;animation-duration:${Math.random() * 14 + 10}s;animation-delay:${Math.random() * -22}s;--drift:${(Math.random() - 0.5) * 80}px;opacity:${Math.random() * 0.4 + 0.1};`;
        c.appendChild(p);
      }
    })();

    // WE TRADE SLIDER
    (function () {
      const outer = document.getElementById('wtOuter');
      const track = document.getElementById('wtTrack');
      if (!outer || !track) return;
      const slides = Array.from(track.querySelectorAll('.wt-slide'));
      const dotEls = Array.from(document.querySelectorAll('.wt-dot'));
      const total = slides.length;
      let cur = 0, startX = 0, isDragging = false, startTX = 0, autoTimer;

      function sw() { return slides[0].offsetWidth; }
      function ctr() { return (outer.offsetWidth - sw()) / 2; }
      function tx(n) { return ctr() - n * (sw() + 32); }

      function goTo(n, instant) {
        cur = ((n % total) + total) % total;
        track.style.transition = instant ? 'none' : 'transform 0.7s cubic-bezier(0.25,0.46,0.45,0.94)';
        track.style.transform = `translateX(${tx(cur)}px)`;
        slides.forEach((s, i) => s.classList.toggle('wt-active', i === cur));
        dotEls.forEach((d, i) => d.classList.toggle('active', i === cur));
      }

      dotEls.forEach((d, i) => d.addEventListener('click', () => { clearInterval(autoTimer); goTo(i); startAuto(); }));

      function startAuto() { autoTimer = setInterval(() => goTo(cur + 1), 4500); }

      outer.addEventListener('mousedown', e => { isDragging = true; startX = e.clientX; startTX = tx(cur); outer.style.cursor = 'grabbing'; e.preventDefault(); });
      window.addEventListener('mousemove', e => {
        if (!isDragging) return;
        track.style.transition = 'none';
        track.style.transform = `translateX(${startTX + e.clientX - startX}px)`;
      });
      window.addEventListener('mouseup', e => {
        if (!isDragging) return;
        isDragging = false; outer.style.cursor = 'grab';
        if (Math.abs(e.clientX - startX) > 60) goTo(cur + (e.clientX < startX ? 1 : -1));
        else goTo(cur);
      });
      outer.addEventListener('touchstart', e => { startX = e.touches[0].clientX; startTX = tx(cur); clearInterval(autoTimer); }, { passive: true });
      outer.addEventListener('touchmove', e => {
        track.style.transition = 'none';
        track.style.transform = `translateX(${startTX + e.touches[0].clientX - startX}px)`;
      }, { passive: true });
      outer.addEventListener('touchend', e => {
        const d = e.changedTouches[0].clientX - startX;
        if (Math.abs(d) > 60) goTo(cur + (d < 0 ? 1 : -1)); else goTo(cur);
        startAuto();
      });

      window.addEventListener('resize', () => goTo(cur, true));
      goTo(0, true);
      startAuto();
    })();

    // COUNTER
    function animCount(el) {
      const t = parseFloat(el.dataset.count), suf = el.dataset.suffix || '';
      const isDec = el.hasAttribute('data-dec'), isK = el.hasAttribute('data-k');
      const dur = 1800, s = performance.now();
      (function step(n) { const p = Math.min((n - s) / dur, 1), e = 1 - Math.pow(1 - p, 3), v = t * e; el.textContent = isDec ? v.toFixed(1) + suf : isK ? Math.floor(v / 1000) + 'K+' : Math.floor(v) + suf; if (p < 1) requestAnimationFrame(step); })(s);
    }
    const io = new IntersectionObserver(entries => { entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); e.target.querySelectorAll('[data-count]').forEach(animCount); io.unobserve(e.target); } }); }, { threshold: .1 });
    document.querySelectorAll('.rv').forEach(el => io.observe(el));
    const sio = new IntersectionObserver(entries => { entries.forEach(e => { if (e.isIntersecting) { e.target.querySelectorAll('[data-count]').forEach(animCount); sio.unobserve(e.target); } }); }, { threshold: .3 });
    const sb = document.querySelector('#stats'); if (sb) sio.observe(sb);

    // SPOTLIGHT CHART BARS
    (function () {
      const vals = [3200, 2900, 3800, 2700, 3500, 3100, 4000, 2800, 3600, 3300, 3900, 3100];
      const mx = Math.max(...vals);
      const container = document.getElementById('spotBars');
      if (!container) return;
      vals.forEach((v, i) => {
        const b = document.createElement('div');
        b.className = 'mock-b' + (i === 4 ? ' hi' : '');
        b.style.height = '5%';
        b.style.transitionDelay = (i * 0.05) + 's';
        container.appendChild(b);
      });
      const spotObs = new IntersectionObserver(entries => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            container.querySelectorAll('.mock-b').forEach((b, i) => {
              setTimeout(() => { b.style.height = (vals[i] / mx * 100) + '%'; }, i * 55);
            });
            spotObs.unobserve(e.target);
          }
        });
      }, { threshold: 0.3 });
      spotObs.observe(container);
    })();

    // PERFORMANCE CHART
    const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    let PD = {};
    [2023, 2024, 2025, 2026].forEach(y => {
      PD[y] = {
        forex: { vals: Array(12).fill(0), wins: Array(12).fill(0), setups: Array(12).fill(0), badge: 'Pips' },
        stocks: { vals: Array(12).fill(0), wins: Array(12).fill(0), setups: Array(12).fill(0), badge: 'Ideas' },
        crypto: { vals: Array(12).fill(0), wins: Array(12).fill(0), setups: Array(12).fill(0), badge: '% Gain' },
        commodity: { vals: Array(12).fill(0), wins: Array(12).fill(0), setups: Array(12).fill(0), badge: 'Points' }
      };
    });
    // Default 2025 data
    PD[2025].forex = { vals: [3200, 2900, 3800, 2700, 3500, 3100, 4000, 2800, 3600, 3300, 3900, 3100], wins: [82, 78, 85, 75, 83, 80, 88, 76, 84, 81, 86, 80], setups: [22, 20, 24, 19, 21, 23, 26, 20, 23, 22, 25, 21], badge: 'Pips' };
    PD[2025].stocks = { vals: [140, 125, 160, 110, 145, 132, 172, 118, 155, 138, 168, 130], wins: [75, 70, 78, 68, 76, 72, 80, 69, 77, 73, 79, 71], setups: [18, 16, 20, 14, 17, 19, 22, 15, 18, 17, 21, 16], badge: 'Ideas' };
    PD[2025].crypto = { vals: [12, 9, 15, 8, 13, 11, 17, 9, 14, 12, 16, 10], wins: [72, 68, 76, 65, 73, 70, 78, 66, 74, 71, 77, 69], setups: [20, 18, 22, 16, 19, 21, 24, 17, 20, 19, 23, 18], badge: '% Gain' };
    PD[2025].commodity = { vals: [280, 240, 320, 210, 295, 265, 345, 225, 305, 270, 330, 255], wins: [79, 74, 82, 71, 80, 77, 84, 72, 81, 78, 83, 75], setups: [14, 12, 16, 10, 13, 15, 18, 11, 14, 13, 17, 12], badge: 'Points' };

    // GOOGLE SHEETS INTEGRATION
    // 1. Create a Google Sheet with 7 columns: Year, Market, Month, Value, WinRate, Setups, Badge
    //    Example row: 2025, forex, Jan, 3500, 85, 24, Pips
    // 2. Go to File > Share > Publish to web > Choose CSV
    // 3. Paste the generated link below:
    const GOOGLE_SHEET_CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTTaYok6tUN4iGe_xSpRxwBEWto29G40oy2EHIFbDMBbFpS12FywY93HEQyv3hysl4XbLfrckQSCg6G/pub?output=csv';

    async function fetchSheetData() {
      if (!GOOGLE_SHEET_CSV_URL) return;
      try {
        const res = await fetch(GOOGLE_SHEET_CSV_URL);
        const text = await res.text();
        const rows = text.split('\n').map(r => r.split(',').map(c => c.trim()));

        for (let i = 1; i < rows.length; i++) {
          if (rows[i].length >= 7) {
            const yr = parseInt(rows[i][0]);
            const mkt = rows[i][1].toLowerCase();
            const mStr = rows[i][2];
            const mIdx = MONTHS.findIndex(m => mStr.toLowerCase().startsWith(m.toLowerCase()));
            if (PD[yr] && PD[yr][mkt] && mIdx >= 0) {
              PD[yr][mkt].vals[mIdx] = parseFloat(rows[i][3]) || PD[yr][mkt].vals[mIdx];
              PD[yr][mkt].wins[mIdx] = parseFloat(rows[i][4]) || PD[yr][mkt].wins[mIdx];
              PD[yr][mkt].setups[mIdx] = parseFloat(rows[i][5]) || PD[yr][mkt].setups[mIdx];
              if (rows[i][6]) PD[yr][mkt].badge = rows[i][6];
            }
          }
        }
        drawPerf();
      } catch (e) {
        console.error("Error fetching Google Sheet data:", e);
      }
    }
    fetchSheetData();

    const LABS = { forex: ['Pips Potential', 'Win Rate', 'Weekly Setups'], stocks: ['Ideas Shared', 'Win Rate', 'Ideas/Week'], crypto: ['Avg % Gain', 'Win Rate', 'Weekly Setups'], commodity: ['Points Moved', 'Win Rate', 'Weekly Setups'] };
    let cY = 2025, cM = 'forex', cI = 0;
    function drawPerf() {
      const d = PD[cY][cM], mkt = { forex: 'FOREX', stocks: 'STOCKS', crypto: 'CRYPTO', commodity: 'COMMODITY' }[cM];
      document.getElementById('perfT').textContent = `${MONTHS[cI].toUpperCase()} ${cY} — ${mkt}`;
      document.getElementById('perfB').textContent = `${d.vals[cI]} ${d.badge}`;
      const cw = document.getElementById('chWrap'), cl = document.getElementById('chLbls');
      cw.innerHTML = ''; cl.innerHTML = '';
      const mx = Math.max(...d.vals, 1); // prevent division by zero
      d.vals.forEach((v, i) => {
        const bar = document.createElement('div'); bar.className = 'ch-bar';
        const inn = document.createElement('div'); inn.className = 'ch-inner';
        inn.style.height = '5%'; inn.style.background = i === cI ? 'rgba(59,130,246,0.7)' : 'rgba(59,130,246,0.2)';
        bar.appendChild(inn); cw.appendChild(bar);
        setTimeout(() => { inn.style.height = (v / mx * 100) + '%'; }, 60 + i * 28);
        bar.addEventListener('click', () => { document.querySelectorAll('.mobtn').forEach((b, j) => b.classList.toggle('active', j === i)); cI = i; drawPerf(); });
        const lbl = document.createElement('div'); lbl.className = 'ch-lbl'; lbl.textContent = MONTHS[i].slice(0, 1); cl.appendChild(lbl);
      });
      const cs = document.getElementById('pcStats');
      cs.innerHTML = [d.vals[cI], d.wins[cI] + '%', d.setups[cI]].map((v, i) => `<div><div class="pcs-val">${v}</div><div class="pcs-lbl">${LABS[cM][i]}</div></div>`).join('');
    }
    drawPerf();
    
    document.querySelectorAll('.ybtn').forEach(b => b.addEventListener('click', () => { document.querySelectorAll('.ybtn').forEach(x => x.classList.remove('active')); b.classList.add('active'); cY = parseInt(b.dataset.y); drawPerf(); }));
    document.querySelectorAll('.mkbtn').forEach(b => b.addEventListener('click', () => { document.querySelectorAll('.mkbtn').forEach(x => x.classList.remove('active')); b.classList.add('active'); cM = b.dataset.m; drawPerf(); }));
    
    document.querySelectorAll('.mobtn').forEach(b => b.addEventListener('click', () => { document.querySelectorAll('.mobtn').forEach(x => x.classList.remove('active')); b.classList.add('active'); cI = +b.dataset.i; drawPerf(); }));

    // TESTIMONIALS SLIDER
    const TMS = [
      { name: 'Karthik A.', city: 'Chennai', date: 'Apr 2025', title: 'Gold strategies that actually work', text: "TradeWiz's gold trading strategies completely changed the game for me. I now have a clear plan for entries, exits, and risk. Every trade setup makes sense." },
      { name: 'Poonam T.', city: 'Bangalore', date: 'Mar 2025', title: 'Unmatched accuracy on forex setups', text: "The accuracy of the forex setups is simply unmatched. A disciplined low-risk, high-reward system that actually delivers consistent results week after week." },
      { name: 'Rishabh N.', city: 'Delhi', date: 'Apr 2025', title: 'NFP events no longer terrify me', text: "Trading live NFP and CPI events used to be terrifying. The live sessions with TradeWiz taught me how to stay calm and trade smart even in volatile conditions." },
      { name: 'Zoya H.', city: 'Hyderabad', date: 'Feb 2025', title: 'The CPI session was a live masterclass', text: "The CPI event session alone was worth the entire membership fee. It was like a live masterclass in real-time trading. I learned more in 2 hours than in months of self-study." },
      { name: 'Nitesh S.', city: 'Mumbai', date: 'Mar 2025', title: 'Finally trading like a pro', text: "Now I understand how to prepare, set logical targets, and manage my risk like a pro. No more guessing. No more random entries. Just a clear, repeatable process." },
      { name: 'Tanvi V.', city: 'Pune', date: 'Jan 2025', title: '3500+ pips in a month is real', text: "The 3500+ pips monthly potential is real. It's the cumulative result of consistent, well-researched, and logical setups that build on each other over time." },
      { name: 'Rajeev M.', city: 'Kolkata', date: 'Apr 2025', title: 'My trading psychology transformed', text: "Mastering risk management through TradeWiz has fundamentally changed my trading psychology. No more anxiety, no more panic sells. Just structured, calm decision-making." },
      { name: 'Sana R.', city: 'Ahmedabad', date: 'Feb 2025', title: 'Every idea comes with full reasoning', text: "Every trade idea comes with clearly defined entries, stop-losses, and take-profits along with the reasoning behind each level. It's education wrapped in every signal." },
      { name: 'Ankit B.', city: 'Gurgaon', date: 'Mar 2025', title: '150 pips on my first real win', text: "I caught 150 pips on a single EURUSD trade thanks to the community's strategies. It was my first real win in trading and gave me the confidence to keep going." },
      { name: 'Kritika L.', city: 'Lucknow', date: 'Jan 2025', title: 'Like trading with a smart army', text: "It truly feels like I'm trading with a smart army behind me. My consistency improved dramatically and I'm finally building a real track record." },
      { name: 'Ashwin T.', city: 'Jaipur', date: 'Apr 2025', title: 'Deep analysis, simple to understand', text: "The weekly reviews are deep in analysis yet simple to understand. Now I finally know why I lost trades earlier. The clarity this community provides is unmatched." },
      { name: 'Naina J.', city: 'Indore', date: 'Feb 2025', title: 'Gold scalping is no longer scary', text: "I would never have dared to scalp gold before. The strategies and live guidance have been a complete revelation. I now scalp with confidence and consistency." },
    ];
    (function initTMSlider() {
      const track = document.getElementById('tmTrack');
      const dotsEl = document.getElementById('tmDots');
      const prevBtn = document.getElementById('tmPrev');
      const nextBtn = document.getElementById('tmNext');
      TMS.forEach(t => {
        const init = t.name.split(' ').map(n => n[0]).join('');
        const slide = document.createElement('div'); slide.className = 'tm-slide';
        slide.innerHTML = `<div class="tcard2"><div class="tc2-quote">"</div><div class="tc2-title">${t.title}</div><p class="tc2-body">${t.text}</p><div class="tc2-footer"><div class="tc2-av">${init}</div><div class="tc2-meta"><div class="tc2-name">${t.name} &middot; ${t.city}</div><div class="tc2-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><div class="tc2-date">${t.date}</div></div></div></div>`;
        track.appendChild(slide);
      });
      let cur = 0;
      function getVisible() {
        const w = track.parentElement.offsetWidth;
        if (w < 600) return 1;
        if (w < 900) return 2;
        return 3;
      }
      function maxIndex() { return Math.max(0, TMS.length - getVisible()); }
      function buildDots() {
        dotsEl.innerHTML = '';
        const pages = maxIndex() + 1;
        for (let i = 0; i < pages; i++) {
          const d = document.createElement('button'); d.className = 'tm-dot2' + (i === cur ? ' active' : '');
          d.addEventListener('click', () => goTo(i)); dotsEl.appendChild(d);
        }
      }
      function goTo(n) {
        cur = Math.max(0, Math.min(n, maxIndex()));
        const slideW = track.children[0] ? track.children[0].offsetWidth + 24 : 0;
        track.style.transform = `translateX(-${cur * slideW}px)`;
        prevBtn.disabled = cur === 0;
        nextBtn.disabled = cur === maxIndex();
        dotsEl.querySelectorAll('.tm-dot2').forEach((d, i) => d.classList.toggle('active', i === cur));
      }
      prevBtn.addEventListener('click', () => goTo(cur - 1));
      nextBtn.addEventListener('click', () => goTo(cur + 1));
      let rx = 0; track.parentElement.addEventListener('touchstart', e => { rx = e.touches[0].clientX; }, { passive: true });
      track.parentElement.addEventListener('touchend', e => { const dx = e.changedTouches[0].clientX - rx; if (Math.abs(dx) > 50) goTo(cur + (dx < 0 ? 1 : -1)); });
      buildDots(); goTo(0);
      window.addEventListener('resize', () => { buildDots(); goTo(Math.min(cur, maxIndex())); });
    })();

    // PRICING TOGGLE
    document.getElementById('tQ').addEventListener('click', () => { document.getElementById('tQ').classList.add('active'); document.getElementById('tA').classList.remove('active'); document.querySelectorAll('.pn').forEach(e => e.textContent = parseInt(e.dataset.q).toLocaleString('en-IN')); document.querySelectorAll('.pp').forEach(e => e.textContent = '/ 3 months · billed quarterly'); });
    document.getElementById('tA').addEventListener('click', () => { document.getElementById('tA').classList.add('active'); document.getElementById('tQ').classList.remove('active'); document.querySelectorAll('.pn').forEach(e => e.textContent = parseInt(e.dataset.a).toLocaleString('en-IN')); document.querySelectorAll('.pp').forEach(e => e.textContent = '/ month · billed annually'); });

    // FAQ
    document.querySelectorAll('.fq-q').forEach(btn => { btn.addEventListener('click', () => { const a = btn.nextElementSibling, open = btn.classList.contains('open'); document.querySelectorAll('.fq-q').forEach(b => { b.classList.remove('open'); b.nextElementSibling.classList.remove('open'); }); if (!open) { btn.classList.add('open'); a.classList.add('open'); } }); });
  

// Lead Generation Modal & Webhook Integration
    (function () {
      // ── REPLACE THIS WITH YOUR GOOGLE APPS SCRIPT WEB APP URL ──
      const SHEET_URL = 'https://script.google.com/macros/s/AKfycbwmWJ3MH8VpJIDgmc5KMb_L3AsFM4LHkR2ixRvzaVx_gs3YKN-TQWmadYfpIPIPHB_-/exec';

      const overlay = document.getElementById('tw-popup-overlay');
      const closeBtn = document.getElementById('tw-popup-close');
      const submitBtn = document.getElementById('tw-popup-submit');
      const form = document.getElementById('tw-popup-form');
      const successBox = document.getElementById('tw-popup-success');

      const nameEl   = document.getElementById('tw-name');
      const emailEl  = document.getElementById('tw-email');
      const phoneEl  = document.getElementById('tw-phone');
      const marketEl = document.getElementById('tw-market');
      const nameErr   = document.getElementById('tw-name-err');
      const emailErr  = document.getElementById('tw-email-err');
      const phoneErr  = document.getElementById('tw-phone-err');
      const marketErr = document.getElementById('tw-market-err');

      // Show popup after 4 seconds (only once per session)
      if (!sessionStorage.getItem('tw_popup_seen')) {
        setTimeout(() => overlay.classList.add('active'), 4000);
      }

      function closePopup() {
        overlay.classList.remove('active');
        sessionStorage.setItem('tw_popup_seen', '1');
      }

      closeBtn.addEventListener('click', closePopup);
      overlay.addEventListener('click', (e) => { if (e.target === overlay) closePopup(); });
      document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closePopup(); });

      // Only allow digits in phone field
      phoneEl.addEventListener('input', () => {
        phoneEl.value = phoneEl.value.replace(/\D/g, '').slice(0, 10);
      });

      function validate() {
        let ok = true;
        const emailRx = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const phoneRx = /^[6-9]\d{9}$/;

        [nameEl, nameErr].forEach(el => el.classList.remove('error', 'visible'));
        [emailEl, emailErr].forEach(el => el.classList.remove('error', 'visible'));
        [phoneEl, phoneErr].forEach(el => el.classList.remove('error', 'visible'));
        [marketEl, marketErr].forEach(el => el.classList.remove('error', 'visible'));

        if (!nameEl.value.trim()) {
          nameEl.classList.add('error'); nameErr.classList.add('visible'); ok = false;
        }
        if (!emailRx.test(emailEl.value.trim())) {
          emailEl.classList.add('error'); emailErr.classList.add('visible'); ok = false;
        }
        if (!phoneRx.test(phoneEl.value.trim())) {
          phoneEl.classList.add('error'); phoneErr.classList.add('visible'); ok = false;
        }
        if (!marketEl.value) {
          marketEl.classList.add('error'); marketErr.classList.add('visible'); ok = false;
        }
        return ok;
      }

      submitBtn.addEventListener('click', async () => {
        if (!validate()) return;
        submitBtn.disabled = true;
        submitBtn.textContent = 'Submitting…';

        const payload = {
          name: nameEl.value.trim(),
          email: emailEl.value.trim(),
          phone: phoneEl.value.trim(),
          market: marketEl.value
        };

        try {
          const formData = new FormData();
          formData.append('token', 'tw_secret_2024_xyz');
          formData.append('name', payload.name);
          formData.append('email', payload.email);
          formData.append('phone', payload.phone);
          formData.append('market', payload.market);
          await fetch(SHEET_URL, {
            method: 'POST',
            body: formData,
            mode: 'no-cors'
          });
        } catch (_) { /* no-cors won't throw, network errors are silent */ }

        if (typeof gtag === 'function') { gtag('event', 'generate_lead', { event_category: 'engagement', event_label: payload.market }); }
        form.style.display = 'none';
        successBox.style.display = 'block';
        sessionStorage.setItem('tw_popup_seen', '1');
        setTimeout(closePopup, 3500);
      });
    })();

// WhatsApp Support Floating Widget
    const waBtn = document.getElementById('waBtn');
    const waLabel = document.getElementById('waLabel');
    const waClose = document.getElementById('waClose');
    let waOpen = false;

    // Auto-show label after 3 seconds
    setTimeout(() => {
      waLabel.classList.add('visible');
      waOpen = true;
    }, 3000);

    waBtn.addEventListener('click', () => {
      if (waOpen) {
        if (typeof gtag === 'function') { gtag('event', 'contact_whatsapp', { event_category: 'contact' }); }
        window.open('https://wa.me/917011957726', '_blank');
      } else {
        waLabel.classList.add('visible');
        waOpen = true;
      }
    });

    waClose.addEventListener('click', (e) => {
      e.stopPropagation();
      waLabel.classList.remove('visible');
      waOpen = false;
    });
  
