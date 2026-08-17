<?php
/**
 * Front page — recreates the saltwater75.com homepage.
 *
 * @package Saltwater75
 */

get_header();

$reviews = array(
	array( 'text' => 'It was fantastic. Great place. Big spaces. Great views. Great drinks and I need to mention that they have the best ice in all their locations. Nobody talks about the ice, but it makes the drinks better!!!', 'name' => 'Doug H.' ),
	array( 'text' => 'The food was great and it was a great experience. Can&rsquo;t wait to go back.', 'name' => 'Jay S.' ),
	array( 'text' => 'Great vibe &ndash; beachy and fun and the food is good!', 'name' => 'Elizabeth B.' ),
	array( 'text' => 'Best Sunset view in OC', 'name' => 'Sharon W.' ),
	array( 'text' => 'We can&rsquo;t wait to go back!', 'name' => 'Veronica L.' ),
);

$gallery = array( 'gallery_1', 'gallery_5', 'gallery_3', 'gallery_4', 'gallery_2', 'gallery_6', 'gallery_7', 'gallery_8' );
?>

<!-- HERO -->
<section class="hero" style="--hero-img:url('<?php echo saltwater75_img( 'hero' ); ?>');">
	<div class="hero__overlay"></div>
	<div class="hero__content">
		<img class="hero__logo" src="<?php echo saltwater75_img( 'logo' ); ?>" alt="<?php echo esc_attr( get_bloginfo( 'name' ) ); ?>">
		<p class="hero__tagline">bayfront dining</p>
		<p class="hero__sub">Fresh seafood, cold drinks &amp; the best sunset view in Ocean City.</p>
		<div class="hero__actions">
			<?php $sw_hero_contact = saltwater75_contact(); ?>
			<a class="btn btn--solid reserve" href="tel:<?php echo esc_attr( $sw_hero_contact['phone_tel'] ); ?>"
			   aria-label="<?php echo esc_attr( sprintf( __( 'Make a reservation — call %s', 'saltwater75' ), $sw_hero_contact['phone_display'] ) ); ?>">
				<?php echo saltwater75_icon( 'phone' ); // phpcs:ignore WordPress.Security.EscapeOutput -- static theme markup. ?>
				<span class="reserve__label"><?php esc_html_e( 'Make a Reservation', 'saltwater75' ); ?></span>
			</a>
			<a class="btn btn--ghost" href="https://www.saltwater75.com/general-5" target="_blank" rel="noopener">View the Menu</a>
			<a class="btn btn--ghost" href="#contact">Find Us</a>
		</div>
	</div>
	<a class="hero__scroll" href="#about" aria-label="Scroll down">&#9662;</a>
</section>

<!-- ABOUT -->
<section id="about" class="section about">
	<div class="wrap about__grid">
		<div class="about__text">
			<span class="eyebrow">About Us</span>
			<h2>A new bayfront restaurant on iconic 75th St.</h2>
			<p>Saltwater75 offers a full menu of appetizers, sandwiches and entrees, including seafood of all sorts! All of our seating overlooks the bay to enjoy beautiful sunsets or views of a wide range of nature in the area.</p>
			<p>We are the home to the famous canoe races of Ocean City &mdash; a new beach venue with different levels, including a rooftop bar!</p>
		</div>
		<div class="about__media">
			<img src="<?php echo saltwater75_img( 'about' ); ?>" alt="Saltwater 75 bayfront view" loading="lazy">
		</div>
	</div>
</section>

<!-- HOURS + CONTACT -->
<section id="contact" class="section info">
	<div class="wrap info__grid">
		<div class="info__card">
			<span class="eyebrow">Visit</span>
			<h3>Address</h3>
			<p>115 75th Street<br>Ocean City, MD 21842</p>
			<p><a class="info__phone" href="tel:14105247575">410-524-7575</a></p>
			<a class="btn btn--solid btn--sm" href="https://www.google.com/maps/search/?api=1&amp;query=115+75th+Street+Ocean+City+MD+21842" target="_blank" rel="noopener">Get Directions</a>
		</div>
		<div class="info__card">
			<span class="eyebrow">Open Daily</span>
			<h3>Hours</h3>
			<ul class="hours">
				<li><span>Monday</span><span>11:00am &ndash; 12:00am</span></li>
				<li><span>Tuesday</span><span>11:00am &ndash; 12:00am</span></li>
				<li><span>Wednesday</span><span>11:00am &ndash; 12:00am</span></li>
				<li><span>Thursday</span><span>11:00am &ndash; 12:00am</span></li>
				<li><span>Friday</span><span>11:00am &ndash; 12:00am</span></li>
				<li><span>Saturday</span><span>11:00am &ndash; 12:00am</span></li>
				<li><span>Sunday</span><span>11:00am &ndash; 12:00am</span></li>
			</ul>
		</div>
	</div>
