<?php
/**
 * Saltwater 75 theme functions.
 *
 * @package Saltwater75
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // No direct access.
}

define( 'SALTWATER75_VERSION', '1.0.0' );

/**
 * Images are hot-linked from the original site's Wix CDN, as requested.
 * Central map so the URLs live in one place. Use saltwater75_img( 'key' ).
 */
function saltwater75_images() {
	$base = 'https://static.wixstatic.com/media/';
	return array(
		'logo'      => $base . 'c57fb0_ff950f6488bf48a5b535d179ea75521a~mv2.png', // swlogoglow.png
		// Sunset over the bay — matches the "best sunset view in Ocean City" line.
		'hero'      => $base . '8b7d81_20399a78150d4aa5bd46b15175849306~mv2.jpg',
		'about'     => $base . '8b7d81_f8c20e63681c48e1a9abb79a7f5e4756~mv2.jpg', // DSC00335
		'gallery_1' => $base . '8b7d81_fac878ca6621489296d01c593d187e87~mv2.jpg',
		'gallery_2' => $base . '8b7d81_f1665d67599d4baba7a5aa082cd31c27~mv2.jpg',
		// took the hero's old food spread, since the sunset shot moved up there
		'gallery_3' => $base . '8b7d81_9e0c692749f1458fac87316b08175b36~mv2.jpg',
		'gallery_4' => $base . '8b7d81_4578ab8a85194bbf8a068a0aa2a69166~mv2.jpg',
		'gallery_5' => $base . '8b7d81_fac94caea9154a1a8c82412cd26aa030~mv2.jpg',
		'gallery_6' => $base . '8b7d81_6236fb9170a1446585495d1908d55e1e~mv2.jpg',
		'gallery_7' => $base . '8b7d81_d75404662ebc4e53810e158d04ebcdf7~mv2.jpg',
		'gallery_8' => $base . '8b7d81_922685b962d5451d91b0b89b36ba2106~mv2.jpg',
	);
}

function saltwater75_img( $key ) {
	$images = saltwater75_images();
	return isset( $images[ $key ] ) ? esc_url( $images[ $key ] ) : '';
}

/**
 * Contact details in one place — the header bar, the reservation CTA and the
 * footer all read from here, so the number only ever changes once.
 */
function saltwater75_contact() {
	return array(
		'phone_display' => '410-524-7575',
		'phone_tel'     => '+14105247575',
		'street'        => '115 75th Street',
		'city'          => 'Ocean City, MD 21842',
		'map_url'       => 'https://www.google.com/maps/search/?api=1&query=115+75th+Street+Ocean+City+MD+21842',
	);
}

/**
 * Where the store actually lives.
 *
 * Saltwater 75 does not run its own checkout. Merch is sold through Wix Stores
 * on the live domain, and digital gift cards are issued by Toast — the
 * restaurant's POS — so they stay there by necessity: a gift card sold by
 * WordPress could not be redeemed at the register. Physical gift cards and the
 * AlleyOops game card are ordinary Wix products.
 *
 * So the theme links out rather than reimplementing a cart.
 *
 * HEADS UP: these Wix URLs sit on saltwater75.com. If WordPress ever takes over
 * that domain, they will resolve to this site — which has no store — and every
 * store link breaks. Move the shop to a subdomain (e.g. shop.saltwater75.com)
 * and change $base here; nothing else in the theme needs editing.
 */
function saltwater75_store() {
	$base = 'https://www.saltwater75.com';

	return array(
		'base'    => $base,
		'catalog' => $base . '/shop-2',
		// Toast issues the digital cards; Wix sells the physical ones.
		'gift_digital'  => 'https://www.toasttab.com/saltwater-75-115-75th-st/giftcards',
		'gift_physical' => $base . '/giftcards',
		'categories'    => array(
			array(
				'label' => 'T-Shirts',
				'url'   => $base . '/teeshirts',
				'desc'  => 'Tees in the full range of Saltwater 75 artwork.',
			),
			array(
				'label' => 'Long Sleeve + Sweatshirts',
				'url'   => $base . '/shop-5',
				'desc'  => 'Hoodies and long sleeves for cooler nights on the bay.',
			),
			array(
				'label' => 'Hats',
				'url'   => $base . '/hats',
				'desc'  => 'Caps and visors to keep the sun off.',
			),
			array(
				'label' => 'Accessories',
				'url'   => $base . '/accessories',
				'desc'  => 'Tumblers, koozies, bottle openers and bags.',
			),
			array(
				'label' => 'Gift Cards + AO Game Card',
				'url'   => $base . '/giftcards',
				'desc'  => 'Saltwater 75, Ropewalk and AlleyOops cards.',
			),
		),
	);
}

/**
 * Interface and social icons as inline SVG.
 *
 * The social marks replace the flat PNGs that used to be hot-linked from the
 * Wix CDN. Inline paths inherit currentColor, so an icon recolours along with
 * its chip or button on hover, and stays sharp at any size on any display.
 *
 * Purely decorative — every caller wraps these in an element carrying the label.
 */
