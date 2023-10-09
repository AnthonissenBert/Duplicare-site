$(document).on('resize, ready', function() {
    // Add class if screen size equals
    var $window = $(window),
    $footer = $('footer');
   
    function resize() {
       if ($window.width() < 992) {
         return $footer.removeClass('fixed-bottom');
       }
       $window.resize(resize).trigger('resize');
    }
});