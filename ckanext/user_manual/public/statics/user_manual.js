$(document).ready(function(){    
    $('.menu-item').click(function(){
        let bodies = $('.menu-item-body');
        for(let i=0;i < bodies.length; i++){
            if($(this).siblings('.menu-item-body').attr('id') !== $(bodies[i]).attr('id')){
                $(bodies[i]).fadeOut();
                $(bodies[i]).siblings('.menu-item').find('i').removeClass('fa-minus');
                $(bodies[i]).siblings('.menu-item').find('i').addClass('fa-plus');
                                                 
            }
        }
        if($(this).siblings('.menu-item-body').is(':hidden')){
            $(this).siblings('.menu-item-body').fadeIn();
            $(this).find('i').removeClass('fa-plus');
            $(this).find('i').addClass('fa-minus');    
        }
        else{
            $(this).siblings('.menu-item-body').fadeOut();
            $(this).find('i').removeClass('fa-minus');
            $(this).find('i').addClass('fa-plus'); 
        }        
    });
});