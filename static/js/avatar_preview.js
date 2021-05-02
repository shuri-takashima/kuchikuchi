$(function(){
    $('#img_preview').hide();
    $('.img_preview_form').on('change', function(e){
        var reader = new FileReader();
        reader.onload = function(e){
            $('#img_preview').attr('src', e.target.result);
            $('#img_preview').show();
        }
        reader.readAsDataURL(e.target.files[0]);

    });
});