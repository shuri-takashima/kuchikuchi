$(function(){
    $('.connection_btn_form').submit(function(event){
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: {
                'user_id': $(this).attr("id"),
            },
            dataType: 'json',
            success: function(response){
                if (response.checked){
                    $('#check_connection').html('unfollow')
                }
                else {
                    $('#check_connection').html('follow')
                }
                $('#follower_count').text(response.follower_count)
            }
        });
    });
});
