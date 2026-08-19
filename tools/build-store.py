#!/usr/bin/env python3
"""
Build the store pages from one catalog.

    python3 tools/build-store.py

Writes six files, all generated, none meant to be hand-edited:

    saltwater75-store.html              the hub — every product, grouped
    saltwater75-store-tshirts.html      one page per category
    saltwater75-store-sweatshirts.html
    saltwater75-store-hats.html
    saltwater75-store-accessories.html
    saltwater75-store-giftcards.html
    saltwater75-store-navbar.html       the top-of-page Wix module: nav + banner

CATALOG below is the only place the products live, so the hub and the five
category pages cannot drift apart. It is a snapshot of the Wix shop, read on
19 August 2026 — 43 products — and the prices are the part that will date
first. To refresh it, read the five category pages on saltwater75.com and
edit the lists here, then re-run. (The full catalog at /shop-2 pages at 20
items, so it takes three requests; the category pages do not.)

The shared chrome — tokens, header, nav, footer, the frame-scale and tel:
script — is not duplicated here. It is lifted at build time from
SHELL_SOURCE, so a fix made to the other pages reaches these too on the next
run. Only the store's own CSS and markup are written below.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SHELL_SOURCE = 'saltwater75-contact.html'

SHOP = 'https://www.saltwater75.com'
PRODUCT = SHOP + '/product-page/'
FULL_CATALOG = SHOP + '/shop-2'

# The store family shares a banner so the six pages read as one set: the hub
# gets the branded cup on the rail, the categories the tables out on the sand.
HUB_PHOTO = '8b7d81_fac878ca6621489296d01c593d187e87~mv2.jpg'
CAT_PHOTO = '8b7d81_fac94caea9154a1a8c82412cd26aa030~mv2.jpg'

# key, title, file, wix category, blurb, [(name, price, slug, image), ...]
CATALOG = [
 dict(key='tees', title='T-Shirts', file='saltwater75-store-tshirts.html',
      wix=SHOP + '/teeshirts',
      blurb='Every design in the shop, in mens, womens and youth cuts.',
      desc='Saltwater 75 t-shirts: 20 designs in mens, womens and youth cuts, '
           'from $18. Ocean City, Maryland.',
      items=[
  ("Nobody Remembers Tee - Short Sleeve","$25.00","nobody-remembers-tee-short-sleeve","8b7d81_369e8aec66a74673bd611d52b85ae684~mv2.jpg"),
  ("Sailing Rectanges","$25.00","sailing-rectanges","8b7d81_d02635931bbc4cb9ac08d44287ca95f2~mv2.jpg"),
  ("Waterlife Sketch","$25.00","waterlife-sketch","8b7d81_52297f97516c45f8b83c8f0a2357d322~mv2.jpg"),
  ("Fishin&rsquo; Boat","$25.00","fishin-boat","8b7d81_a2712a914a6a4c1291b9a94fc918a789~mv2.jpg"),
  ("Ol&rsquo; Salty Boy","$25.00","ol-salty-boy","8b7d81_4af492e1c7d64199a17a26c7f07e80ef~mv2.jpg"),
  ("But Did We Sink","$25.00","but-did-we-sink","8b7d81_0ee243a54fb746398ec28d7dbceb07cd~mv2.jpg"),
  ("Women&rsquo;s Saltwater &ldquo;Roughtime&rdquo; Tee","$25.00","women-s-saltwater-roughtime-tee","8b7d81_dc93fd7c28084172bc0915fa7b2a7b61~mv2.png"),
  ("Stars &amp; Sails","$25.00","stars-sails","8b7d81_dec99fc1a42f45ba868908ce547565c7~mv2.png"),
  ("SW75 Regatta","$25.00","sw75-regatta","8b7d81_d7606546b37c40d899235680cddd6c8d~mv2.png"),
  ("Sunset Waves &mdash; Women&rsquo;s","$25.00","sunset-waves-women-s-t-shirt","8b7d81_57b08d95d9db4d40ad7cd947dd6f2675~mv2.png"),
  ("Beach House Boat &mdash; Men&rsquo;s","$25.00","beach-house-boat-men-s-t-shirt","8b7d81_a6375bc1ed3d4cd29330d0331d3e49e4~mv2.png"),
  ("Regatta Flag &mdash; Men&rsquo;s","$25.00","regatta-flag-men-s-t-shirt","8b7d81_7dfaf642c16d4096ab43b14e090c3036~mv2.png"),
  ("Sun &amp; Waves Tie Dye &mdash; Men&rsquo;s","$25.00","sun-waves-tie-dye-men-s-t-shirt","8b7d81_25bfcf51d39f437693e57ff2dffa0d5b~mv2.avif"),
  ("Man Myth Legend &mdash; Men&rsquo;s","$25.00","man-myth-legend-men-s-t-shirt","8b7d81_eb110d298bbb434b86c5e5380d8f1c26~mv2.png"),
  ("Plan for Sailing &mdash; Men&rsquo;s","$25.00","plan-for-sailing-men-s-t-shirt","8b7d81_935683190f8e499a80c53c6022ab335a~mv2.png"),
  ("Trust Me I&rsquo;m the Captain &mdash; Men&rsquo;s","$25.00","t-shirt-1","8b7d81_8d22aa7cd3df47adb823024dd20b806a~mv2.png"),
  ("In The Wind &mdash; Women&rsquo;s","$25.00","in-the-wind-women-s-t-shirt","8b7d81_faec0efdcea34952ae9f03f645b8394a~mv2.png"),
  ("Waves &mdash; Women&rsquo;s","$22.00","waves-men-s-t-shirt","8b7d81_fec66a755de84372a007e9ca9f8addd2~mv2.png"),
  ("That B Pyrates &mdash; Youth","$18.00","that-b-pyrates-youth-t-shirt","8b7d81_7f02d7b9d96c41daaa1edeef2c24ee36~mv2.png"),
  ("Colorful Waves &mdash; Youth","$18.00","colorful-waves-youth-t-shirt","8b7d81_a2c78cba264948c4830baf509ae44cb8~mv2.png"),
      ]),
 dict(key='tops', title='Long Sleeve + Sweatshirts', file='saltwater75-store-sweatshirts.html',
      wix=SHOP + '/shop-5',
      blurb='For when the wind comes off the bay after dark.',
      desc='Saltwater 75 hoodies, a pullover and a performance long sleeve, '
           '$25 to $38, for when the wind comes off the bay.',
      items=[
  ("But Did We Sink Hoodie","$38.00","but-did-we-sink-hoodie","8b7d81_d59765ff7bb04eeeaf5c606559b5304e~mv2.jpg"),
  ("Saltwater 75 Hoodie &mdash; Plans for Sailing","$38.00","saltwater-75-hoodie-plans-for-sailing","8b7d81_301badf670084c90aefb9ff77fa65a06~mv2.png"),
  ("Saltwater 75 Pullover &mdash; Ivy League","$38.00","saltwater-75-pullover-ivy-league","8b7d81_a105c8ceb0ee4cd1a23130fe4151051e~mv2.png"),
  ("Burgee &mdash; Men&rsquo;s Performance Long Sleeve","$25.00","burgee-men-s-long-sleeve","8b7d81_469085d7afe2455c9b3c393cb7bd6bcb~mv2.png"),
      ]),
 dict(key='hats', title='Hats', file='saltwater75-store-hats.html',
      wix=SHOP + '/hats',
      blurb='One in the shop right now.',
      desc='The Saltwater 75 trucker hat, $25, from the shop on 75th Street '
           'in Ocean City, Maryland.',
      items=[
  ("Saltwater 75 &mdash; Trucker Hat","$25.00","saltwater-75-trucker-hat","8b7d81_aca3f4cd3ce24c8bb1cf617dd72ffc8d~mv2.png"),
      ]),
 dict(key='accessories', title='Accessories', file='saltwater75-store-accessories.html',
      wix=SHOP + '/accessories',
      blurb='Tumblers, bags and bar gear &mdash; the small stuff that ends up on the boat.',
      desc='Saltwater 75 tumblers, cooler bags, totes, koozies, bottle openers '
           'and bar gear, from $2.',
      items=[
  ("SW Navy Tumbler","$55.00","sw-navy-tumbler","8b7d81_ed6a3f8dcbc74d71aa6632df8418d88b~mv2.jpg"),
  ("Saltwater 75 Cooler Bag","$40.00","saltwater-75-cooler-bag","8b7d81_a25a219f8b14490bb9c4a6583085d5d7~mv2.png"),
  ("Saltwater 75 Canvas Tote","$40.00","saltwater-75-canvas-tote","8b7d81_eef0b7a07b8b444eae06ce37c3b97bfa~mv2.png"),
  ("Saltwater 75 &mdash; Water Bottle","$20.00","saltwater-75-water-bottle","8b7d81_bb22cccffd0d43a0824bfdd7baa581d4~mv2.jpg"),
  ("Saltwater 75 Umbrella","$19.00","saltwater-75-umbrella","8b7d81_a30d55899091476f843b2c002ff977c4~mv2.png"),
  ("Saltwater 75 Dry Bag","$18.00","saltwater-75-dry-bag","8b7d81_38881f6388124a7ab15022fc94746398~mv2.png"),
  ("Saltwater 75 &mdash; Floating Key Ring","$7.50","saltwater-75-floating-key-ring","8b7d81_82883ab724904cf5ac0ced98d4ef9757~mv2.png"),
  ("Beer Bottle Opener","$7.00","beer-bottle-opener","8b7d81_87ae1739b4fe49d2aa73d9f1fc4b4531~mv2.jpg"),
  ("Saltwater 75 Splash Proof Phone Pouch","$6.00","saltwater-75-splash-proof-phone-pouch","8b7d81_9c04249681994559b631b14cd7a6233d~mv2.png"),
  ("Saltwater 75 &mdash; Sling Bag","$5.00","saltwater-75-sling-bag","8b7d81_22750cf643014a86af5de5c10a5804f9~mv2.png"),
  ("Saltwater 75 &mdash; Cork Screw / Bottle Opener Combo","$5.00","saltwater-75-cork-screw-bottle-opener-combo","8b7d81_8f2c30ba248740a4925bf4c97b725b90~mv2.png"),
  ("Saltwater 75 Sunglasses","$4.00","saltwater-75-sunglasses","8b7d81_d9951a2fc5a346c88fafa4eda2aeb2ec~mv2.png"),
  ("Saltwater 75 Coozie","$2.00","saltwater-75-coozie","8b7d81_df9a8ff8d45f4f6983b069c29e71bc9f~mv2.png"),
      ]),
 dict(key='giftcards', title='Gift Cards + AO Game Card', file='saltwater75-store-giftcards.html',
      wix=SHOP + '/giftcards',
      blurb='Saltwater 75, Ropewalk and AlleyOops &mdash; digital or physical.',
      desc='Gift cards for Saltwater 75, Ropewalk and AlleyOops, plus the '
           'AlleyOops game card. Digital or physical.',
      items=[
  # The shop lists the digital card at $0.00 because the amount is chosen at
  # checkout. Printing "$0.00" here would read as a bug, so it says so instead.
  ("Saltwater75 Gift Card &mdash; Digital","Choose an amount","saltwater75-gift-card-digital","8b7d81_a089d0aa5d044f0d8bca778630ada891~mv2.jpg"),
  ("Saltwater 75 Gift Card &mdash; Physical","$5.00","saltwater-75-gift-card","8b7d81_a089d0aa5d044f0d8bca778630ada891~mv2.jpg"),
  ("Ropewalk Gift Cards","$50.00","ropewalk-gift-cards","8b7d81_4bdc7e7a6acc4cb890089cd4d810e0a4~mv2.jpg"),
  ("AlleyOops Gift Card","$5.00","alleyoops-gift-card","8b7d81_cdfc0adf9c4b406ba8892f93bbecee56~mv2.png"),
  ("AlleyOops Game Card","$5.00","alleyoops-game-card","8b7d81_ca641c646c5a4eb5810d442e4e8ee7a3~mv2.jpg"),
      ]),
]

STORE_DESC = ('The Saltwater 75 shop: tees, hoodies, hats, tumblers, bar gear and gift '
              'cards for Saltwater 75, Ropewalk and AlleyOops. 43 items, with prices.')

# The top-of-page Wix modules: same bar, same banner photo, different words.
# The cart one is a copy of the store one — the cart itself is Wix's, and goes
# in underneath as its own element.
MODULES = [
 dict(title='Store', file='saltwater75-store-navbar.html', current=True,
      lede='Tees, hoodies, hats and bar gear &mdash; plus gift cards for '
           'Saltwater 75, Ropewalk and AlleyOops.',
      desc='The Saltwater 75 store: tees, hoodies, hats, tumblers, bar gear and '
           'gift cards, from the bar at 115 75th Street, Ocean City.'),
 dict(title='Cart', file='saltwater75-cart-navbar.html', current=False,
      lede='Everything you have picked out, ready when you are.',
      desc='Your Saltwater 75 cart.'),
]

PHONE_ICON = ('<svg class="icon" viewBox="0 0 512 512" aria-hidden="true" focusable="false">'
 '<path d="M164.9 24.6c-7.7-18.6-28-28.5-47.4-23.2l-88 24C12.1 30.2 0 46 0 64c0 247.4 '
 '200.6 448 448 448 18 0 33.8-12.1 38.6-29.5l24-88c5.3-19.4-4.6-39.7-23.2-47.4l-96-40c-16.3'
 '-6.8-35.2-2.1-46.3 11.6L304.7 368C234.3 334.7 177.3 277.7 144 207.3L193.3 167c13.7-11.2 '
 '18.4-30 11.6-46.3l-40-96z"/></svg>')

MAPS = ('https://www.google.com/maps/search/?api=1&amp;query=115+75th+Street+Ocean+City+MD+21842')


# --------------------------------------------------------------------------
# SEO
# --------------------------------------------------------------------------

FAVICON = ('https://static.wixstatic.com/media/c57fb0_ff950f6488bf48a5b535d179ea75521a'
           '~mv2.png/v1/fit/w_180,h_180,q_90/saltwater75-icon.png')
OG_IMAGE = ('https://static.wixstatic.com/media/8b7d81_4578ab8a85194bbf8a068a0aa2a69166'
            '~mv2.jpg/v1/fill/w_1200,h_630,al_c,q_85/saltwater75-og.jpg')


def seo(title, desc, canonical=None, noindex=False):
    """The head's SEO block, in the same shape and order the hand-written pages
       carry it. canonical and noindex are never both set: a page told not to be
       indexed has no credit left to hand anywhere.

       Worth knowing where this does and does not reach. Pasted into a Wix HTML
       embed, none of it is the page's SEO — the embed is an iframe with a head
       of its own, and Wix's own SEO panel owns the page. It counts when one of
       these URLs is crawled or shared directly, which is what the hosted copies
       are for."""
    out = ['<!-- SEO -->', '<title>%s</title>' % title,
           '<meta name="description" content="%s">' % desc]
    out.append('<meta name="robots" content="noindex, follow">' if noindex
               else '<link rel="canonical" href="%s">' % canonical)
    out += ['<link rel="icon" href="%s" type="image/png">' % FAVICON,
            '<meta property="og:type" content="website">',
            '<meta property="og:site_name" content="Saltwater 75">',
            '<meta property="og:title" content="%s">' % title,
            '<meta property="og:description" content="%s">' % desc]
    if canonical:
        out.append('<meta property="og:url" content="%s">' % canonical)
    out += ['<meta property="og:image" content="%s">' % OG_IMAGE,
            '<meta property="og:image:width" content="1200">',
            '<meta property="og:image:height" content="630">',
            '<meta property="og:image:alt" content="The deck at Saltwater 75, looking out over the bay">',
            '<meta name="twitter:card" content="summary_large_image">',
            '<!-- /SEO -->']
    return '\n'.join(out)


# --------------------------------------------------------------------------
# the shared chrome, lifted from a page that already has it
# --------------------------------------------------------------------------

def shell():
    src = open(os.path.join(ROOT, SHELL_SOURCE)).read()

    def between(a, b):
        i = src.index(a); j = src.index(b, i); return src[i:j]

    # everything above the source page's OWN section CSS: tokens, chrome,
    # responsive rules, the subpage banner and the closing CTA
    head = src[:src.index('/* ---------- Contact: the three ways in ---------- */')]
    a = head.index('<!-- SEO -->')
    b = head.index('<!-- /SEO -->') + len('<!-- /SEO -->')
    head = (head[:a], head[b:])          # the contact page's own block drops out
    header = between('<a class="skip-link', '<main id="content"')
    footer = between('<footer id="colophon"', '\n\n<script>')
    script = src[src.index('<script>\n/**'):]
    script = script.replace(' * Saltwater 75 — contact page behaviour.',
                            ' * Saltwater 75 — store page behaviour.')

    # the source page marks itself as the current page; this family does not
    header = header.replace(
        '<li class="menu-item menu-item-has-children"><a href="#top" aria-current="page">Contact</a>',
        '<li class="menu-item menu-item-has-children"><a href="%s/contact" target="_blank" rel="noopener">Contact</a>' % SHOP)
    header = header.replace('<li class="menu-item"><a href="#hours">Hours &amp; Directions</a></li>',
        '<li class="menu-item"><a href="%s/contact" target="_blank" rel="noopener">Hours &amp; Directions</a></li>' % SHOP)
    return head, header, footer, script


def nav_for(page, wix=False, current=True):
    """Point the Store menu at this family rather than back out to Wix. `page`
       is a catalog entry, or None for the hub. `wix` is for the embedded
       module, where a relative filename would not resolve: there the menu goes
       to the real category pages on saltwater75.com instead."""
    def item(cat):
        if wix:
            return ('<a href="%s" target="_blank" rel="noopener">%s</a>'
                    % (cat['wix'], cat['title']))
        if page is not None and cat['key'] == page['key']:
            return '<a href="#top" aria-current="page">%s</a>' % cat['title']
        # The hub holds every category, so there its menu jumps down the page;
        # from a category page each sibling is a file of its own.
        href = '#' + cat['key'] if page is None else cat['file']
        return '<a href="%s">%s</a>' % (href, cat['title'])

    if wix:
        # The cart module's page is the cart, which is not a menu item — so
        # nothing in the bar is the current page there.
        store_link = ('<a href="#top" aria-current="page">Store</a>' if current
                      else '<a href="%s/shop" target="_blank" rel="noopener">Store</a>' % SHOP)
    else:
        store_link = ('<a href="#top" aria-current="page">Store</a>' if page is None
                      else '<a href="saltwater75-store.html">Store</a>')
    subs = '\n'.join('            <li class="menu-item">%s</li>' % item(c) for c in CATALOG)
    return ('<li class="menu-item menu-item-has-children">%s\n'
            '          <ul class="sub-menu">\n%s\n'
            '            <li class="menu-item"><a href="%s" target="_blank" rel="noopener">Full Catalog</a></li>\n'
            '          </ul>\n        </li>' % (store_link, subs, FULL_CATALOG))


def wire_nav(header, page, wix=False, current=True):
    """Swap the source page's whole Store menu for this page's version."""
    start = header.index('<li class="menu-item menu-item-has-children"><a href="%s/shop"' % SHOP)
    end = header.index('</li>', header.index('Full Catalog', start)) + len('</li>')
    # ...and one more, which closes the Store item itself. A third would take
    # the Entertainment link that follows it with it.
    end = header.index('</li>', end) + len('</li>')
    return header[:start] + nav_for(page, wix, current) + header[end:]


# --------------------------------------------------------------------------
# markup
# --------------------------------------------------------------------------

def shot(media):
    """Wix resizes on its own CDN: /v1/fit keeps the whole product in frame
       (no crop), and the trailing filename is ignored but required."""
    return ('https://static.wixstatic.com/media/%s/v1/fit/w_500,h_500,q_85/'
            'saltwater75.%s' % (media, media.rsplit('.', 1)[1]))


def alt(name):
    plain = (name.replace('&rsquo;', "'").replace('&mdash;', '—').replace('&amp;', '&')
                 .replace('&ldquo;', '"').replace('&rdquo;', '"'))
    return plain.replace('"', '&quot;')


def card(p):
    name, price, slug, media = p
    cls = 'product__price' + ('' if price.startswith('$') else ' product__price--note')
    return ('        <a class="product" href="%s%s" target="_blank" rel="noopener">\n'
            '          <span class="product__shot"><img src="%s" alt="%s" loading="lazy" decoding="async"></span>\n'
            '          <span class="product__body">\n'
            '            <span class="product__name">%s</span>\n'
            '            <span class="%s">%s</span>\n'
            '          </span>\n'
            '        </a>\n' % (PRODUCT, slug, shot(media), alt(name), name, cls, price))


def grid(items):
    return '      <div class="shop-grid">\n%s      </div>\n' % ''.join(card(p) for p in items)


def chips(page):
    """Category chips. On a category page the current one is a marker rather
       than a link back to where you already are."""
    out = []
    for c in CATALOG:
        if page is not None and c['key'] == page['key']:
            out.append('        <span class="shop-chip shop-chip--here" aria-current="page">%s</span>' % c['title'])
        else:
            href = '#' + c['key'] if page is None else c['file']
            out.append('        <a class="shop-chip" href="%s">%s</a>' % (href, c['title']))
    if page is not None:
        out.append('        <a class="shop-chip" href="saltwater75-store.html">Everything</a>')
    return '\n'.join(out)


PRICE_NOTE = ('        Every item opens on our shop, where the sizes, colours and checkout live.\n'
              '        Prices are the ones showing there today &mdash; the product page is always the last word.')


def closing_cta():
    return '''  <section id="visit" class="section hh-cta">
    <div class="wrap">
      <div class="section__head">
        <p class="section__lede">Or pick any of it up in person &mdash; open daily 11:00am &ndash; 12:00am at 115 75th Street.</p>
      </div>
      <div class="hh-cta__actions">
        <a class="btn btn--solid reserve" href="tel:+14105247575" aria-label="Make a reservation — call 410-524-7575">
          %s
          <span class="reserve__label">Make a Reservation</span>
        </a>
        <a class="btn btn--ghost" href="%s" target="_blank" rel="noopener">Get Directions</a>
      </div>
    </div>
  </section>
''' % (PHONE_ICON, MAPS)


def hub_main():
    sections = []
    for i, c in enumerate(CATALOG):
        # The browse strip above is already --ink-2, so the first category has
        # to start on --ink or the two run together as one long band.
        band = ' shop-cat--alt' if i % 2 == 1 else ''
        sections.append('''  <section id="%s" class="section shop-cat%s">
    <div class="wrap">
      <div class="shop-cat__head">
        <div>
          <h2>%s</h2>
          <p class="shop-cat__blurb">%s</p>
        </div>
        <a class="shop-cat__all" href="%s" target="_blank" rel="noopener">All %s &#8599;</a>
      </div>
%s    </div>
  </section>
''' % (c['key'], band, c['title'], c['blurb'], c['wix'], c['title'], grid(c['items'])))

    return '''<main id="content" class="site-content">

  <section id="top" class="page-hero" style="--hero-img:url('https://static.wixstatic.com/media/%s');">
    <div class="wrap page-hero__inner">
      <h1 class="ent-title">Store</h1>
      <p class="ent-lede">Tees, hoodies, hats and bar gear &mdash; plus gift cards for Saltwater 75, Ropewalk and AlleyOops.</p>
    </div>
  </section>

  <section id="browse" class="section shop-browse">
    <div class="wrap">
      <div class="shop-nav">
%s
      </div>
      <p class="shop-browse__note">
%s
      </p>
      <div class="shop-browse__actions">
        <a class="btn btn--solid" href="%s" target="_blank" rel="noopener">Shop the Full Catalog</a>
      </div>
    </div>
  </section>

%s
%s
</main>
''' % (HUB_PHOTO, chips(None), PRICE_NOTE, FULL_CATALOG, ''.join(sections), closing_cta())


def cat_main(page):
    n = len(page['items'])
    count = 'One item' if n == 1 else '%d items' % n
    return '''<main id="content" class="site-content">

  <section id="top" class="page-hero" style="--hero-img:url('https://static.wixstatic.com/media/%s');">
    <div class="wrap page-hero__inner">
      <h1 class="ent-title">%s</h1>
      <p class="ent-lede">%s</p>
    </div>
  </section>

  <section id="browse" class="section shop-browse">
    <div class="wrap">
      <div class="shop-nav">
%s
      </div>
      <p class="shop-browse__note">
%s
      </p>
      <div class="shop-browse__actions">
        <a class="btn btn--solid" href="%s" target="_blank" rel="noopener">Shop %s on Our Site</a>
      </div>
    </div>
  </section>

  <section id="%s" class="section shop-cat">
    <div class="wrap">
      <div class="shop-cat__head">
        <div>
          <h2>%s</h2>
          <p class="shop-cat__blurb">%s in the shop today.</p>
        </div>
        <a class="shop-cat__all" href="saltwater75-store.html">Every category &rarr;</a>
      </div>
%s    </div>
  </section>

%s
</main>
''' % (CAT_PHOTO, page['title'], page['blurb'], chips(page), PRICE_NOTE,
       page['wix'], page['title'], page['key'], page['title'], count,
       grid(page['items']), closing_cta())


def module_main(title, lede):
    """The top-of-page module: the chrome and the banner, and nothing else."""
    return '''<main id="content" class="site-content">

  <section id="top" class="page-hero page-hero--module" style="--hero-img:url(\'https://static.wixstatic.com/media/%s\');">
    <div class="wrap page-hero__inner">
      <h1 class="ent-title">%s</h1>
      <p class="ent-lede">%s</p>
    </div>
  </section>

</main>
''' % (HUB_PHOTO, title, lede)


STORE_CSS = '''/* ---------- Store: browse strip ---------- */
.shop-browse { background: var(--ink-2); padding-block: clamp(2.5rem, 5vw, 3.5rem); text-align: center; }
.shop-nav { display: flex; flex-wrap: wrap; gap: .6rem; justify-content: center; }
.shop-chip {
	border: 1px solid var(--line); border-radius: 999px;
	padding: .5rem 1.05rem; font-size: .82rem; font-weight: 600;
	color: var(--sand); background: rgba(255,255,255,.04);
	transition: background .2s ease, color .2s ease, border-color .2s ease;
}
.shop-chip:hover, .shop-chip:focus-visible { background: var(--gold); color: var(--ink); border-color: var(--gold); }
/* The page you are already on: a marker, not a link back to itself. */
.shop-chip--here {
	background: rgba(232,160,75,.16); border-color: var(--gold); color: var(--gold-2);
	cursor: default;
}
.shop-browse__note {
	max-width: 40rem; margin: 1.5rem auto 0;
	color: var(--sand-dim); font-size: .88rem;
}
.shop-browse__actions { margin-top: 1.25rem; }

/* ---------- Store: a category ---------- */
.shop-cat--alt { background: var(--ink-2); }
.shop-cat__head {
	display: flex; align-items: flex-end; justify-content: space-between;
	gap: 1rem 1.5rem; flex-wrap: wrap;
	border-bottom: 1px solid var(--line); padding-bottom: 1rem;
	margin-bottom: clamp(1.5rem, 3vw, 2.25rem);
}
.shop-cat__head h2 { margin: 0; font-size: clamp(1.6rem, 3.4vw, 2.4rem); }
.shop-cat__blurb { margin: .35rem 0 0; color: var(--sand-dim); font-size: .92rem; }
.shop-cat__all {
	font-size: .78rem; font-weight: 600; letter-spacing: .08em;
	text-transform: uppercase; color: var(--gold); white-space: nowrap;
}

/* ---------- Store: the products ---------- */
.shop-grid {
	display: grid; gap: 1.15rem;
	grid-template-columns: repeat(auto-fill, minmax(13.5rem, 1fr));
}
.product {
	display: flex; flex-direction: column; overflow: hidden;
	background: rgba(255,255,255,.04); border: 1px solid var(--line);
	border-radius: var(--radius); color: var(--sand);
	transition: transform .2s ease, border-color .2s ease, background .2s ease;
}
.product:hover, .product:focus-visible {
	transform: translateY(-4px); border-color: var(--gold);
	background: rgba(232,160,75,.08); color: var(--sand);
}
/* The shop photographs everything on white, so the tile is white too — a cream
   one would show the photo's own background as a paler rectangle inside it.
   `contain` over `cover`: a tee cropped square loses the print, which is the
   only thing telling one of these apart from the next. */
.product__shot {
	position: relative; display: block; flex: none;
	aspect-ratio: 1 / 1; background: #fff;
}
/* Absolutely positioned, so the photo's own proportions cannot feed back into
   the tile. In flow it did: a percentage height inside an aspect-ratio box is
   circular, the browser fell back to the image's natural height, and one row
   of tees came out with white squares of five different heights. */
.product__shot img {
	position: absolute; inset: .55rem;
	width: calc(100% - 1.1rem); height: calc(100% - 1.1rem);
	object-fit: contain;
}
.product__body {
	display: flex; flex-direction: column; gap: .3rem; flex: 1;
	padding: .85rem 1rem 1.05rem;
}
.product__name {
	font-family: var(--head); font-size: 1rem; font-weight: 600; line-height: 1.28;
}
/* Pinned to the bottom so the prices line up across a row of ragged names. */
.product__price { margin-top: auto; padding-top: .35rem; color: var(--gold-2); font-weight: 600; font-size: .95rem; }
.product__price--note { color: var(--sand-dim); font-weight: 500; font-size: .86rem; }

@media (max-width: 520px) {
	.shop-grid { grid-template-columns: repeat(auto-fill, minmax(9.5rem, 1fr)); gap: .8rem; }
	.product__name { font-size: .92rem; }
	.shop-browse__actions .btn { width: 100%; max-width: 18.125rem; }
}

/* ---------- The module's bar, a size up -----------------------------------
   On a full page the bar takes its scale from everything under it. Alone at
   the top of a Wix page it reads small, so the module runs a size up: logo,
   links, the reservation button, the burger and the drawer rows. Scoped to
   .is-module throughout, so the six store pages keep the size the rest of the
   site uses. */
.is-module .site-logo img { height: 4.6rem; }
.is-module .site-header.is-scrolled .site-logo img { height: 3.6rem; }
.is-module .utility__item { font-size: .86rem; }
.is-module .utility__item .icon { width: .82rem; height: .82rem; }
.is-module .site-header__actions .btn--sm.reserve { font-size: .9rem; padding: .7rem 1.35rem; }

/* Between 1025 and 1250 the menu is already tightening to stay on one line
   beside the logo, so only grow the links where there is room to. */
@media (min-width: 1251px) {
	.is-module .main-navigation a { font-size: 1.02rem; padding: .6rem .95rem; }
}

@media (max-width: 1024px) {
	.is-module .nav-toggle { width: 3.1rem; height: 2.9rem; }
	.is-module .nav-toggle__bar { height: 3px; margin: .38rem 0; }
	/* The X has to travel one bar pitch, and the pitch just changed: 3px bar
	   plus a .38rem gap is 9, where the stock bar's 2px and .3125rem was 7. */
	.is-module .nav-open .nav-toggle__bar:nth-child(1) { transform: translateY(9px) rotate(45deg); }
	.is-module .nav-open .nav-toggle__bar:nth-child(3) { transform: translateY(-9px) rotate(-45deg); }

	/* Clears the taller header the bigger logo makes. */
	.is-module .main-navigation { padding-top: 8.25rem; }
	.is-module .main-navigation .menu > .menu-item > a { font-size: 1.06rem; padding: .95rem .7rem; }
	.is-module .main-navigation .sub-menu a { font-size: .98rem; padding: .62rem .8rem; }
}

/* ---------- The top-of-page module ---------------------------------------
   This banner is the whole module below the header, and on a phone its job is
   as much structural as visual: the drawer is position:fixed, and inside an
   embed that resolves against the WIDGET box rather than the phone screen. A
   short widget therefore gives a short menu, with the six items scrolling
   inside a strip. Standing the banner up to a real height means a widget sized
   to this module has the room for the menu to open down into.

   Desktop is left alone — the menu is a row up in the bar, needing no height
   underneath it at all. */
@media (max-width: 700px) {
	.page-hero--module {
		/* Sized against the drawer rather than picked for looks. Opened, the
		   six items and their padding measure ~31.8rem at the size the bar
		   runs above, and the banner's own padding is in vw, which collapses
		   to nothing at phone widths — so without a floor the module ends up
		   shorter than the menu it has to hold. Both are in rem, so the
		   frame-scale correction shrinks them together and the margin holds.
		   Re-measure this if the drawer rows ever change size again. */
		min-height: 34rem;
		display: grid; align-content: center;
		padding-block: clamp(7.5rem, 15vw, 9rem) clamp(2.5rem, 6vw, 3.5rem);
	}
}
'''


MODULE_COMMENT = """<!--
  ===========================================================================
  SALTWATER 75 — %s / TOP-OF-PAGE MODULE (single file)
  ===========================================================================
  GENERATED by tools/build-store.py — an edit made here is lost the next time
  that runs.

  The contact strip, the header, the nav and the %s banner, and then it
  stops. Meant to be pasted into a Wix HTML embed at the TOP of that page,
  with the page's real content going in underneath as its own module — the
  products, or Wix's own cart.

  There is no footer here: saltwater75-footer.html is that, as its own
  module at the bottom of the page.

  Every link goes to saltwater75.com rather than to a file beside this one,
  because inside a Wix embed a relative filename does not resolve.

  Give the widget its height in Wix — a frame cannot grow itself, and here
  the height is doing real work. The mobile menu is position:fixed, which
  inside an embed resolves against the WIDGET box, not the phone screen: a
  300px-tall widget gives a 300px-tall drawer with six items scrolling in a
  strip. The banner below the bar is what buys that room.

  The module measures 563px at both 500px and 1280px wide, so:
    • phone   — 590px
    • desktop — 590px
  If the open menu still scrolls inside the widget, raise the phone one; it
  can never be too tall, since the banner is the same colour underneath.

  Still loaded from the internet:
    • Google Fonts  — Playfair Display + Montserrat
    • Photo         — hot-linked from static.wixstatic.com
  ===========================================================================
