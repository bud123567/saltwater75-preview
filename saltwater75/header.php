<?php
/**
 * Header + sticky navigation.
 *
 * @package Saltwater75
 */
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="theme-color" content="#0b1f26">
	<?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<a class="skip-link screen-reader-text" href="#content"><?php esc_html_e( 'Skip to content', 'saltwater75' ); ?></a>

<?php $sw_contact = saltwater75_contact(); ?>
<header id="masthead" class="site-header" data-sticky>

	<?php // Slim contact strip; collapses out of the way once the page scrolls. ?>
	<div class="site-header__utility">
		<div class="site-header__utility-inner">
			<a class="utility__item utility__item--address" href="<?php echo esc_url( $sw_contact['map_url'] ); ?>" target="_blank" rel="noopener">
				<?php echo saltwater75_icon( 'pin' ); // phpcs:ignore WordPress.Security.EscapeOutput -- static theme markup. ?>
				<span><?php echo esc_html( $sw_contact['street'] . ', ' . $sw_contact['city'] ); ?></span>
			</a>
			<a class="utility__item" href="tel:<?php echo esc_attr( $sw_contact['phone_tel'] ); ?>">
				<?php echo saltwater75_icon( 'phone' ); // phpcs:ignore WordPress.Security.EscapeOutput -- static theme markup. ?>
				<span><?php echo esc_html( $sw_contact['phone_display'] ); ?></span>
			</a>
		</div>
	</div>

	<div class="site-header__inner">

		<div class="site-branding">
			<a class="site-logo" href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home" aria-label="<?php echo esc_attr( get_bloginfo( 'name' ) ); ?>">
				<img src="<?php echo saltwater75_img( 'logo' ); ?>" alt="<?php echo esc_attr( get_bloginfo( 'name' ) ); ?>" width="251" height="92">
			</a>
		</div>

		<nav id="site-navigation" class="main-navigation" aria-label="<?php esc_attr_e( 'Primary', 'saltwater75' ); ?>">
			<?php
			wp_nav_menu( array(
				'theme_location' => 'primary',
				'menu_id'        => 'primary-menu',
				'menu_class'     => 'menu nav-menu',
				'container'      => false,
				'fallback_cb'    => 'saltwater75_default_menu',
			) );
			?>
		</nav>

		<div class="site-header__actions">
			<?php // Reservations are taken by phone, so the CTA simply dials. ?>
			<a class="btn btn--solid btn--sm reserve" href="tel:<?php echo esc_attr( $sw_contact['phone_tel'] ); ?>"
			   aria-label="<?php echo esc_attr( sprintf( __( 'Make a reservation — call %s', 'saltwater75' ), $sw_contact['phone_display'] ) ); ?>">
				<?php echo saltwater75_icon( 'phone' ); // phpcs:ignore WordPress.Security.EscapeOutput -- static theme markup. ?>
				<span class="reserve__label"><?php esc_html_e( 'Make a Reservation', 'saltwater75' ); ?></span>
			</a>

			<button class="nav-toggle" aria-controls="primary-menu" aria-expanded="false">
				<span class="nav-toggle__bar"></span>
				<span class="nav-toggle__bar"></span>
				<span class="nav-toggle__bar"></span>
				<span class="screen-reader-text"><?php esc_html_e( 'Menu', 'saltwater75' ); ?></span>
			</button>
		</div>

	</div>
</header>

<main id="content" class="site-content">
