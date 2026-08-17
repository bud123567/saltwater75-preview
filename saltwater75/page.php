<?php
/**
 * Template for static pages (Menu, Contact, etc. built in WordPress).
 *
 * @package Saltwater75
 */

get_header();
?>
<div class="wrap page-content">
	<?php
	while ( have_posts() ) :
		the_post();
		?>
		<article <?php post_class(); ?>>
			<header class="entry-header">
				<?php the_title( '<h1 class="entry-title">', '</h1>' ); ?>
			</header>
			<div class="entry-content">
				<?php
				the_content();
				wp_link_pages();
				?>
			</div>
		</article>
		<?php
	endwhile;
	?>
</div>
<?php
get_footer();
