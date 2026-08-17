<?php
/**
 * Fallback template for any view without a more specific template.
 *
 * @package Saltwater75
 */

get_header();
?>
<div class="wrap page-content">
	<?php if ( have_posts() ) : ?>
		<?php while ( have_posts() ) : the_post(); ?>
			<article <?php post_class(); ?>>
				<header class="entry-header">
					<?php the_title( '<h1 class="entry-title">', '</h1>' ); ?>
				</header>
				<div class="entry-content">
					<?php the_content(); ?>
				</div>
			</article>
		<?php endwhile; ?>

		<?php the_posts_navigation(); ?>
	<?php else : ?>
		<h1 class="entry-title"><?php esc_html_e( 'Nothing here yet', 'saltwater75' ); ?></h1>
		<p><?php esc_html_e( 'No content was found.', 'saltwater75' ); ?></p>
	<?php endif; ?>
</div>
<?php
get_footer();
