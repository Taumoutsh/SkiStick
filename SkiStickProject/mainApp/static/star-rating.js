$(function(){
    $('.star-rating .fa').on('mouseover', function(){
        $(this).removeClass('fa fa-star-o').addClass('fa fa-star');
        $(this).prevAll().removeClass('fa fa-star-o').addClass('fa fa-star');
        $(this).nextAll().removeClass('fa fa-star').addClass('fa fa-star-o');
    });

    $('.star-rating').on('mouseleave', function(){
        active = $(this).parent().find('.selected');
        if(active.length) {
            active.removeClass('fa fa-star-o').addClass('fa fa-star');
            active.prevAll().removeClass('fa fa-star-o').addClass('fa fa-star');
            active.nextAll().removeClass('fa fa-star').addClass('fa fa-star-o');
        } else {
            $(this).find('.fa').removeClass('fa fa-star').addClass('fa fa-star-o');
        }
    });

    $('.star-rating .fa').click(function(){
        if($(this).hasClass('selected')) {
            $('.star-rating .selected').removeClass('selected');
        } else {
            $('.star-rating .selected').removeClass('selected');
            $(this).addClass('selected');
        }
    });

    $('.star-rating').on("click", function() {
        var rating = $('.fa-star').length;
        $('#form_calificacion').val(rating);
    });
});
