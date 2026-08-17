# Saltwater 75 — Wix section embeds

Six self-contained sections, each designed to drop into its own Wix HTML embed.
Build the page top to bottom, one box at a time.

## Installing each one

1. Wix Editor → **Add (+) → Embed Code → Embed HTML**
2. Choose **Code**, paste the entire contents of the file
3. **Stretch the element to full width**
4. Set the **height** from the table below — this is the important part

Then repeat for the next section. Each is independent; add only the ones you want,
in whatever order suits the page.

## Do you want the nav to stick?

This is the one decision that changes the setup. **An embed can never be sticky** —
it's an iframe sitting in the page flow, so it scrolls away no matter how you slice
it. Splitting the nav into its own embed does not help; it just scrolls away in a
smaller box, and its dropdowns get clipped by the shorter box.

A sticky nav has to run in the real page DOM, which means Custom Code.

**Sticky nav (recommended)**

1. `../wix-navbar.html` → Settings → Custom Code → Body-start → All pages
2. In that file set `offsetContent: false` so the bar floats over the hero
   rather than sitting above it
3. Use `01-hero.html` as the first embed — hero photo only, no nav baked in
4. Then `02`–`06` below it

The nav hides Wix's header *and* the mobile Quick Action Bar for you, and it stays
pinned while the page scrolls.

**No Custom Code**

Use `00-top.html` instead — nav and hero in one block. Everything works except the
sticking; the bar scrolls away with the hero. Hide Wix's header manually in the
Editor.

### About `00-top.html`

It carries the nav bar **and** the hero background as a single block, which is how
the design is meant to look — the menu sitting over the photo rather than stacked
above it. It also fixes the problem a standalone nav embed has: because the hero
box is tall, the Store and Contact dropdowns have room to open *inside* it instead
of being clipped at the edge.

Place it at the very top of the page, and **hide Wix's own header in the Editor**
or you'll have two navs.

`01-hero.html` is the hero on its own, for the case where you'd rather keep Wix's
native menu. **Use one or the other — not both.**

## Box heights

Wix embeds do **not** grow to fit their contents. Too short and the section is cut
off; too tall and you get a dead gap. These are measured, not estimated — the
content height at each width plus a small buffer.

| # | Section | Desktop | Mobile editor |
|---|---------|--------:|--------------:|
| 00 | **Top — nav + hero** | **700** | **620** |
| 01 | Hero only (alternative) | 600 | 540 |
| 02 | About | 470 | 660 |
| 03 | Hours + Address | 540 | 760 |
| 04 | Gallery | 840 | 850 |
| 05 | Shop | 750 | 1370 |
| 06 | Reviews | 660 | 1010 |

Set the mobile heights separately in Wix's **mobile editor** — stacked layouts are
much taller than the desktop ones, and Shop nearly doubles.

If you edit the text in a section, re-check its height. Adding a sentence can push
content past the box edge, and it fails silently.

## Things to know

**Links.** Every internal link uses `target="_top"` so it navigates the whole site
rather than loading inside the little box. If you add links, do the same or they
will open the site inside the frame.

**Search visibility.** Text inside an embed is attributed to the frame, not to your
Wix page, so Google effectively sees these sections as empty. It doesn't matter much
for the gallery or hero, but it does for:

- **02-about** — real body copy about the restaurant
- **03-hours** — hours and address, which feed local search

Keep your hours and address in Wix's own business info regardless, and consider
building the About section natively in Wix if search traffic matters to you.

**Images** are hot-linked from `static.wixstatic.com`, the same as your live site.
They keep working while your Wix plan is active. If you ever leave Wix, these break
along with everything else pointing at that CDN.

**Gift cards.** In `05-store.html`, the digital gift card button goes to **Toast**,
not Wix. Toast is your point-of-sale, so a card it issues can be redeemed at the
register — one sold anywhere else could not be. Don't repoint that button at Wix.

**No sticky behaviour.** These are boxes in the page; they scroll normally. The
nav bar is the one piece that wants to be sticky, and an embed can't do that — see
`../wix-navbar.html` (Custom Code) if you want a sticky nav later.
