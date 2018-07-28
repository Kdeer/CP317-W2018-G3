$(function () {
    $('#write-review-submit').on('click', function () {
        let success = true;
        $('#write-radios').popover('hide');
        $('#message').popover('hide');
        if (!$("input[name='rating']:checked").val()) {
            $('#write-radios').popover('show');
            success = false;
        }
        if(!$('#message').val()){
            $('#message').popover('show');
            success = false;
        }
        return success;
    });
});