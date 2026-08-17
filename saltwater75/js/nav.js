/**
 * Saltwater 75 — navigation behaviour.
 * Sticky header state on scroll, mobile toggle, dropdowns, subscribe confirmation.
 */
(function () {
	'use strict';

	// Running inside an iframe (e.g. pasted into a Wix HTML embed) changes what
	// viewport units mean — see the .is-framed rules in style.css.
	var framed;
	try {
		framed = window.self !== window.top;
	} catch (e) {
		framed = true;   // cross-origin access threw, which itself means framed
	}
	if (framed) {
		document.documentElement.classList.add('is-framed');
		// 100svh would resolve to the frame's height, so approximate a real
		// viewport from the device screen — that IS readable from inside a
		// frame. Bounded so tiny laptops and huge monitors both stay sensible.
		var screenH = (window.screen && window.screen.availHeight) || 900;
		var heroH   = Math.max(560, Math.min(screenH - 130, 950));
		document.documentElement.style.setProperty('--framed-hero-h', heroH + 'px');
	}

	var header = document.querySelector('.site-header[data-sticky]');
	var toggle = document.querySelector('.nav-toggle');
	var nav    = document.getElementById('site-navigation');

	// Solid header once the user scrolls past the hero-ish threshold.
	function onScroll() {
		if (!header) return;
		if (window.scrollY > 40) {
			header.classList.add('is-scrolled');
		} else {
			header.classList.remove('is-scrolled');
		}
	}
	window.addEventListener('scroll', onScroll, { passive: true });
	onScroll();

	// Must match the drawer breakpoint in style.css.
	var mobile = window.matchMedia('(max-width: 1024px)');

	function setOpen(open) {
		header.classList.toggle('nav-open', open);
		document.body.classList.toggle('nav-locked', open);
		toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
	}

	// Mobile menu toggle.
	if (toggle && nav) {
		toggle.addEventListener('click', function () {
			setOpen(!header.classList.contains('nav-open'));
		});

		// Leaving the mobile breakpoint would strand the drawer open.
		mobile.addEventListener('change', function (e) {
			if (!e.matches) setOpen(false);
		});

		document.addEventListener('keydown', function (e) {
			if (e.key === 'Escape' && header.classList.contains('nav-open')) {
				setOpen(false);
				toggle.focus();
			}
		});

		// Tap-to-open submenus on touch / small screens.
		nav.querySelectorAll('.menu-item-has-children > a').forEach(function (link) {
			link.addEventListener('click', function (e) {
				if (mobile.matches) {
					e.preventDefault();
					link.parentElement.classList.toggle('is-open');
				}
			});
		});

		// Close the mobile menu after picking an in-page link — but not when the
		// link is a submenu parent, which is only expanding its children.
		nav.querySelectorAll('a[href^="#"]').forEach(function (link) {
			var isParent = link.parentElement.classList.contains('menu-item-has-children');
			link.addEventListener('click', function () {
				if (isParent && mobile.matches) return;
				setOpen(false);
			});
		});
	}

	// Fake subscribe confirmation (mirrors the original "Thanks for subscribing!").
	var form = document.querySelector('.subscribe__form');
	var note = document.querySelector('.subscribe__note');
	if (form && note) {
		form.addEventListener('submit', function (e) {
			e.preventDefault();
			if (!form.checkValidity()) { form.reportValidity(); return; }
			form.hidden = true;
			note.hidden = false;
		});
	}
})();
