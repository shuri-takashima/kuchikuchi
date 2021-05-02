$(function(){
    $("#comment_btn_form").submit(function(event){
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: $(this).attr("action"),
            data: {
                'content_id': $(this).attr("class"),
                'comment': $('#id_comment').val(),
            },
            dataType: 'json',
            success: function(response){
                $('#id_comment').val('');
                $('#comment_add')
                    .after('<div class="shadow-sm rounded-pill comment_area"><diV class="flex-column comment_box"><div id="comment_user_username"><img class="my_img"src="' + response.avatar_url + '">' + response.username + '</div><div class="text-break comment_detail" >' + response.comment + '</div></diV></div>')
            }
        });
    });
});