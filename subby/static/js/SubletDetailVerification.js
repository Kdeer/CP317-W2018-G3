$(function () {

    $('#contact-submit-btn').on('click', function (e) {
        $('#name').popover('hide');
        $('#email').popover('hide');
        $('#message').popover('hide');
        let name = $('#name').val();
        let email = $('#email').val();
        let message = $('#message').val();
        let error = false;
        if (!name) {
            $('#name').popover('show');
            error = true;
        }
        if (!email) {
            $('#email').popover('show');
            error = true;
        }
        if (!message) {
            $('#message').popover('show');
            error = true;
        }
        if (error) {
            e.preventDefault();
            return false;
        }

    });

    $('#edit-sublet-confirm').on('click', function(e){
       let title = $('#listing-title');
       let street_address = $('#street_address');
       let city = $('#city');
       let postal_code = $('#postal_code');
       let price = $('#price');
       let description = $('#listing-description');
       let lat = $('#lat');
       let lng = $('#lng');
       let error = false;

       title.popover('hide');
       price.popover('hide');
       description.popover('hide');
       $('#pac-input').popover('hide');

       if(!title.val()){
           title.popover('show');
           error = true;
       }
       if(!street_address.val() || !city.val() || !postal_code.val() || !lat.val() || !lng.val()){
           $('#pac-input').popover('show');
           error = true;
       }
       if(!price.val()){
           price.popover('show');
           error = true;
       }
       if(!description.val()){
           description.popover('show');
           error = true;
       }
       if(error){
           e.preventDefault();
           return false;
       }

    });
});