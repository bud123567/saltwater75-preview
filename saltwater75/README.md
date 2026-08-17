# Saltwater 75 — WordPress Theme

A WordPress theme that recreates [saltwater75.com](https://www.saltwater75.com) (Ocean City, MD — bayfront dining). It ships with a **sticky navigation bar** and pulls **all imagery from the original site's Wix CDN** (`static.wixstatic.com`), so no image files are bundled.

## What's inside

```
saltwater75/
├── style.css        Theme header + full stylesheet (coastal palette, sticky nav, responsive)
├── functions.php    Enqueues, menu registration, image map, fallback menu
├── header.php       Sticky header + logo + primary nav
├── front-page.php   Homepage: hero, about, hours/contact, gallery, reviews, mailing list
├── footer.php       Footer, social icons, © line
├── index.php        Generic fallback template
├── page.php         Template for static pages you create in WP
├── js/nav.js        Sticky-on-scroll state, mobile menu, dropdowns, subscribe confirm
└── README.md
```

## Install

1. Zip the **inner `saltwater75/` folder** (the folder that contains `style.css`):
   ```
   cd saltwater75-wordpress
   zip -r saltwater75.zip saltwater75
   ```
   (A ready-made `saltwater75.zip` is already in this folder.)
2. In WordPress admin: **Appearance → Themes → Add New → Upload Theme**, choose `saltwater75.zip`, then **Activate**.
3. Visit the front of the site. The homepage renders automatically via `front-page.php`.

### Optional
- **Set the homepage explicitly:** Settings → Reading → *Your homepage displays: A static page* (only needed if you'd rather assign a specific page; `front-page.php` already takes priority by default).
- **Real menu:** Appearance → Menus → create a menu → assign it to the **Primary Menu** location. Until you do, the theme shows a built-in fallback menu that mirrors saltwater75.com (Home, Happy Hour, Menu, Store ▾, Entertainment, Contact ▾, More).
- **Logo:** Appearance → Customize → Site Identity to swap the custom logo (defaults to the original glowing SW logo).

## The store

Saltwater 75 does not run its own checkout, and this theme deliberately doesn't add one. Their commerce is split across two systems:

| What | Runs on | Where |
|---|---|---|
| Merch — tees, hoodies, hats, accessories | **Wix Stores** | `saltwater75.com/shop-2` and category pages |
| **Digital** gift cards | **Toast** (their restaurant POS) | `toasttab.com/saltwater-75-115-75th-st/giftcards` |
| **Physical** gift cards, AlleyOops game card | Wix Stores | `saltwater75.com/giftcards` |

Digital gift cards have to stay on Toast. Toast is the point-of-sale in the restaurant, so a card it issues is redeemable at the register — a card sold by WordPress would not be. The theme therefore links out to both systems rather than reimplementing a cart.

Everything is configured in one place, `saltwater75_store()` in `functions.php`. It feeds both the Store dropdown in the nav and the Store section on the front page, so adding or renaming a category is a single edit.

> **⚠️ Before pointing this site at `saltwater75.com`**
>
> The store URLs live on that domain. If WordPress takes it over, they resolve to *this* site — which has no store — and every store link breaks. Move the shop to a subdomain (e.g. `shop.saltwater75.com`) and update `$base` in `saltwater75_store()`. Nothing else needs editing.
>
> The same applies to imagery: every image is hot-linked from `static.wixstatic.com`. Cancelling Wix takes the whole site's images with it. Self-host them (see the note below) before dropping the Wix plan.

If you'd rather bring commerce into WordPress later, WooCommerce is the path: their catalog is ~20 simple products with no complex variants. Gift cards would still need to stay on Toast.

## Notes

- **Sticky nav:** the header is `position: fixed` and gains a solid/blurred background + shrinks once you scroll past ~40px (`js/nav.js` toggles `.is-scrolled`).
- **Images:** hot-linked from `static.wixstatic.com`. They load as long as the original site keeps them public. To self-host, download them and drop the local URLs into the `saltwater75_images()` map in `functions.php`.
- The mailing-list form is front-end only (shows "Thanks for subscribing!"). Wire it to your provider (e.g. Mailchimp shortcode) to actually collect emails.
- Content (about text, hours, address, phone, five reviews) is transcribed from the live site as of build time.
