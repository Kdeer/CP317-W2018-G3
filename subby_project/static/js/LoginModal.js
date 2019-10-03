$(function () {
    $('.login-btn').on('click', function () {
        $('#signup-modal').modal('hide');
        $('#login-modal').modal('show');
    });

    $('.signup-btn').on('click', function () {
        $('#login-modal').modal('hide');
        $('#signup-modal').modal('show');
    });

    let uwaterloo_email = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@uwaterloo.ca$/;
    let mylaurier_email = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@mylaurier.ca$/;
    let wlu_email = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@wlu.ca$/;
    let uwaterloo_new = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@edu.uwaterloo.ca$/;
    let passwordCheck = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/;

    $('#submit-login-btn').on('click', function () {
        let email = $('#email-box').val();
        if (!email || (!uwaterloo_email.test(email) && !mylaurier_email.test(email)
            && !wlu_email.test(email) && !uwaterloo_new.test(email))) {
            $('#email-box').popover('show');
            return false;
        }
    });

    $('#signup-submit-btn').on('click', function () {
        $('#su-email-box').popover('hide');
        $('#su-pw-box').popover('hide');
        $('#pw-confirm-box').popover('hide');
        $('#su-username-box').popover('hide');
        let email = $('#su-email-box').val();
        let pw = $('#su-pw-box').val();
        let pw_confirm = $('#pw-confirm-box').val();
        let username = $('#su-username-box').val();
        let error = false;
        if (!email || (!uwaterloo_email.test(email) && !mylaurier_email.test(email)
            && !wlu_email.test(email) && !uwaterloo_new.test(email))) {
            $('#su-email-box').popover({
                content: "Please enter a valid email",
                html: true,
                trigger: "manual",
                placement: "right"
            }).popover('toggle');
            error = true;
        }
        if (!pw || pw.length < 8 || !passwordCheck.test(pw)) {
            $('#su-pw-box').popover('show');
            error = true;
        }

        if (!pw_confirm || pw_confirm !== pw) {
            $('#pw-confirm-box').popover('show');
            error = true;
        }
		
		if (!username || username.length > 20) {
			$('#su-username-box').popover('show');
		}

        if (error) {
            return false;
        }

    });

});
