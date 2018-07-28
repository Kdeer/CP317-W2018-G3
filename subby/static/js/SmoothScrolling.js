$(function () {
    $('.scroll-btn.right-scroll').on('click', function (e) {
        $('#image-gallery').animate({scrollLeft: '+=500'}, 800, 'linear');
    });
    $('.scroll-btn.left-scroll').on('click', function (e) {
        $('#image-gallery').animate({scrollLeft: '-=500'}, 800, 'linear');
    });
});