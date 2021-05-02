$(function(){
    $('#file_preview').hide();
    $('.file_preview_form').on('change', function(e){
        var reader = new FileReader();
        reader.onload = function(e){
            $('#file_preview').html("<source src='" + reader.result + "'/>")
            $('#file_preview').show();
        }
        reader.readAsDataURL(e.target.files[0]);
    });
});