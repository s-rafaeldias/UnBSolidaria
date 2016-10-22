$(document).ready(function() {

/*----------------------------------------------------*/
/*	Sequence Slider
/*----------------------------------------------------*/
     
$(function(){
    var options = {
        nextButton: true,
        prevButton: true,
        pagination: true,
        animateStartingFrameIn: true,
        autoPlay: true,
        autoPlayDelay: 3000,
        preloader: true,
        preloadTheseFrames: [1],
    };
    
    var mySequence = $("#sequence").sequence(options).data("sequence");
});

/*----------------------------------------------------*/
/*	Portfolio Mixitup
/*----------------------------------------------------*/

$(function(){
         $('#Grid').mixitup({
                targetSelector: '.mix',
                filterSelector: '.filter',
                effects: ['fade','blur'],
                easing: 'smooth',

            });
});
    
/*----------------------------------------------------*/
/*	Flexisel Clientslider
/*----------------------------------------------------*/

$("#clientslider").flexisel({
        visibleItems: 5,
        animationSpeed: 1000,
        autoPlay: false,
        autoPlaySpeed: 3000,            
        pauseOnHover: true,
        enableResponsiveBreakpoints: true,
        responsiveBreakpoints: { 
            portrait: { 
                changePoint:480,
                visibleItems: 1
            }, 
            landscape: { 
                changePoint:640,
                visibleItems: 2
            },
            tablet: { 
                changePoint:768,
                visibleItems: 3
            }
        }
});

/*----------------------------------------------------*/
/*	Sticky Nav
/*----------------------------------------------------*/

$(window).load(function(){
      $("#menu").sticky({ topSpacing: 0 });
});

/*----------------------------------------------------*/
/*	MagnificPopup
/*----------------------------------------------------*/

$(function(){
  $('.magnific-popup').magnificPopup({type:'image'});
});

/*----------------------------------------------------*/
/*	About Us BxSlider
/*----------------------------------------------------*/

$(function(){          
             $('.aboutus').bxSlider({
                 mode: 'horizontal',
                 slideMargin: 3,
                 auto:true
             });             
});


/*----------------------------------------------------*/
/*	Testemonials BxSlider
/*----------------------------------------------------*/

$(function(){            
             $('.testemonials').bxSlider({
                 mode: 'horizontal',
                 slideMargin: 3,
                 auto:true
             });             
});


/*----------------------------------------------------*/
/*	Portfolio Hover Overlay
/*----------------------------------------------------*/

$('.overlay').hover(
        function(){
            $(this).find('.caption').fadeIn(550); 
        },
        function(){
            $(this).find('.caption').fadeOut(550); 
        }
); 

/*----------------------------------------------------*/
/*	Color Switch Panel
/*----------------------------------------------------*/

$('.switch').click(function(){

        if($('.editor').css('left') == '-150px'){
            $('.editor').animate({
                left: '-2px'
            });
        }
        else{
            $('.editor').animate({
                left: '-150px'
            });
        }

});

/*----------------------------------------------------*/
/*	Change CSS ( Color Change )
/*----------------------------------------------------*/

$(function(){ 
	     $('#changecss').styleSwitcher();
});

/*----------------------------------------------------*/
/*	Back to the Top Button
/*----------------------------------------------------*/

$(function(){
    $(window).scroll(function() { 
        if ($(this).scrollTop() > 1200) {
            $("#top-bt:hidden").css('visibility','visible');   
            $("#top-bt:hidden").fadeIn('550');  
        } 
        else {     
            $("#top-bt:visible").fadeOut("550"); 
        }  
    });
});
    
});