$.fn.extend({   
        // Devuelve true si el elemento está en window
        isInScene : function(arg)
        {   
            // Fuerza que arg sea un objeto
            arg = arg || {};
            // Valor por defecto de desfase
            arg.desfase = arg.desfase || 0;
            // Fuerza a que desfase sea númerico
            arg.desfase = parseInt(arg.desfase,10);
     
            // Posición vertical del elemento respecto al principio del documento
            var pos_container = $(this).offset().top;
     
            // Altura del elemento
            var container_height = $(this).outerHeight();
     
            // Posición vertical de document
            var pos_document = $(document).scrollTop();
     
            // Alto ventana
            var window_height = $(window).height(); 
     
            return (pos_document+window_height > pos_container+arg.desfase && pos_container+container_height > pos_document+arg.desfase);
        }
    });
     
    // Utilizamos el método isInScene
    $(document).scroll(function(e)
    {   
        if( $("#components").isInScene()){
            $('#components').addClass('animated bounceInLeft');
        }else{
            $('#components').removeClass('animated bounceInLeft');
        }   

        if( $("#team").isInScene()){
            $('#team').addClass('animated bounceInRight');
        }else{
            $('#team').removeClass('animated bounceInRight');
        }

        if( $("#pricing").isInScene()){
            $('#pricing').addClass('animated bounceInLeft');
        }else{
            $('#pricing').removeClass('animated bounceInLeft');
        }   

        if( $("#contact").isInScene()){
            $('#contact').addClass('animated bounceInRight');
        }else{
            $('#contact').removeClass('animated bounceInRight');
        }
    });