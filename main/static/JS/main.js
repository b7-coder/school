//burger menu
$(document).ready(function() {
    $(".menuTooggle").click(function() {
      $(this).toggleClass("active");
      $('.header__menu').slideToggle(0, function(){
        if($(this).css('display') === "none"){
          $(this).removeAttr('style');
        }
      });
    });
  });

