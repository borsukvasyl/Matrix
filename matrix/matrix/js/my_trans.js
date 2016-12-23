function create_list(){
        var list = ''
        for(i=1;i<=6;i++){
            list+='<option value="'+i+'">'+i+'x'+i+'</option>'
        }
        $('#sel').html(list)
    }
    
    function change_matrix_size(){
        
        $('#sel').click(function(){
        
            var size = $(this).val()
            
            if (size >= 1 && size <= 6){
                $('#matrix_form').html(create_matrix(size))
            }else{
                $('#matrix_form').text('')
            }
        })
    }
    
    function create_matrix(size){
        var matrix = '<table cellspacing="7" cellpadding="5" border=\'0\'>'
        for(i=0;i<size;i++){
            matrix += '<tr align=\'center\'>'
            for(j=0;j<size;j++){
                matrix += '<td>('+i+','+j+')<br><input type="checkbox" name="('+i+','+j+')"></td>'
            }
            matrix += '</tr>'
        }
        matrix += '</table>'
        matrix += '<input type=\'submit\' value=\'Create\'>'
        return(matrix)
    }
    
    function logo(){
        $(body).mousemove(function(){
            
        })
    }