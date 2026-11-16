// Small enhancements only; every page reads fine without JavaScript.
(function () {
  document.documentElement.classList.add('js');

  // Three-step section: show one description at a time.
  document.querySelectorAll('[data-pillars]').forEach(function (root) {
    var tabs = root.querySelectorAll('[role="tab"]');
    var panels = root.querySelectorAll('.pillar-panel');
    function select(i) {
      tabs.forEach(function (t, n) { t.setAttribute('aria-selected', n === i ? 'true' : 'false'); });
      panels.forEach(function (p, n) { p.classList.toggle('is-active', n === i); });
    }
    var current = 0, timer = null;
    var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function show(i) { current = i; select(i); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } root.classList.remove('is-auto'); }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { stop(); show(i); });
      t.addEventListener('mouseenter', function () { stop(); show(i); });
      t.addEventListener('focus', function () { stop(); show(i); });
    });
    show(0);
    // Step through the three panels until the visitor takes over.
    if (!still && 'IntersectionObserver' in window) {
      new IntersectionObserver(function (entries, obs) {
        if (!entries[0].isIntersecting) return;
        obs.disconnect();
        root.classList.add('is-auto');
        timer = setInterval(function () { if (!document.hidden) show((current + 1) % tabs.length); }, 4500);
      }, { threshold: 0.4 }).observe(root);
    }
  });

  // Parallax: illustration panels drift slightly against the scroll.
  var arts = document.querySelectorAll('.split .art');
  if (arts.length && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var ticking = false;
    var parallax = function () {
      ticking = false;
      var vh = window.innerHeight;
      arts.forEach(function (art) {
        var r = art.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        var progress = ((r.top + r.height / 2) - vh / 2) / (vh / 2 + r.height / 2);
        art.firstElementChild.style.setProperty('--py', (-progress * r.height * 0.07).toFixed(1) + 'px');
      });
    };
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(parallax); } }, { passive: true });
    window.addEventListener('resize', parallax);
    parallax();
  }

  // Fade sections in as they scroll into view.
  var items = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('is-in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  items.forEach(function (el) { io.observe(el); });
})();
