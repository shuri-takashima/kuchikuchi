$(function(){
    $(".good_btn_form").submit(function(event){
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: $(this).attr("action"),
            data: {
                'content_id': $(this).attr("id"),
            },
            dataType: 'json',
            success: function(response){
                if(response.gooded){
                    $(".good_btn").html('<i class="fas fa-lg fa-heart submit_icon"></i>');
                }
                else {
                    $(".good_btn").html('<i class="far fa-lg fa-heart submit_icon"></i>');
                }
                $('#good_count').text(response.count);
            }
        });
    });
});