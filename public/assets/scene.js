// Animated plants and soil particles, drawn on <canvas data-scene="soil|meadow">.
// "soil" has a band of earth with microbes; "meadow" grows from the bottom edge.
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var darkMq = window.matchMedia('(prefers-color-scheme: dark)');

  var LIGHT = {
    soil: ['#7a5533', '#3f2a18'], crumbs: ['#8d6540', '#5a3c22', '#a37b52', '#2e1e11'],
    dust: ['#7a5533', '#a37b52', '#2f9a45', '#c9a227', '#5a3c22'],
    leaf: ['#2fbf62', '#1f9d4d', '#157a3a', '#57cf7f'], stem: '#1a7a3a', microbe: '#c8f7a8'
  };
  var DARK = {
    soil: ['#3d2c1d', '#150e08'], crumbs: ['#5a3c22', '#2e1e11', '#6f4f31', '#0f0a06'],
    dust: ['#c9a57a', '#8d6540', '#3ecf72', '#e0c14a', '#a37b52'],
    leaf: ['#3ecf72', '#1f9d4d', '#178a42', '#62dd8d'], stem: '#1f9d4d', microbe: '#b6f5a0'
  };

  function rand(a, b) { return a + Math.random() * (b - a); }
  function pick(list) { return list[Math.floor(Math.random() * list.length)]; }
  function clamp(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
  function ease(t) { t = clamp(t); return 1 - Math.pow(1 - t, 3); }

  function createScene(canvas) {
    var ctx = canvas.getContext('2d');
    if (!ctx) return;
    var hasSoil = canvas.getAttribute('data-scene') === 'soil';
    var host = canvas.closest('section') || canvas.parentNode;
    var W = 0, H = 0, builtW = 0, pal = LIGHT;
    var plants = [], dust = [], microbes = [], crumbs = [];
    var wind = 0, pointer = null, pointerWind = 0;
    var time = 0, last = 0, raf = 0, visible = true;

    function groundY(x) {
      if (!hasSoil) return H + 2;
      return H * 0.84 + Math.sin(x / W * 6.3 + 1) * H * 0.018 + Math.sin(x / W * 15 + 4) * H * 0.008;
    }

    function build() {
      builtW = W;
      var i, n;
      plants = [];
      n = Math.max(8, Math.min(26, Math.round(W / 62)));
      for (i = 0; i < n; i++) {
        var rx = (i + rand(0.15, 0.85)) / n;
        var edge = Math.abs(rx - 0.5) * 2;            // 0 in the centre, 1 at the sides
        var tall = W < 700 ? 0.17 : 0.3;                // keep plants clear of the headline on phones
        var rh = hasSoil ? (0.09 + tall * Math.pow(edge, 1.3)) * rand(0.7, 1.1) : rand(0.14, 0.34);
        var leaves = [], pairs = 2 + Math.floor(rand(0, 3));
        for (var k = 0; k < pairs; k++) {
          var u = 0.28 + (k / pairs) * 0.6 + rand(-0.04, 0.04);
          leaves.push({ u: u, side: k % 2 ? 1 : -1, len: rand(0.2, 0.3) * (1 - u * 0.35), color: pick(pal.leaf) });
        }
        plants.push({
          rx: rx, rh: rh, lean: rand(-0.2, 0.2), phase: rand(0, 6.3), speed: rand(0.6, 1.1),
          delay: rand(0, 1.8), dur: rand(2.4, 3.8), depth: rand(0.55, 1), leaves: leaves,
          top: [pick(pal.leaf), pick(pal.leaf)]
        });
      }
      plants.sort(function (a, b) { return a.depth - b.depth; });

      dust = [];
      n = Math.max(36, Math.min(120, Math.round(W / 12)));
      for (i = 0; i < n; i++) dust.push(spawnDust({}, true));

      crumbs = []; microbes = [];
      if (hasSoil) {
        n = Math.round(W / 9);
        for (i = 0; i < n; i++) crumbs.push({ rx: Math.random(), ry: Math.pow(Math.random(), 0.8), r: rand(0.8, 3.4), color: pick(pal.crumbs), a: rand(0.35, 0.9) });
        n = Math.max(10, Math.round(W / 60));
        for (i = 0; i < n; i++) microbes.push({ rx: Math.random(), ry: rand(0.15, 0.95), ang: rand(0, 6.3), v: rand(5, 13), r: rand(1, 2.2), phase: rand(0, 6.3) });
      }
    }

    function spawnDust(d, anyAge) {
      d.x = rand(0, W);
      d.y = groundY(d.x) - (hasSoil ? 0 : rand(0, 6));
      d.vy = -rand(7, 26);
      d.vx = rand(-4, 4);
      d.life = rand(6, 15);
      d.age = anyAge ? rand(0, d.life) : 0;
      if (anyAge) d.y += d.vy * d.age;
      d.r = rand(0.8, 3.2);
      d.f = rand(0.4, 1.2);
      d.phase = rand(0, 6.3);
      d.color = pick(pal.dust);
      d.depth = rand(0.35, 1);
      return d;
    }

    function resize() {
      var rect = canvas.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = rect.width; H = rect.height;
      canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      if (Math.abs(W - builtW) > 1) build();
      if (reduce) draw();
    }

    function leaf(x, y, angle, len, color, alpha) {
      if (len < 0.5) return;
      ctx.save();
      ctx.translate(x, y); ctx.rotate(angle);
      ctx.globalAlpha = alpha; ctx.fillStyle = color;
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.quadraticCurveTo(len * 0.45, -len * 0.42, len, 0);
      ctx.quadraticCurveTo(len * 0.45, len * 0.42, 0, 0);
      ctx.fill();
      ctx.restore();
    }

    function drawPlant(p) {
      var g = reduce ? 1 : ease((time - p.delay) / p.dur);
      if (g <= 0) return;
      var full = p.rh * H, h = full * g;
      var x0 = p.rx * W, y0 = groundY(x0) + 4;
      var sway = (Math.sin(time * p.speed + p.phase) * 0.04 + wind * 0.14) * h;
      var cx = x0 + p.lean * h * 0.2, cy = y0 - h * 0.6;
      var x1 = x0 + p.lean * h + sway, y1 = y0 - h;
      var alpha = 0.45 + 0.55 * p.depth;

      ctx.globalAlpha = alpha;
      ctx.strokeStyle = pal.stem; ctx.lineCap = 'round';
      ctx.lineWidth = Math.max(1.4, full * 0.02) * p.depth;
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.quadraticCurveTo(cx, cy, x1, y1); ctx.stroke();

      for (var i = 0; i < p.leaves.length; i++) {
        var l = p.leaves[i], u = l.u, m = 1 - u;
        var px = m * m * x0 + 2 * m * u * cx + u * u * x1;
        var py = m * m * y0 + 2 * m * u * cy + u * u * y1;
        var ang = Math.atan2(2 * m * (cy - y0) + 2 * u * (y1 - cy), 2 * m * (cx - x0) + 2 * u * (x1 - cx));
        var open = ease((g - u * 0.8) / 0.25);
        var flutter = Math.sin(time * 1.7 + p.phase + u * 5) * 0.09;
        leaf(px, py, ang + l.side * (1.25 - 0.35 * open) + flutter, full * l.len * open, l.color, alpha);
      }
      var tipAng = Math.atan2(y1 - cy, x1 - cx), topOpen = ease((g - 0.7) / 0.3);
      var tf = Math.sin(time * 1.4 + p.phase) * 0.07;
      leaf(x1, y1, tipAng - 0.62 + tf, full * 0.3 * topOpen, p.top[0], alpha);
      leaf(x1, y1, tipAng + 0.62 + tf, full * 0.24 * topOpen, p.top[1], alpha);
      ctx.globalAlpha = 1;
    }

    function drawSoil(dt) {
      var x, grad = ctx.createLinearGradient(0, H * 0.8, 0, H);
      grad.addColorStop(0, pal.soil[0]); grad.addColorStop(1, pal.soil[1]);
      ctx.fillStyle = grad;
      ctx.beginPath(); ctx.moveTo(0, H);
      for (x = 0; x <= W + 24; x += 24) ctx.lineTo(x, groundY(x));
      ctx.lineTo(W, H); ctx.closePath(); ctx.fill();

      var i, c, gy;
      for (i = 0; i < crumbs.length; i++) {
        c = crumbs[i]; x = c.rx * W; gy = groundY(x);
        ctx.globalAlpha = c.a; ctx.fillStyle = c.color;
        ctx.beginPath(); ctx.arc(x, gy + 3 + c.ry * (H - gy - 4), c.r, 0, 6.3); ctx.fill();
      }
      // Microbes: small glowing dots wandering through the soil.
      ctx.fillStyle = pal.microbe;
      for (i = 0; i < microbes.length; i++) {
        var mb = microbes[i];
        if (!reduce) {
          mb.ang += rand(-1, 1) * dt * 2.2;
          mb.rx += Math.cos(mb.ang) * mb.v * dt / W;
          mb.ry += Math.sin(mb.ang) * mb.v * dt / (H * 0.16);
          if (mb.rx < 0) mb.rx += 1; else if (mb.rx > 1) mb.rx -= 1;
          if (mb.ry < 0.12 || mb.ry > 0.96) { mb.ang = -mb.ang; mb.ry = Math.min(0.96, Math.max(0.12, mb.ry)); }
        }
        x = mb.rx * W; gy = groundY(x);
        var y = gy + mb.ry * (H - gy), pulse = 0.5 + 0.5 * Math.sin(time * 2 + mb.phase);
        ctx.globalAlpha = 0.12 + 0.12 * pulse;
        ctx.beginPath(); ctx.arc(x, y, mb.r * 3.2, 0, 6.3); ctx.fill();
        ctx.globalAlpha = 0.55 + 0.4 * pulse;
        ctx.beginPath(); ctx.arc(x, y, mb.r, 0, 6.3); ctx.fill();
      }
      ctx.globalAlpha = 1;
    }

    function drawDust(dt) {
      for (var i = 0; i < dust.length; i++) {
        var d = dust[i];
        if (!reduce) {
          d.age += dt;
          if (d.age > d.life || d.y < -10) { spawnDust(d, false); continue; }
          d.x += (d.vx + Math.sin(d.age * d.f + d.phase) * 9 + wind * 55) * dt * d.depth;
          d.y += d.vy * dt * d.depth;
          if (pointer) {
            var dx = d.x - pointer.x, dy = d.y - pointer.y, dist = dx * dx + dy * dy;
            if (dist < 12100 && dist > 1) { var push = (1 - dist / 12100) * 90 * dt; dist = Math.sqrt(dist); d.x += dx / dist * push; d.y += dy / dist * push; }
          }
        }
        var fade = Math.sin(Math.PI * clamp(d.age / d.life));
        ctx.globalAlpha = fade * (0.25 + 0.6 * d.depth);
        ctx.fillStyle = d.color;
        ctx.beginPath(); ctx.arc(d.x, d.y, d.r * (0.6 + 0.4 * d.depth), 0, 6.3); ctx.fill();
      }
      ctx.globalAlpha = 1;
    }

    function draw(dt) {
      dt = dt || 0;
      ctx.clearRect(0, 0, W, H);
      var i;
      for (i = 0; i < plants.length; i++) if (plants[i].depth < 0.78) drawPlant(plants[i]);
      if (hasSoil) drawSoil(dt);
      for (i = 0; i < plants.length; i++) if (plants[i].depth >= 0.78) drawPlant(plants[i]);
      drawDust(dt);
    }

    function frame(now) {
      raf = 0;
      var dt = Math.min(0.05, (now - last) / 1000 || 0);
      last = now; time += dt;
      var target = Math.sin(time * 0.23) * 0.22 + Math.sin(time * 0.71 + 2) * 0.1 + pointerWind;
      wind += (target - wind) * Math.min(1, dt * 1.5);
      pointerWind *= Math.pow(0.4, dt);
      draw(dt);
      schedule();
    }
    function schedule() {
      if (!raf && !reduce && visible && !document.hidden) { last = performance.now(); raf = requestAnimationFrame(frame); }
    }

    function restyle() { pal = darkMq.matches ? DARK : LIGHT; builtW = 0; resize(); }

    host.addEventListener('pointermove', function (e) {
      var rect = canvas.getBoundingClientRect();
      var x = e.clientX - rect.left, y = e.clientY - rect.top;
      if (pointer) pointerWind = Math.max(-1.2, Math.min(1.2, pointerWind + (x - pointer.x) / W * 3));
      pointer = { x: x, y: y };
    });
    host.addEventListener('pointerleave', function () { pointer = null; });
    window.addEventListener('resize', resize);
    document.addEventListener('visibilitychange', schedule);
    if (darkMq.addEventListener) darkMq.addEventListener('change', restyle);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) { visible = entries[0].isIntersecting; schedule(); }).observe(canvas);
    }

    pal = darkMq.matches ? DARK : LIGHT;
    if (reduce) time = 100;
    resize();
    schedule();
  }

  var canvases = document.querySelectorAll('canvas[data-scene]');
  for (var i = 0; i < canvases.length; i++) createScene(canvases[i]);
})();
