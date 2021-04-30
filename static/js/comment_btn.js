$(function(){
    $("#comment_btn_form").submit(function(event){
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: $(this).attr("action"),
            data: {
                'content_id': $(this).attr("class"),
                'comment': $('#comment_input').val(),
            },
            dataType: 'json',
            success: function(response){
                $('#comment_input').val('');
                $('#comment_info').append('<p>' + response.comment + '</p>');
                $('#comment_user_username').append('<p>' + response.username + '<p>');
                $('#comment_user_img').append('<img src="' + response.avatar_url + '">');
            }
        });
    });
});