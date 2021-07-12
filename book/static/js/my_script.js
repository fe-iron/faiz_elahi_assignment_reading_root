const filter_values = [];
$(".filter a").click(function(e) {

  e.preventDefault();
  $("#showcase div").addClass('off');

  var id = $(this).attr('id');
  $("." + id).removeClass('off');

});

function check_box(val){
    if(val === 1){
      if(filter_values.length == 0){
        alert("First Select some filter values!");
      }else{
        $.ajax({
            type: 'GET',
                url: 'filter',
                data: {'name[]': filter_values},
                success: function(response){
                    books = response['book'];
                    $(".cards").addClass('off');
                    for(let i=0; i<books.length; i++){
                        $("#"+books[i]).removeClass("off");
                    }
                },
                error: function(response){
                    console.log("error: "+response);
                }
            })
      }
    }else{
        if(filter_values.indexOf(val) != -1){
            for( var i = 0; i < filter_values.length; i++){

                if ( filter_values[i] === val) {

                    filter_values.splice(i, 1);
                }
            }
        }else{
            filter_values.push(val);
        }
    }
}