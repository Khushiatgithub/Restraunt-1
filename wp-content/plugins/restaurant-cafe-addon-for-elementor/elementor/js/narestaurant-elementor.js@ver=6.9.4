/*
Template Name: Restaurant & Cafe Addon for Elementor
Author: NicheAddon
Version: 1.0.0
Email: support@nicheaddon.com
*/

(function($){
'use strict';

/*----- ELEMENTOR LOAD SWIPER CALL ---*/
function SwiperSliderInit(slider_el){
  //Atrakt Swiper Slider Script
  let animEndEv 			= 'webkitAnimationEnd animationend';
  let swipermw 				= (slider_el.hasClass('swiper-mousewheel')) ? true : false;
  let swiperkb 				= (slider_el.hasClass('swiper-keyboard')) ? true : false;
  let swipercentered 		= (slider_el.hasClass('swiper-center')) ? true : false;
  let swiperautoplay 		= slider_el.data('autoplay');
  let swiperinterval 		= slider_el.data('interval');
  let swiperloop 			= slider_el.data('loop');
  let swipermousedrag 		= slider_el.data('mousedrag');
  let swipereffect 			= slider_el.data('effect');
  let swiperclikable 		= slider_el.data('clickpage');
  let swiperspeed 			= slider_el.data('speed');
  let swiperinteraction 	= slider_el.data('interaction');

  let swipersitems 			= ( slider_el.data('items') ) ? slider_el.data('items') : 1;
  let swiperstabitems 		= ( slider_el.data('tab-items') ) ? slider_el.data('tab-items') : 1;
  let swipersmobileitems 	= ( slider_el.data('mobile-items') ) ? slider_el.data('mobile-items') : 1;

  //Atrakt Swiper Slides Script
  let autoplay = swiperinterval;
	
	// Init elementor swiper
	let Swiper = elementorFrontend.utils.swiper;
	initSwiper();

	async function initSwiper() {
	  let slidervar = await new Swiper( slider_el, {
		autoplayDisableOnInteraction: swiperinteraction,
		slidesPerView: swipersitems,
		effect: swipereffect,
		speed: swiperspeed,
		loop: swiperloop,
		paginationClickable: swiperclikable,
		watchSlidesProgress: true,
		autoplay: swiperautoplay,
		simulateTouch: swipermousedrag,
		breakpoints: {
			// when window width is >= 320px
			320: {
			  slidesPerView: swipersmobileitems,
			},
			// when window width is >= 480px
			480: {
			  slidesPerView: swipersmobileitems,
			},
			// when window width is >= 640px
			640: {
			  slidesPerView: swiperstabitems,
			},
			991: {
			  slidesPerView: swipersitems,
			}
		},      
		pagination: {
			el: '.swiper-pagination',
			clickable: true,
		},
		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},
		mousewheelControl: swipermw,
		keyboardControl: swiperkb,
	});
		slidervar.on('slideChange', function (s) {
			let currentSlide = $(slidervar.slides[slidervar.activeIndex]);
			let elems = currentSlide.find('.animated')
			elems.each(function() {
				let $this = $(this);
				let animationType = $this.data('animation');
				$this.addClass(animationType, 100).on(animEndEv, function() {
				  $this.removeClass(animationType);
				});
			});
		});
	}		
}
/*----- ELEMENTOR LOAD FUNTION CALL ---*/

$( window ).on( 'elementor/frontend/init', function() {
	//Owl Carousel Slider Script
	var owl_carousel = function(){
		$('.owl-carousel').each( function() {
	    var $carousel = $(this);
	    var $items = ($carousel.data('items') !== undefined) ? $carousel.data('items') : 1;
	    var $items_tablet = ($carousel.data('items-tablet') !== undefined) ? $carousel.data('items-tablet') : 1;
	    var $items_mobile_landscape = ($carousel.data('items-mobile-landscape') !== undefined) ? $carousel.data('items-mobile-landscape') : 1;
	    var $items_mobile_portrait = ($carousel.data('items-mobile-portrait') !== undefined) ? $carousel.data('items-mobile-portrait') : 1;
	    $carousel.owlCarousel ({
	      loop : ($carousel.data('loop') !== undefined) ? $carousel.data('loop') : true,
	      items : $carousel.data('items'),
	      margin : ($carousel.data('margin') !== undefined) ? $carousel.data('margin') : 0,
	      dots : ($carousel.data('dots') !== undefined) ? $carousel.data('dots') : true,
	      nav : ($carousel.data('nav') !== undefined) ? $carousel.data('nav') : false,
	      navText : ["<div class='slider-no-current'><span class='current-no'></span><span class='total-no'></span></div><span class='current-monials'></span>", "<div class='slider-no-next'></div><span class='next-monials'></span>"],
	      autoplay : ($carousel.data('autoplay') !== undefined) ? $carousel.data('autoplay') : false,
	      autoplayTimeout : ($carousel.data('autoplay-timeout') !== undefined) ? $carousel.data('autoplay-timeout') : 5000,
	      animateIn : ($carousel.data('animatein') !== undefined) ? $carousel.data('animatein') : false,
	      animateOut : ($carousel.data('animateout') !== undefined) ? $carousel.data('animateout') : false,
	      mouseDrag : ($carousel.data('mouse-drag') !== undefined) ? $carousel.data('mouse-drag') : true,
	      autoWidth : ($carousel.data('auto-width') !== undefined) ? $carousel.data('auto-width') : false,
	      autoHeight : ($carousel.data('auto-height') !== undefined) ? $carousel.data('auto-height') : false,
	      center : ($carousel.data('center') !== undefined) ? $carousel.data('center') : false,
	      responsiveClass: true,
	      dotsEachNumber: true,
	      smartSpeed: 600,
	      autoplayHoverPause: true,
	      responsive : {
	        0 : {
	          items : $items_mobile_portrait,
	        },
	        480 : {
	          items : $items_mobile_landscape,
	        },
	        768 : {
	          items : $items_tablet,
	        },
	        992 : {
	          items : $items,
	        }
	      }
	    });
	    var totLength = $('.owl-dot', $carousel).length;
	    $('.total-no', $carousel).html(totLength);
	    $('.current-no', $carousel).html(totLength);
	    $carousel.owlCarousel();
	    $('.current-no', $carousel).html(1);
	    $carousel.on('changed.owl.carousel', function(event) {
	      var total_items = event.page.count;
	      var currentNum = event.page.index + 1;
	      $('.total-no', $carousel ).html(total_items);
	      $('.current-no', $carousel).html(currentNum);
	    });
	  });
	}; // end

	//Restaurant & Cafe Addon for Elementor Preloader Script
  $('.narep-preloader').fadeOut(500);

	var item_hover_class = function( selector ){
		$(selector).on({
		  mouseenter : function() {
			$(this).addClass('narep-hover');
		  },
		  mouseleave : function() {
			$(this).removeClass('narep-hover');
		  }
		});
	};

	var item_prev_class = function( selector ){
		$(selector).on({
		  mouseenter : function() {
			$(this).prevAll(selector).addClass('process-done');
		  },
		  mouseleave : function() {
			$(this).prevAll(selector).removeClass('process-done');
		  }
		});
	};

	//Restaurant & Cafe Addon for Elementor Services
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_services.default', function($scope, $){
		item_hover_class('.narep-service-item');
	} );
	//Restaurant & Cafe Addon for Elementor Blog
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_blog.default', function($scope, $){
		item_hover_class('.narep-news-item');
    $('.narep-item').matchHeight ({
      property: 'height'
    });
    
    //Flickity Carousel Slider Script
	  $('.flick-carousel').each( function() {
	    var $Flick = $(this);
	    $Flick.flickity  ({
	      draggable : ($Flick.data('draggable') !== undefined) ? $Flick.data('draggable') : false,
	      freeScroll : ($Flick.data('freescroll') !== undefined) ? $Flick.data('freescroll') : false,
	      freeScrollFriction : ($Flick.data('freescrollfriction') !== undefined) ? $Flick.data('freescrollfriction') : 0.075,
	      wrapAround : ($Flick.data('wraparound') !== undefined) ? $Flick.data('wraparound') : true,
	      groupCells : ($Flick.data('groupcells') !== undefined) ? $Flick.data('groupcells') : '',
	      autoPlay : ($Flick.data('autoplay') !== undefined) ? $Flick.data('autoplay') : '',
	      pauseAutoPlayOnHover : ($Flick.data('pauseautoplayonhover') !== undefined) ? $Flick.data('pauseautoplayonhover') : false,
	      adaptiveHeight : ($Flick.data('adaptiveheight') !== undefined) ? $Flick.data('adaptiveheight') : false,
	      dragThreshold : ($Flick.data('dragthreshold') !== undefined) ? $Flick.data('dragthreshold') : '',
	      selectedAttraction : ($Flick.data('selectedattraction') !== undefined) ? $Flick.data('selectedattraction') : 0.025,
	      friction : ($Flick.data('friction') !== undefined) ? $Flick.data('friction') : 0.28,
	      initialIndex : ($Flick.data('initialindex') !== undefined) ? $Flick.data('initialindex') : '',
	      accessibility : ($Flick.data('accessibility') !== undefined) ? $Flick.data('accessibility') : true,
	      setGallerySize : ($Flick.data('setgallerysize') !== undefined) ? $Flick.data('setgallerysize') : true,
	      resize : ($Flick.data('resize') !== undefined) ? $Flick.data('resize') : true,
	      cellAlign : ($Flick.data('cellalign') !== undefined) ? $Flick.data('cellalign') : 'center',
	      contain : ($Flick.data('contain') !== undefined) ? $Flick.data('contain') : false,
	      rightToLeft : ($Flick.data('righttoleft') !== undefined) ? $Flick.data('righttoleft') : false,
	      prevNextButtons : ($Flick.data('prevnextbuttons') !== undefined) ? $Flick.data('prevnextbuttons') : false,
	      pageDots : ($Flick.data('pagedots') !== undefined) ? $Flick.data('pagedots') : false,
	    });
	  });

	} );
	//Restaurant & Cafe Addon for Elementor Gallery
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_gallery.default', function($scope, $){
		item_hover_class('.narep-gallery-item');
		$('.masonry-wrap').each(function(i, gridContainer) {
      var $gridContainer = $(gridContainer);
      var $grid = $gridContainer.find('.narep-masonry').imagesLoaded(function() {
        $grid.isotope ({
          itemSelector: '.masonry-item',
          // layoutMode: 'packery',
          percentPosition: true,
          isFitWidth: true,
        })
      });
      $grid.packery({
	      itemSelector: '.masonry-item'
	    });
      $gridContainer.find('.masonry-filters').on('click', 'li a', function() {
        var filterValue = $(this).attr('data-filter');
        $grid.isotope ({
          filter: filterValue,
        });
      });
    });
    $('.masonry-filters').each( function( i, buttonGroup ) {
      var $buttonGroup = $(buttonGroup);
      $buttonGroup.on( 'click', 'li a', function() {
        $buttonGroup.find('.active').removeClass('active');
        $(this).addClass('active');
      });
    });
	} );
	//Restaurant & Cafe Addon for Elementor Contact
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_contact.default', function($scope, $){
		item_hover_class('.narep-contact-item');
	} );
	//Restaurant & Cafe Addon for Elementor Process
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_process.default', function($scope, $){
	  item_prev_class('.narep-process-item');
	} );
	//Restaurant & Cafe Addon for Elementor Team
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_team.default', function($scope, $){
	  item_hover_class('.narep-mate-item');
	} );
	//Restaurant & Cafe Addon for Elementor Video Popup
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_video.default', function($scope, $){
	  item_hover_class('.narep-video-wrap');
	} );
	//Restaurant & Cafe Addon for Elementor History
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_history.default', function($scope, $){
	  // item_hover_class('.narep-history-item');
		$('.narep-item').matchHeight ({
	    property: 'height'
	  });
	} );
	//Restaurant & Cafe Addon for Elementor Slider
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_slider.default', function($scope, $){
		//Restaurant Swiper Slider Script
		let slider_el = $scope.find(".swiper-slides");
		SwiperSliderInit(slider_el);		
	} );

	//Chart
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_chart.default', function($scope, $){
		//Chart Script
		let $canvas = $scope.find(".narep-chart canvas");
        let chartData = $canvas.data('chart');

        if (chartData) {
            // Global configs
            Chart.defaults.global.responsive = true;
            Chart.defaults.global.maintainAspectRatio = false;
            Chart.defaults.global.tooltips.backgroundColor = 'rgba(35,35,35,0.9)';
            Chart.defaults.global.tooltips.bodyFontSize = 13;
            Chart.defaults.global.tooltips.bodyFontStyle = 'bold';
            Chart.defaults.global.tooltips.yPadding = 13;
            Chart.defaults.global.tooltips.xPadding = 10;
            Chart.defaults.doughnut.cutoutPercentage = 60;

            // Create the chart
            new Chart($canvas, {
                type: chartData.type,
                data: {
                    labels: chartData.labels,
                    datasets: chartData.datasets
                },
                options: chartData.options
            });
        }	
	} );

	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_typewriter.default', function($scope, $) {
		let target_el   = $scope.find(".narep-typewriter");
		let $id         = target_el.attr('data-id');
		let $typed_id   = target_el.attr('data-type-id');
		let $typeSpeed  = target_el.attr('data-type-speed');
		let $backSpeed  = target_el.attr('data-back-speed');
		let $backDelay  = target_el.attr('data-back-delay');
		let $startDelay = target_el.attr('data-start-delay');
		let $cursorChar = target_el.attr('data-cursor-char');

		let target_var  = 'typed_' + $typed_id + '_' + $id;

		target_var = new Typed('.' + target_var, {
			typeSpeed: parseInt($typeSpeed),
			backSpeed: parseInt($backSpeed),
			backDelay: parseInt($backDelay),
			startDelay: parseInt($startDelay),
			cursorChar: $cursorChar,
			loop: true,
			stringsElement: '.'+ target_var +'_strings',
		});   
	} );

	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_basic_image_compare.default', function($scope, $) {
		let target_el   = $scope.find(".narep-compare");
        let beforeUrl = target_el.data('before-url');
        let beforeTitle = target_el.data('before-title');
        let afterUrl = target_el.data('after-url');
        let afterTitle = target_el.data('after-title');
        let showLabels = target_el.data('show-labels');
        let startingPosition = target_el.data('starting-position');
        let compareStyle = target_el.data('compare-style');

        new juxtapose.JXSlider(target_el[0], [
            {
                src: beforeUrl,
                label: beforeTitle
            },
            {
                src: afterUrl,
                label: afterTitle
            }
        ], {
            animate: true,
            showLabels: showLabels,
            showCredits: false,
            startingPosition: startingPosition + "%",
            makeResponsive: true,
            mode: compareStyle
        });
	} );	

	//Restaurant & Cafe Addon for Elementor Tab
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_tab.default', function($scope, $){
		$('.narep-tab-links a').on('click', function(e) {
	    var currentAttrValue = $(this).attr('href');

	    // Show/Hide Tabs
	    $('.narep-tab-content ' + currentAttrValue).fadeIn(0).siblings().hide().stop(true, true);

	    // Change/remove current tab to active
	    $(this).parent('li').addClass('active').siblings().removeClass('active');

	    e.preventDefault();
	  });

	  $('.narep-item').matchHeight ({
	    property: 'height'
	  });

	  if ($('div').hasClass('tab-horizontal')) {
	    $('.tab-horizontal').each(function (index) {
	      var $NAH_el, NAH_leftPos, NAH_newWidth,
	      $NAH_mainNav = $(this).find(".narep-tab-links");
	      var $NAH_TabLine = $NAH_mainNav.find(".narep-tab-line");
	      
	      $NAH_TabLine
	        .width($NAH_mainNav.find(".active").width())
	        .css("left", $NAH_mainNav.find(".active a").position().left)
	        .data("origLeft", $NAH_TabLine.position().left)
	        .data("origWidth", $NAH_TabLine.width());

	      $NAH_mainNav.find("li a").on({
	        mouseenter : function() {
	          $NAH_el = $(this);
	          NAH_leftPos = $NAH_el.position().left;
	          NAH_newWidth = $NAH_el.parent().width();
	          $NAH_TabLine.stop().animate({
	            left: NAH_leftPos,
	            width: NAH_newWidth
	          });
	        },
	        mouseleave : function() {
	          $NAH_el = $NAH_mainNav.find('.active');
	          NAH_leftPos = $NAH_el.position().left;
	          NAH_newWidth = $NAH_el.width();
	          $NAH_TabLine.stop().animate({
	            left: NAH_leftPos,
	            width: NAH_newWidth
	          }); 
	        }
	      });
	    });
	  }

	  if ($('div').hasClass('tab-vertical')) {
	    $('.tab-vertical').each(function (index) {
	      var $NAV_el, NAV_topPos, NAV_newHeight,
	      $NAV_mainNav = $(this).find(".narep-tab-links");
	      var $NAV_TabLine = $NAV_mainNav.find(".narep-tab-line");
	      
	      $NAV_TabLine
	        .height($NAV_mainNav.find(".active").height())
	        .css("top", $NAV_mainNav.find(".active a").position().top)
	        .data("origLeft", $NAV_TabLine.position().top)
	        .data("origHeight", $NAV_TabLine.height());

	      $NAV_mainNav.find("li a").on({
	        mouseenter : function() {
	          $NAV_el = $(this);
	          NAV_topPos = $NAV_el.position().top;
	          NAV_newHeight = $NAV_el.parent().height();
	          $NAV_TabLine.stop().animate({
	            top: NAV_topPos,
	            height: NAV_newHeight
	          });
	        },
	        mouseleave : function() {
	          $NAV_el = $NAV_mainNav.find('.active');
	          NAV_topPos = $NAV_el.position().top;
	          NAV_newHeight = $NAV_el.height();
	          $NAV_TabLine.stop().animate({
	            top: NAV_topPos,
	            height: NAV_newHeight
	          }); 
	        }
	      });
	    });
	  }

	} );

	//Restaurant & Cafe Addon for Elementor Valuable Box
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_valuable.default', function($scope, $){
	  item_hover_class('.narep-valuable-item');
	  $('.narep-item').matchHeight ({
	    property: 'height'
	  });
	  // Slick Vertical Slider
	  jQuery('.slick-vertical-slider').not('.slick-initialized').slick ({
	    dots: false,
	    vertical: true,
	    slidesToShow: 3,
	    slidesToScroll: 1,
	    verticalSwiping: true,
	  });
	} );

	//Restaurant & Cafe Addon for Elementor Stats
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_stats.default', function($scope, $){
	  item_hover_class('.narep-stats-item');
	} );

	//Restaurant & Cafe Addon for Elementor Restaurants
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_restaurants.default', function($scope, $){
	  item_hover_class('.narep-restaurant-item');
	} );

	//Restaurant & Cafe Addon for Elementor Food Item
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_food_item.default', function($scope, $){
	  item_hover_class('.narep-food-item');
	} );

	//Restaurant & Cafe Addon for Elementor Tools
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_tools.default', function($scope, $){
	  item_hover_class('.narep-tool-item');
	  item_hover_class('.narep-care-item');
	} );

	//Restaurant & Cafe Addon for Elementor Benefits
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_benefits.default', function($scope, $){
	  item_hover_class('.narep-benefit-item');
	  $('.narep-item').matchHeight ({
	    property: 'height'
	  });
	  // Naeep Benefit Tab
	  $('.narep-benefit-tab a').on('click', function(e) {
	    var currentAttrValue = $(this).attr('href');

	    // Show/Hide Tabs
	    $('.narep-tab-benefit ' + currentAttrValue).fadeIn(0).siblings().hide().stop(true, true);
	    $('.narep-tab-benefit ' + currentAttrValue).addClass('active').siblings().removeClass('active');

	    // Change/remove current tab to active
	    $(this).addClass('active').siblings().removeClass('active');

	    e.preventDefault();
	  });
	} );

	//Restaurant & Cafe Addon for Elementor Food Tab
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_foodtab.default', function($scope, $){
	  $('.narep-food-tab a').on('click', function(e) {
	    var currentAttrValue = $(this).attr('href');

	    // Show/Hide Tabs
	    $('.narep-tab-food ' + currentAttrValue).fadeIn(0).siblings().hide().stop(true, true);
	    $('.narep-tab-food ' + currentAttrValue).addClass('active').siblings().removeClass('active');

	    // Change/remove current tab to active
	    $(this).addClass('active').siblings().removeClass('active');

	    e.preventDefault();
	  });
	} );

	//Restaurant & Cafe Addon for Elementor Addon Menu
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_addon_menu.default', function($scope, $){
	  item_hover_class('.narep-addon-menu-wrap');
	  $('.narep-addon-menu-wrap').each(function (index) {
	    $(this).find('.narep-addon-item :checkbox').on("change", function() {
	      $(this).parents(".narep-addon-menu-wrap").find(".addon-total").text(function() {
	        var baseTotal = $(this).parents(".narep-addon-menu-wrap").find(".addon-total").attr("data-total");
	        var sum = 0;
	        sum = Number(baseTotal);
	        $(this).parents(".narep-addon-menu-wrap").find(".narep-addon-item :checkbox:checked").each(function() {
	          sum += ~~$(this).val();
	        });
	        return '$'+sum;
	      });
	    });
	  });
	} );

	//Restaurant & Cafe Addon for Elementor Chefs Recipe
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_chefs_recipe.default', function($scope, $){
	  item_hover_class('.narep-chefs-food');
		//Restaurant Swiper Slider Script
    $('.swiper-slides').each(function (index) {
      //Restaurant Swiper Slider Script
      var animEndEv = 'webkitAnimationEnd animationend';
      var swipermw = $('.swiper.swiper-mousewheel').length ? true : false;
      var swiperkb = $('.swiper.swiper-keyboard').length ? true : false;
      var swipercentered = $('.swiper.swiper-center').length ? true : false;
      var swiperautoplay = $('.swiper').data('autoplay');
      var swiperloop = $('.swiper').data('loop');
      var swipermousedrag = $('.swiper').data('mousedrag');
      var swipereffect = $('.swiper').data('effect');
      var swiperclikable = $('.swiper').data('clickpage');
      var swiperspeed = $('.swiper').data('speed');
      var swiperitem = $('.swiper').data('item');
      var swiperspace = $('.swiper').data('space');

      //Restaurant Swiper Slides Script
      var swiper = new Swiper($(this), {
        slidesPerView: swiperitem,
        spaceBetween: swiperspace,
        autoplay: swiperautoplay,
        effect: swipereffect,
        speed: swiperspeed,
        loop: swiperloop,
        paginationClickable: swiperclikable,
        watchSlidesProgress: true,
        simulateTouch: swipermousedrag,
        pagination: {
          el: '.swiper-pagination',
          clickable: true,
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
        scrollbar: {
          el: '.swiper-scrollbar',
          hide: false,
        },
        mousewheelControl: swipermw,
        keyboardControl: swiperkb,
      });
      swiper.on('slideChange', function (s) {
        var currentSlide = $(swiper.slides[swiper.activeIndex]);
          var elems = currentSlide.find('.animated')
          elems.each(function() {
            var $this = $(this);
            var animationType = $this.data('animation');
            $this.addClass(animationType, 100).on(animEndEv, function() {
              $this.removeClass(animationType);
            });
          });
      });
    });
	} );

	//Restaurant & Cafe Addon for Elementor Open Table
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_open_table.default', function($scope, $){
		$('.narep-item').matchHeight ({
	    property: 'height'
	  });
	  
		//Flickity Time Carousel Slider Script
	  $('.flick-time-carousel').each( function() {
	    var $Flick = $(this);
	    $Flick.flickity  ({
	      draggable : ($Flick.data('draggable') !== undefined) ? $Flick.data('draggable') : false,
	      freeScroll : ($Flick.data('freescroll') !== undefined) ? $Flick.data('freescroll') : false,
	      freeScrollFriction : ($Flick.data('freescrollfriction') !== undefined) ? $Flick.data('freescrollfriction') : 0.075,
	      wrapAround : ($Flick.data('wraparound') !== undefined) ? $Flick.data('wraparound') : true,
	      groupCells : ($Flick.data('groupcells') !== undefined) ? $Flick.data('groupcells') : '',
	      autoPlay : ($Flick.data('autoplay') !== undefined) ? $Flick.data('autoplay') : '',
	      pauseAutoPlayOnHover : ($Flick.data('pauseautoplayonhover') !== undefined) ? $Flick.data('pauseautoplayonhover') : false,
	      adaptiveHeight : ($Flick.data('adaptiveheight') !== undefined) ? $Flick.data('adaptiveheight') : false,
	      dragThreshold : ($Flick.data('dragthreshold') !== undefined) ? $Flick.data('dragthreshold') : '',
	      selectedAttraction : ($Flick.data('selectedattraction') !== undefined) ? $Flick.data('selectedattraction') : 0.025,
	      friction : ($Flick.data('friction') !== undefined) ? $Flick.data('friction') : 0.28,
	      initialIndex : ($Flick.data('initialindex') !== undefined) ? $Flick.data('initialindex') : '',
	      accessibility : ($Flick.data('accessibility') !== undefined) ? $Flick.data('accessibility') : true,
	      setGallerySize : ($Flick.data('setgallerysize') !== undefined) ? $Flick.data('setgallerysize') : true,
	      resize : ($Flick.data('resize') !== undefined) ? $Flick.data('resize') : true,
	      cellAlign : ($Flick.data('cellalign') !== undefined) ? $Flick.data('cellalign') : 'center',
	      contain : ($Flick.data('contain') !== undefined) ? $Flick.data('contain') : false,
	      rightToLeft : ($Flick.data('righttoleft') !== undefined) ? $Flick.data('righttoleft') : false,
	      prevNextButtons : ($Flick.data('prevnextbuttons') !== undefined) ? $Flick.data('prevnextbuttons') : false,
	      pageDots : ($Flick.data('pagedots') !== undefined) ? $Flick.data('pagedots') : false,
	    });
	  });

		//Flickity Date Carousel Slider Script
	  $('.flick-date-carousel').each( function() {
	    var $Flick = $(this);
	    $Flick.flickity  ({
	      draggable : ($Flick.data('draggable') !== undefined) ? $Flick.data('draggable') : false,
	      freeScroll : ($Flick.data('freescroll') !== undefined) ? $Flick.data('freescroll') : false,
	      freeScrollFriction : ($Flick.data('freescrollfriction') !== undefined) ? $Flick.data('freescrollfriction') : 0.075,
	      wrapAround : ($Flick.data('wraparound') !== undefined) ? $Flick.data('wraparound') : true,
	      groupCells : ($Flick.data('groupcells') !== undefined) ? $Flick.data('groupcells') : '',
	      autoPlay : ($Flick.data('autoplay') !== undefined) ? $Flick.data('autoplay') : '',
	      pauseAutoPlayOnHover : ($Flick.data('pauseautoplayonhover') !== undefined) ? $Flick.data('pauseautoplayonhover') : false,
	      adaptiveHeight : ($Flick.data('adaptiveheight') !== undefined) ? $Flick.data('adaptiveheight') : false,
	      dragThreshold : ($Flick.data('dragthreshold') !== undefined) ? $Flick.data('dragthreshold') : '',
	      selectedAttraction : ($Flick.data('selectedattraction') !== undefined) ? $Flick.data('selectedattraction') : 0.025,
	      friction : ($Flick.data('friction') !== undefined) ? $Flick.data('friction') : 0.28,
	      initialIndex : ($Flick.data('initialindex') !== undefined) ? $Flick.data('initialindex') : '',
	      accessibility : ($Flick.data('accessibility') !== undefined) ? $Flick.data('accessibility') : true,
	      setGallerySize : ($Flick.data('setgallerysize') !== undefined) ? $Flick.data('setgallerysize') : true,
	      resize : ($Flick.data('resize') !== undefined) ? $Flick.data('resize') : true,
	      cellAlign : ($Flick.data('cellalign') !== undefined) ? $Flick.data('cellalign') : 'center',
	      contain : ($Flick.data('contain') !== undefined) ? $Flick.data('contain') : false,
	      rightToLeft : ($Flick.data('righttoleft') !== undefined) ? $Flick.data('righttoleft') : false,
	      prevNextButtons : ($Flick.data('prevnextbuttons') !== undefined) ? $Flick.data('prevnextbuttons') : false,
	      pageDots : ($Flick.data('pagedots') !== undefined) ? $Flick.data('pagedots') : false,
	    });
	  });
	  // Date picker
	  $('.narep-datepicker').datepicker({
	    format: 'mm/dd/yyyy',
	    startDate: '-3d',
	    autoclose: true,
	  });
	  // Time picker
	  $('.narep-timepicker').timepicker();

	  // Open Table Submit
	  $('#narep-tbDate, #narep-tbTime').on('click mouseenter', function() {
	    $('#narep-tbDateTime').val($('#narep-tbDate').val() + ' ' + $('#narep-tbTime').val());
	  });
	  $('.style-one button.narep-btn').on('click mouseenter', function() {
	    $('#narep-tbDateTime').val($('#narep-tbDate').val() + ' ' + $('#narep-tbTime').val());
	  });
	  $('.narep-dateradio, .narep-bookradio').on('click mouseleave', function() {
	    $('#narep-tbDateTime').val($('.narep-dateradio:checked').val() + ' ' + $('.narep-bookradio:checked').val());
	  });
	  $('.style-two button.narep-btn').on('click mouseenter', function() {
	    $('#narep-tbDateTime').val($('.narep-dateradio:checked').val() + ' ' + $('.narep-bookradio:checked').val());
	  });
	} );

	//Restaurant & Cafe Addon for Elementor Branches
	elementorFrontend.hooks.addAction( 'frontend/element_ready/narestaurant_unique_branch_slider.default', function($scope, $){
	  $('.narep-branch-main').slick({
	    slidesToShow: 1,
	    arrows: false,
	    asNavFor: '.narep-branch-nav',
	    vertical: true,
	    autoplay: false,
	    verticalSwiping: true,
	    centerMode: false
	  });

	  $('.narep-branch-nav').slick({
	    slidesToShow: 4,
	    asNavFor: '.narep-branch-main',
	    dots: true,
	    vertical: true,
	    focusOnSelect: true,
	    autoplay: false,
	    centerMode: false
	  });
	} );
	
} );
})(jQuery);