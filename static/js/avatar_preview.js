$(function(){
    $('.img_preview_form').on('change', function(e){
        var reader = new FileReader();
        $('.my_profile_img').remove();
        reader.onload = function(e){
            $('label[for="id_avatar"]').append('<img src="' + e.target.result +'" class="my_profile_img">')
        }
        reader.readAsDataURL(e.target.files[0]);

    });
});