function saltwater75_icon( $key ) {
	$icons = array(
		'pin'       => '<svg class="icon" viewBox="0 0 384 512" aria-hidden="true" focusable="false"><path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"/></svg>',
		'phone'     => '<svg class="icon" viewBox="0 0 512 512" aria-hidden="true" focusable="false"><path d="M164.9 24.6c-7.7-18.6-28-28.5-47.4-23.2l-88 24C12.1 30.2 0 46 0 64c0 247.4 200.6 448 448 448 18 0 33.8-12.1 38.6-29.5l24-88c5.3-19.4-4.6-39.7-23.2-47.4l-96-40c-16.3-6.8-35.2-2.1-46.3 11.6L304.7 368C234.3 334.7 177.3 277.7 144 207.3L193.3 167c13.7-11.2 18.4-30 11.6-46.3l-40-96z"/></svg>',
		// Instagram and TikTok are drawn on a 448x512 grid, Facebook on 320x512.
		'instagram' => '<svg class="social__icon" viewBox="0 0 448 512" aria-hidden="true" focusable="false"><path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/></svg>',
		'facebook'  => '<svg class="social__icon" viewBox="0 0 320 512" aria-hidden="true" focusable="false"><path d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"/></svg>',
		'tiktok'    => '<svg class="social__icon" viewBox="0 0 448 512" aria-hidden="true" focusable="false"><path d="M448 209.91a210.06 210.06 0 0 1-122.77-39.25v178.72A162.55 162.55 0 1 1 185 188.31v89.89a74.62 74.62 0 1 0 52.23 71.18V0h88a121.18 121.18 0 0 0 1.86 22.17 122.18 122.18 0 0 0 53.91 80.22 121.43 121.43 0 0 0 67 20.14z"/></svg>',
	);

	return isset( $icons[ $key ] ) ? $icons[ $key ] : '';
}

/**
 * Theme setup.
 */
function saltwater75_setup() {
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'automatic-feed-links' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
	add_theme_support( 'custom-logo', array( 'height' => 92, 'width' => 251, 'flex-height' => true, 'flex-width' => true ) );

	register_nav_menus( array(
		'primary' => __( 'Primary Menu', 'saltwater75' ),
	) );
}
add_action( 'after_setup_theme', 'saltwater75_setup' );

/**
 * Content width.
 */
function saltwater75_content_width() {
	$GLOBALS['content_width'] = 1200;
}
add_action( 'after_setup_theme', 'saltwater75_content_width', 0 );

/**
 * Styles & scripts.
 */
function saltwater75_scripts() {
	// Google Fonts – Playfair Display (headings) + Montserrat (body) to echo the original serif/sans pairing.
	wp_enqueue_style(
		'saltwater75-fonts',
		'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700;800&family=Montserrat:wght@300;400;500;600;700&display=swap',
		array(),
		null
	);

	wp_enqueue_style( 'saltwater75-style', get_stylesheet_uri(), array( 'saltwater75-fonts' ), SALTWATER75_VERSION );

	wp_enqueue_script( 'saltwater75-nav', get_template_directory_uri() . '/js/nav.js', array(), SALTWATER75_VERSION, true );
}
add_action( 'wp_enqueue_scripts', 'saltwater75_scripts' );

/**
 * Fallback menu — shown when no menu is assigned to the "primary" location,
 * so the theme mirrors saltwater75.com immediately after activation.
 */
function saltwater75_default_menu() {
	$items = array(
		array( 'label' => 'Home', 'url' => home_url( '/' ) ),
		array( 'label' => 'Happy Hour', 'url' => 'https://www.saltwater75.com/happy-hour' ),
		array( 'label' => 'Menu', 'url' => 'https://www.saltwater75.com/general-5' ),
		array(
			// Children point at the live Wix shop; see saltwater75_store().
			'label' => 'Store',
			'url'   => '#store',
			'sub'   => saltwater75_store()['categories'],
		),
		array( 'label' => 'Entertainment', 'url' => 'https://www.saltwater75.com/entertainment-calendar' ),
		array(
			'label' => 'Contact',
			'url'   => '#contact',
			'sub'   => array(
				array( 'label' => 'Plan A Party!', 'url' => '#contact' ),
				array( 'label' => 'Frequently Asked', 'url' => '#contact' ),
				array( 'label' => 'Employment', 'url' => 'https://forms.wix.com/r/7024068827293942238' ),
			),
		),
	);

	echo '<ul id="primary-menu" class="menu nav-menu">';
	foreach ( $items as $item ) {
		$has_children = ! empty( $item['sub'] );
		$classes      = 'menu-item' . ( $has_children ? ' menu-item-has-children' : '' );
		printf( '<li class="%s"><a href="%s">%s</a>', esc_attr( $classes ), esc_url( $item['url'] ), esc_html( $item['label'] ) );
		if ( $has_children ) {
			echo '<ul class="sub-menu">';
			foreach ( $item['sub'] as $sub ) {
				// Store and application links leave the site, so open them in a new tab.
				$external = 0 === strpos( $sub['url'], 'http' );
				printf(
					'<li class="menu-item"><a href="%s"%s>%s</a></li>',
					esc_url( $sub['url'] ),
					$external ? ' target="_blank" rel="noopener"' : '',
					esc_html( $sub['label'] )
				);
			}
			echo '</ul>';
		}
		echo '</li>';
	}
	echo '</ul>';
}
