$(function(){
  $('.edit-btn').on('click', function(){
    $('.edit-disabled-fieldset').prop('disabled', false);
    $(this).attr('style', 'display: none;');
    $('.acc-submit-btn').attr('style', '');
  });

  $('.lock-account-btn').on('click', function() {
    $el = $('.lock-account-btn');
    $alertEl = $('.ajax-alert');
    token = $('[name=csrfmiddlewaretoken]').val();

    res = $.ajax({
      type: "POST",
      headers: { "X-CSRFToken": token },
      url: $el.data('lock-url'),
      success: function(data) {
        $el.toggleClass('btn-danger');
        $el.toggleClass('btn-secondary');

        if (data.is_active) {
          $el.html('Lock Account');
        } else {
          $el.html('Unlock Account');
        }

        $alertEl.css('display', 'none');
      },
      error: function(jqXHR, status, err) {
        $alertEl.css('display', 'block');
        $alertEl.addClass('alert-danger');
        $alertEl.html("Unable to lock the user account: ", err);
      }
    });
  });
});
