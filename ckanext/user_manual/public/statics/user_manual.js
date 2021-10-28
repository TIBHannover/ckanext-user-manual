$(document).ready(function(){    
    $('.menu-item').click(function(){
        let bodies = $('.menu-item-body');
        for(let i=0;i < bodies.length; i++){
            if($(this).siblings('.menu-item-body').attr('id') !== $(bodies[i]).attr('id')){
                $(bodies[i]).fadeOut();    
            }
        }
        if($(this).siblings('.menu-item-body').is(':hidden')){
            $(this).siblings('.menu-item-body').fadeIn();    
        }
        else{
            $(this).siblings('.menu-item-body').fadeOut();
        }        
    });
});