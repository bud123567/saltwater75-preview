/*
 * Wix Velo — size an HTML embed to the page inside it.
 * =============================================================================
 * Paste this into the page's code panel in the Wix editor (Dev Mode on), and
 * change '#html1' to whatever the embed is called on that page.
 *
 * WHY IT EXISTS
 * An iframe cannot resize itself. Its height is whatever the host set, so when
 * the widget is taller than the page, the difference shows as a blank band
 * under the footer, and when it is shorter the footer gets clipped or the
 * frame grows a scrollbar of its own.
 *
 * Every Saltwater 75 page now measures itself and posts the number out:
 *
 *     { type: 'sw75:height', height: 5189, page: 'saltwater75-contact.html' }
 *
 * on load, and again whenever photos, fonts or a rotation change the answer.
 * This listens for that and sets the widget to match.
 *
 * IF box.height TURNS OUT NOT TO BE SETTABLE
 * Wix has changed what Velo lets you write over the years, so the assignment
 * is wrapped. If it throws, the height still gets logged and can be typed into
 * the editor by hand — the number is the useful part either way. The same
 * number is logged by the page itself in the browser console:
 *
 *     [Saltwater 75] content height: 5189px
 *
 * Read it on a phone-sized window for the mobile height, and on a desktop one
 * for the desktop height; Wix keeps those two separately.
 */

$w.onReady(function () {
	var box = $w('#html1');            // <- the embed's ID on this page

	box.onMessage(function (event) {
		var data = event.data;
		if (!data || data.type !== 'sw75:height') return;

		var h = Math.ceil(data.height);
		if (!(h > 0)) return;

		try {
			box.height = h;
		} catch (e) {
			console.log('Saltwater 75: set this embed to ' + h + 'px by hand — '
			          + 'Velo would not set it here (' + e.message + ')');
		}
	});
});