</section>

<!-- GALLERY -->
<section id="gallery" class="section gallery">
	<div class="wrap">
		<div class="section__head">
			<span class="eyebrow">The Scene</span>
			<h2>Bay views, good times</h2>
		</div>
		<div class="gallery__grid">
			<?php foreach ( $gallery as $i => $key ) : ?>
				<figure class="gallery__item">
					<img src="<?php echo saltwater75_img( $key ); ?>" alt="Saltwater 75 photo <?php echo esc_attr( $i + 1 ); ?>" loading="lazy">
				</figure>
			<?php endforeach; ?>
		</div>
	</div>
</section>

<!-- STORE -->
<?php $sw_store = saltwater75_store(); ?>
<section id="store" class="section store">
	<div class="wrap">
		<div class="section__head">
			<span class="eyebrow">Shop</span>
			<h2>Take a little Saltwater home</h2>
			<p class="section__lede">Tees, hoodies, hats and bar gear &mdash; plus gift cards for Saltwater 75, Ropewalk and AlleyOops.</p>
		</div>

		<div class="store__grid">
			<?php foreach ( $sw_store['categories'] as $cat ) : ?>
				<a class="store__card" href="<?php echo esc_url( $cat['url'] ); ?>" target="_blank" rel="noopener">
					<h3 class="store__card-title"><?php echo esc_html( $cat['label'] ); ?></h3>
					<p class="store__card-desc"><?php echo esc_html( $cat['desc'] ); ?></p>
					<span class="store__card-go" aria-hidden="true">Shop &rarr;</span>
				</a>
			<?php endforeach; ?>
		</div>

		<?php // Digital cards are issued by Toast (the POS) so they redeem at the register. ?>
		<div class="store__gift">
			<div class="store__gift-text">
				<h3>Gift cards</h3>
				<p>Send a digital card instantly, or pick up a physical one from the shop.</p>
			</div>
			<div class="store__gift-actions">
				<a class="btn btn--solid btn--sm" href="<?php echo esc_url( $sw_store['gift_digital'] ); ?>" target="_blank" rel="noopener">Send a Digital Card</a>
				<a class="btn btn--ghost btn--sm" href="<?php echo esc_url( $sw_store['gift_physical'] ); ?>" target="_blank" rel="noopener">Physical Cards</a>
			</div>
		</div>
	</div>
</section>

<!-- TESTIMONIALS -->
<section id="reviews" class="section reviews">
	<div class="wrap">
		<div class="section__head">
			<span class="eyebrow">Reviews</span>
			<h2>See What Everyone is Saying!</h2>
		</div>
		<div class="reviews__grid">
			<?php foreach ( $reviews as $review ) : ?>
				<figure class="review">
					<div class="review__stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
					<blockquote><?php echo wp_kses_post( $review['text'] ); ?></blockquote>
					<figcaption>&mdash; <?php echo esc_html( $review['name'] ); ?></figcaption>
				</figure>
			<?php endforeach; ?>
		</div>
	</div>
</section>

<!-- MAILING LIST -->
<section id="subscribe" class="section subscribe">
	<div class="wrap subscribe__inner">
		<h2>Subscribe to get exclusive updates</h2>
		<form class="subscribe__form" action="#" method="post" novalidate>
			<label class="screen-reader-text" for="sw-email">Email</label>
			<input id="sw-email" type="email" name="email" placeholder="Email" required>
			<button type="submit" class="btn btn--solid">Join Our Mailing List</button>
		</form>
		<p class="subscribe__note" hidden>Thanks for subscribing!</p>
	</div>
</section>

<?php
get_footer();
