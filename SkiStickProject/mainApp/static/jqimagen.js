$(document).ready(function(){
  $(".img-thumbnail").hover(function(){
    $(this).css({
      'transition': 'transform .2s',
      'transform' : 'scale(1.1)',
    });
    }, function(){
    $(this).css({
      'transition': 'transform .2s',
      'transform' : 'scale(1)',
    });
  });
});