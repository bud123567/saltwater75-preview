<?php
/**
 * Footer.
 *
 * @package Saltwater75
 */
?>
</main><!-- #content -->

<footer id="colophon" class="site-footer">
	<div class="wrap site-footer__inner">

		<div class="site-footer__brand">
			<img class="site-footer__logo" src="<?php echo saltwater75_img( 'logo' ); ?>" alt="<?php echo esc_attr( get_bloginfo( 'name' ) ); ?>">
			<p>115 75th Street, Ocean City, MD 21842<br>
			<a href="tel:14105247575">410-524-7575</a></p>
		</div>

		<nav class="social" aria-label="<?php esc_attr_e( 'Social', 'saltwater75' ); ?>">
			<a class="social__link" href="https://www.instagram.com/saltwater75oc" target="_blank" rel="noopener" aria-label="Instagram">
				<?php echo saltwater75_icon( 'instagram' ); // phpcs:ignore WordPress.Security.EscapeOutput -- static theme markup. ?>
			</a>
			<a class="social__link" href="https://www.facebook.com/sw75oc" target="_blank" rel="noopener" aria-label="Facebook">
				<?php echo saltwater75_icon( 'facebook' ); // phpcs:ignore WordPress.Security.EscapeOutput -- static theme markup. ?>
			</a>
			<a class="social__link" href="https://www.tiktok.com/@saltwater75s" target="_blank" rel="noopener" aria-label="TikTok">
				<?php echo saltwater75_icon( 'tiktok' ); // phpcs:ignore WordPress.Security.EscapeOutput -- static theme markup. ?>
			</a>
		</nav>

	</div>
	<div class="site-footer__bar">
		<p>&copy; <?php echo esc_html( date( 'Y' ) ); ?> by Saltwater 75</p>
	</div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
