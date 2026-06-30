$(document).ready(function() {
    var $footer = $('footer.fixed-bottom');
    if ($footer.length) {
        function checkWidth() {
            if ($(window).width() < 992) {
                $footer.css('position', 'relative');
            } else {
                $footer.css('position', '');
            }
        }
        $(window).on('resize', checkWidth);
        checkWidth();
    }
});
