jQuery(document).ready(function($) {
  "use strict";

  //Naeep Hover Script
  $('.narep-chefs-food, .narep-addon-menu-wrap, .narep-food-item, .narep-particular-wrap, .narep-food-menu-item-wrap, .narep-aboutus-item, .narep-aboutme-item, .narep-benefit-item, .narep-care-item, .narep-tool-item, .narep-restaurant-item, .narep-stats-item, .narep-price-item, .narep-service-item, .narep-news-item, .narep-gallery-item, .narep-contact-item, .narep-mate-item, .narep-video-wrap, .narep-history-item').hover (
    function() {
      $(this).addClass('narep-hover');
    },
    function() {
      $(this).removeClass('narep-hover');
    }
  );

  // Scrollax Init
  $.Scrollax();

  // Slick Vertical Slider
  jQuery('.slick-vertical-slider').not('.slick-initialized').slick ({
    dots: false,
    vertical: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    verticalSwiping: true,
  });

  //Owl Carousel Slider Script
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

  //Counter Script
  $('.stats-counter').counterUp ({
    delay: 1,
    time: 1000,
  });

  // Match Height Script
  $('.narep-item').matchHeight();

  //Naeep Masonry Script
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
    $gridContainer.find('.masonry-filters.normal-filter').on('click', 'li a', function() {
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

  //Naeep Popup Picture Script
  $('.narep-popup').magnificPopup ({
    delegate: 'a',
    type: 'image',
    closeOnContentClick: false,
    closeBtnInside: false,
    mainClass: 'mfp-with-zoom mfp-img-mobile',
    closeMarkup:'<div class="mfp-close" title="%title%"></div>',
    image: {
      verticalFit: true,
      titleSrc: function(item) {
        return item.el.attr('title') + ' &middot; <a class="image-source-link" href="'+item.el.attr('data-source')+'" target="_blank">image source</a>';
      }
    },
    gallery: {
      enabled: true,
      arrowMarkup:'<div title="%title%" class="mfp-arrow mfp-arrow-%dir%"></div>',
    },
    zoom: {
      enabled: true,
      duration: 300,
      opener: function(element) {
        return element.find('*');
      }
    }
  });

  //Naeep Magnific Popup Video Script
  $('.narep-popup-video').magnificPopup ({
    mainClass: 'mfp-fade',
    type: 'iframe',
    closeMarkup:'<div class="mfp-close" title="%title%"></div>',
    iframe: {
      patterns: {
        youtube: {
          index: 'youtube.com/',
          id: function(url) {
            var m = url.match(/[\\?\\&]v=([^\\?\\&]+)/);
            if ( !m || !m[1] ) return null;
            return m[1];
          },
          src: 'https://www.youtube.com/embed/%id%?autoplay=1'
        },
        vimeo: {
          index: 'vimeo.com/',
          id: function(url) {
            var m = url.match(/(https?:\/\/)?(www.)?(player.)?vimeo.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*/);
            if ( !m || !m[5] ) return null;
            return m[5];
          },
          src: 'https://player.vimeo.com/video/%id%?autoplay=1'
        },
        dailymotion: {
          index: 'dailymotion.com/',
          id: function(url) {
            var m = url.match(/^.+dailymotion.com\/(video|hub)\/([^_]+)[^#]*(#video=([^_&]+))?/);
            if ( !m || !m[2] ) return null;
            return m[2];
          },
          src: 'https://iframespot.blogspot.com/ncr/?m=0&type=dv&url=https%3A%2F%2Fwww.dailymotion.com%2Fembed%2Fvideo%2F%id%%3Fapi%3D0%26autoplay%3D1%26info%3D0%26logo%3D0%26social%3D0%26related%3D0'
        }
      }
    }
  });
  if ($('div').hasClass('narep-popup')) {
    $('.narep-popup').find('a').attr("data-elementor-open-lightbox","no");
  }
  //Naeep Add Class In Previous Items
  $('.narep-process-item').hover(function() {
    $(this).prevAll('.narep-process-item').toggleClass('process-done');
  });

  // Naeep Tab
  $('.narep-tab-links a').on('click', function(e) {
    var currentAttrValue = $(this).attr('href');

    // Show/Hide Tabs
    $('.narep-tab-content ' + currentAttrValue).fadeIn(0).siblings().hide().stop(true, true);
    $('.narep-tab-content ' + currentAttrValue).addClass('active').siblings().removeClass('active');

    // Change/remove current tab to active
    $(this).parent('li').addClass('active').siblings().removeClass('active');

    e.preventDefault();
  });

  // Naeep Food Tab
  $('.narep-food-tab a').on('click', function(e) {
    var currentAttrValue = $(this).attr('href');

    // Show/Hide Tabs
    $('.narep-tab-food ' + currentAttrValue).fadeIn(0).siblings().hide().stop(true, true);
    $('.narep-tab-food ' + currentAttrValue).addClass('active').siblings().removeClass('active');

    // Change/remove current tab to active
    $(this).addClass('active').siblings().removeClass('active');

    e.preventDefault();
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

  // Naeep Pricing Tab
  $('.narep-price-tab-links a').on('click', function(e) {
    var currentAttrValue = $(this).attr('href');

    // Show/Hide Tabs
    $('.narep-price-tab-content ' + currentAttrValue).fadeIn(0).siblings().hide().stop(true, true);
    $('.narep-price-tab-content ' + currentAttrValue).addClass('active').siblings().removeClass('active');

    // Change/remove current tab to active
    $(this).addClass('active').siblings().removeClass('active');

    e.preventDefault();
  });

  setTimeout(function() {
    $('.narep-cta').addClass('active');
  }, 6000);
  $('.cta-close').click(function() {
    $('.narep-cta').fadeOut('normal', function() {
      $(this).remove();
      $('.narep-cta').removeClass('active');
    });
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
  //Addon Menu Script
  $('.narep-addon-menu-wrap').each(function (index) {
      $(this).find('.narep-addon-item :checkbox').on("change", function() {
          var baseTotal = $(this).parents(".narep-addon-menu-wrap").find(".addon-total").attr("data-price");
          var sum = 0, addons = {};
          sum = parseFloat(baseTotal);
          $(this).parents(".narep-addon-menu-wrap").find(".narep-addon-item :checkbox:checked").each(function() {
              sum += ~~$(this).val();
              addons[$(this).attr('data-title')] = $(this).val();
          });                  
          $(this).parents(".narep-addon-menu-wrap").find(".addon-total span").text(sum);
          $(this).parents(".narep-addon-menu-wrap").find(".narep-cart-action").attr('data-total', sum);
          $(this).parents(".narep-addon-menu-wrap").find(".narep-cart-action").attr('data-addons', JSON.stringify(addons));
      });
  });

  var RSilderIndex = $('.closed-time').length;
  $('.flick-carousel').attr('data-initialindex', RSilderIndex);
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

  //Flickity Carousel Slider Script
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

  //Gift Card Script
  if ($('div').hasClass('narep-gift-form')) {
    var rNameOut = document.getElementById("recipientName").innerHTML;
    $("#recipient-name").keyup(function(){
      var rNameIn = document.getElementById("recipient-name").value;
      if(rNameIn.length) {
        document.getElementById("recipientName").innerHTML = rNameIn;
      } else {
        document.getElementById("recipientName").innerHTML = rNameOut;
      }
    });

    var rAmountOut = document.getElementById("recipientAmount").innerHTML;
    $("#card-amount").keyup(function(){
      var rAmountIn = document.getElementById("card-amount").value;
      if(rAmountIn.length) {
        document.getElementById("recipientAmount").innerHTML = rAmountIn;
      } else {
        document.getElementById("recipientAmount").innerHTML = rAmountOut;
      }
    });

    var rMessageOut = document.getElementById("recipientMessage").innerHTML;
    $("#card-message").keyup(function(){
      var rMessageIn = document.getElementById("card-message").value;
      if(rMessageIn.length) {
        document.getElementById("recipientMessage").innerHTML = rMessageIn;
      } else {
        document.getElementById("recipientMessage").innerHTML = rMessageOut;
      }
    });
  }

  // Date picker
  $('.narep-datepicker').datepicker({
    format: 'yyyy-mm-dd',
    startDate: '-3d',
    autoclose: true,
  });
  // Time picker
  $('.narep-timepicker').timepicker({
    timeFormat: 'H:mm',
    interval: 30,
    minTime: '12:00am',
    maxTime: '11:30pm',
    dynamic: false,
    dropdown: true,
    scrollbar: false
  });

  // Open Table Submit
  $('#narep-tbDate, #narep-tbTime').on('click mouseenter', function() {
    $('#narep-tbDateTime').val($('#narep-tbDate').val() + 'T' + $('#narep-tbTime').val());
  });
  $('.style-one button.narep-btn').on('click mouseenter', function() {
    $('#narep-tbDateTime').val($('#narep-tbDate').val() + 'T' + $('#narep-tbTime').val());
  });
  $('.narep-dateradio, .narep-bookradio').on('click mouseleave', function() {
    $('#narep-tbDateTime').val($('.narep-dateradio:checked').val() + 'T' + $('.narep-bookradio:checked').val());
  });
  $('.style-two button.narep-btn').on('click mouseenter', function() {
    $('#narep-tbDateTime').val($('.narep-dateradio:checked').val() + 'T' + $('.narep-bookradio:checked').val());
  });

  $('.narep-dateradio').on('click', function() {
    // Create date from input value
    var inputDate = new Date($('.narep-dateradio:checked').val());
    // Get today's date
    var todaysDate = new Date();
    if (inputDate.setHours(0,0,0,0) == todaysDate.setHours(0,0,0,0)) {
      $('.narep-radio-slider').addClass('today-slot');
    } else {
      $('.narep-radio-slider').removeClass('today-slot');
    }
  });

  // Plus Minus Incremeny
  function narep_quantity_increments() {
    jQuery("div.narep-quantity:not(.narep-buttons-added), td.narep-quantity:not(.narep-buttons-added)").each(function(a, b) {
      var c = jQuery(b);
      c.addClass("narep-buttons-added"), c.children().first().before('<input type="button" value="-" class="narep-minus" />'), c.children().last().after('<input type="button" value="+" class="narep-plus" />')
    })
  }
  String.prototype.getDecimals || (String.prototype.getDecimals = function() {
    var a = this,
    b = ("" + a).match(/(?:\.(\d+))?(?:[eE]([+-]?\d+))?$/);
    return b ? Math.max(0, (b[1] ? b[1].length : 0) - (b[2] ? +b[2] : 0)) : 0
  }), jQuery(document).ready(function() {
      narep_quantity_increments()
  }), jQuery(document).on("updated_wc_div", function() {
      narep_quantity_increments()
  }), jQuery(document).on("click", ".narep-plus, .narep-minus", function() {
    var a = jQuery(this).closest(".narep-quantity").find(".narep-qty"),
        b = parseFloat(a.val()),
        c = parseFloat(a.attr("max")),
        d = parseFloat(a.attr("min")),
        e = a.attr("step");
    b && "" !== b && "NaN" !== b || (b = 0), "" !== c && "NaN" !== c || (c = ""), "" !== d && "NaN" !== d || (d = 0), "any" !== e && "" !== e && void 0 !== e && "NaN" !== parseFloat(e) || (e = 1), jQuery(this).is(".narep-plus") ? c && b >= c ? a.val(c) : a.val((b + parseFloat(e)).toFixed(e.getDecimals())) : d && b <= d ? a.val(d) : b > 0 && a.val((b - parseFloat(e)).toFixed(e.getDecimals())), a.trigger("change")
  });

  var iCnt = 1;
  var container = $('.narep-seats');

  $('.narep-plus').click(function() {
    if (iCnt <= 19) {
      iCnt = iCnt + 1;
      $(container).find('.narep-plate' + iCnt).fadeIn(400).addClass('active');
    }
  });

  $('.narep-minus').click(function() {
    if (iCnt != 1) {
      $('.narep-plate' + iCnt).fadeOut(400).removeClass('active');
      iCnt = iCnt - 1;
    }
  });

  $('.narep-branch-main').not('.slick-initialized').slick({
    slidesToShow: 1,
    arrows: false,
    asNavFor: '.narep-branch-nav',
    vertical: true,
    autoplay: false,
    verticalSwiping: true,
    centerMode: false
  });

  $('.narep-branch-nav').not('.slick-initialized').slick({
    slidesToShow: 4,
    asNavFor: '.narep-branch-main',
    dots: true,
    vertical: true,
    focusOnSelect: true,
    autoplay: false,
    centerMode: false,
    responsive: [
      {
        breakpoint: 991,
        settings: {
          vertical: false,
          slidesToShow: 2,
        }
      },
      {
        breakpoint: 768,
        settings: {
          vertical: false,
          slidesToShow: 1,
        }
      },
    ]
  });

  // Naeep Branch
  $('.narep-address-trigger').on('click', function(e) {
    $(this).toggleClass('active').next().toggleClass('active');
    e.preventDefault();
  });

  $('.elementor-element').each( function() {
    if ($(this).data('nich-link')!==undefined) {
      $(this).append( "<a href='"+$(this).data('nich-link')+"' target='_blank' class='narep-btn narep-pro-btn'>"+$(this).data('nich-text')+"</a>" );
    }
  });

});