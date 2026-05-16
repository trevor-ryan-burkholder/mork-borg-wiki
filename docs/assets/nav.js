// MÖRK BORG WIKI — Navigation JS

(function () {
  'use strict';

  // ── Mobile Nav Toggle ─────────────────────────────────────
  const toggle = document.querySelector('.nav-toggle');
  const nav    = document.querySelector('.site-nav');
  const overlay = document.querySelector('.nav-overlay');

  function openNav() {
    nav.classList.add('open');
    overlay.classList.add('active');
    toggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeNav() {
    nav.classList.remove('open');
    overlay.classList.remove('active');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      if (nav.classList.contains('open')) {
        closeNav();
      } else {
        openNav();
      }
    });
  }

  if (overlay) {
    overlay.addEventListener('click', closeNav);
  }

  // Close nav on link click (mobile)
  if (nav) {
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth <= 900) {
          closeNav();
        }
      });
    });
  }

  // ── Active Nav Highlighting ────────────────────────────────
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.site-nav a');

  navLinks.forEach(function (link) {
    const linkPath = new URL(link.href, window.location.origin).pathname;
    // Normalize trailing slash
    const normCurrent = currentPath.replace(/\/$/, '') || '/';
    const normLink    = linkPath.replace(/\/$/, '') || '/';

    if (normCurrent === normLink) {
      link.classList.add('active');
    }
  });

  // ── Keyboard Escape closes nav ─────────────────────────────
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav && nav.classList.contains('open')) {
      closeNav();
    }
  });

})();
