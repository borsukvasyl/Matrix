function create_list(){
        var list = ''
        for(i=1;i<=4;i++){
            list+='<option value="'+i+'">'+i+'x'+i+'</option>'
        }
        $('#sel1').html(list)
        $('#sel2').html(list)
    }
    
    function change_matrix_size(){
        
        $('#sel1').click(function(){
        
            var size = $(this).val()
            
            if (size >= 1 && size <= 6){
                $('#matrix_form1').html(create_matrix(1, size))
                $('#matrix_form2').html(create_matrix(2, size))
                
            }else{
                $('#matrix_form1').text('')
            }
        })
        
        
    }
    
    function create_matrix(num, size){
        var matrix = '<table cellspacing="7" cellpadding="5" border=\'0\'>'
        for(i=0;i<size;i++){
            matrix += '<tr align=\'center\'>'
            for(j=0;j<size;j++){
                matrix += '<td>('+i+','+j+')<br><input type="checkbox" name="('+num+','+i+','+j+')"></td>'
            }
            matrix += '</tr>'
        }
        matrix += '</table>'
        return(matrix)
    }