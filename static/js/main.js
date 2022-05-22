'use strict';

(function ($) {

    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");
    });

    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    $('.search-switch').on('click', function () {
        $('.search-model').fadeIn(400);
    });

    $('.search-close-switch').on('click', function () {
        $('.search-model').fadeOut(400, function () {
            $('#search-input').val('');
        });
    });

    $(".canvas__open").on('click', function () {
        $(".offcanvas-menu-wrapper").addClass("active");
        $(".offcanvas-menu-overlay").addClass("active");
    });

    $(".offcanvas-menu-overlay").on('click', function () {
        $(".offcanvas-menu-wrapper").removeClass("active");
        $(".offcanvas-menu-overlay").removeClass("active");
    });

    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });


    $(".hero__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: false,
        nav: true,
        navText: ["<i class='fa fa-angle-left'><i/>", "<i class='fa fa-angle-right'><i/>"],
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true
    });

    $(".categories__slider").owlCarousel({
        loop: true,
        margin: 22,
        items: 5,
        dots: false,
        nav: true,
        navText: ["<span class='arrow_carrot-left'><span/>", "<span class='arrow_carrot-right'><span/>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: false,
        responsive: {
            0: {
                items: 1,
                margin: 0
            },
            480: {
                items: 2
            },
            768: {
                items: 3
            },
            992: {
                items: 4
            },
            1200: {
                items: 5
            }
        }
    });

    $('input[name=phone]').mask("+996 (111) 11-11-11");

    $(".testimonial__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 2,
        dots: true,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            }
        }
    });

    $(".related__products__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 4,
        dots: false,
        nav: true,
        navText: ["<span class='arrow_carrot-left'><span/>", "<span class='arrow_carrot-right'><span/>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            768: {
                items: 3
            },
            992: {
                items: 4
            },
        }
    });

    $("select").niceSelect();

    $('.video-popup').magnificPopup({
        type: 'iframe'
    });

    $('#bar1').barfiller({
        barColor: '#111111',
        duration: 2000
    });
    $('#bar2').barfiller({
        barColor: '#111111',
        duration: 2000
    });
    $('#bar3').barfiller({
        barColor: '#111111',
        duration: 2000
    });

    $('.product__details__thumb img').on('click', function () {
        $('.product__details__thumb .pt__item').removeClass('active');
        $(this).addClass('active');
        var imgurl = $(this).data('imgbigurl');
        var bigImg = $('.big_img').attr('src');
        if (imgurl != bigImg) {
            $('.big_img').attr({
                src: imgurl
            });
        }
    });

    var proQty = $('.pro-qty');
    proQty.prepend('<span class="dec qtybtn">-</span>');
    proQty.append('<span class="inc qtybtn">+</span>');
    proQty.on('click', '.qtybtn', function () {
        var $button = $(this);
        var oldValue = $button.parent().find('input').val();
        if ($button.hasClass('inc')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        $button.parent().find('input').val(newVal);
    });

    

    $(".product__details__thumb").niceScroll({
        cursorborder: "",
        cursorcolor: "rgba(0, 0, 0, 0.5)",
        boxzoom: false
      });

})(jQuery);