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
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(i); });
      t.addEventListener('mouseenter', function () { select(i); });
    });
    select(0);
  });

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
