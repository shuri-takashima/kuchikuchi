//goodボタンの処理
//$(document).ready(function(event){
//    $(document).on('click', '#good', function(event){
//        event.preventDefault();
//        $.ajax({
//            type: 'POST',
//            url: "{% url 'content:good_btn' %}",
//            data: {
//                'content_id': $(this).attr('name'),
//                'csrfmiddlewaretoken': '{{ csrf_token }}', },
//            dataType: 'json',
//            success: function(response){
//                selector = document.getElementsByName(response.content_id)
//                if(response.gooded){
//                    $(selector).html('<i class="fas fa-lg fa-heart"></i>');
//                    $(selector).css('color', '#cb989c');
//                    $('#good_count').html(response.good_count)
//                }
//                else {
//                    $(selector).html('<i class="far fa-lg fa-heart"></i>');
//                    $(selector).css('color', '#cb989c');
//                }
//                $('#good_count').text(response.count);
//            }
//        });
//    });
//});