-->"""


def file_comment(title, body):
    return '''<!--
  ===========================================================================
  SALTWATER 75 — %s
  ===========================================================================
  GENERATED by tools/build-store.py — an edit made here is lost the next time
  that runs. The products, the prices and this page's shape all live there.

  Everything is in this one document: markup, all CSS, all JavaScript. No
  local files needed — double-click it, or drop it on any host as-is.

%s
  Nothing on this page sells anything: every card is a link through to its own
  product page on saltwater75.com, where the sizes, the stock and the checkout
  live. The catalog is a snapshot read on 19 August 2026, and the prices are
  the part that will date first.

  Links between these six store pages are relative filenames, so they work
  side by side on any host. Pasted into a Wix HTML embed they will not
  resolve — point them at the Wix category pages instead, or link the hosted
  copies by their full URL.

  Still loaded from the internet:
    • Google Fonts  — Playfair Display + Montserrat
    • Photos        — hot-linked from static.wixstatic.com, resized by URL
                      (/v1/fit keeps the whole product in frame, uncropped)
  ===========================================================================
-->''' % (title, body)


def write(path, seo_block, comment, main, page, wix=False, with_footer=True,
          body_class='', current=True):
    (head_a, head_b), header, footer, script = shell()
    head = head_a + seo_block + head_b
    body = '<body class="%s">' % body_class if body_class else '<body>'
    doc = (head + STORE_CSS + '</style>\n' + comment + '\n</head>\n' + body + '\n'
           + wire_nav(header, page, wix, current) + '\n' + main + '\n'
           + (footer + '\n\n' if with_footer else '') + script)
    open(os.path.join(ROOT, path), 'w').write(doc)
    return len(doc)


def main():
    total = len(CATALOG)
    n = write('saltwater75-store.html',
              seo('Store | Saltwater 75 &mdash; Ocean City, MD', STORE_DESC,
                  canonical=SHOP + '/shop'),
              file_comment('STORE (single file)',
  '''  The whole shop on one page: %d products in %d categories, each grouped the
  way the shop groups them. One page per category sits alongside this one —
  see the Store menu, or tools/build-store.py for the list.
''' % (sum(len(c['items']) for c in CATALOG), total)),
              hub_main(), None)
    print('saltwater75-store.html  %6d bytes  %d products' %
          (n, sum(len(c['items']) for c in CATALOG)))

    for c in CATALOG:
        n = write(c['file'],
                  seo('%s | Saltwater 75 &mdash; Ocean City, MD' % c['title'],
                      c['desc'], canonical=c['wix']),
                  file_comment('STORE / %s (single file)' % c['title'].upper(),
  '''  One category out of the shop: %s. The hub at saltwater75-store.html
  carries all %d products across every category.
''' % (c['title'], sum(len(x['items']) for x in CATALOG))),
                  cat_main(c), c)
        print('%-34s %6d bytes  %d products' % (c['file'], n, len(c['items'])))

    for m in MODULES:
        n = write(m['file'],
                  seo('%s | Saltwater 75' % m['title'], m['desc'], noindex=True),
                  MODULE_COMMENT % (m['title'].upper(), m['title']),
                  module_main(m['title'], m['lede']), None,
                  wix=True, with_footer=False, body_class='is-module',
                  current=m['current'])
        print('%-34s %6d bytes  nav + banner, no footer' % (m['file'], n))


if __name__ == '__main__':
    main()
