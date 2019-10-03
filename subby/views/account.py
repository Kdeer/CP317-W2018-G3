from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from subby.decorators.loginrequiredmessage import message_login_required
from subby.models.sublet import Sublet
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

import datetime, pytz

@message_login_required
def account_home(request):
	id = request.user.id
	email = request.user.email
	first_name = request.user.first_name
	last_name = request.user.last_name
	created_at = request.user.created_at
	updated_at = request.user.updated_at
	phone_number = request.user.phone_number
	username = request.user.username
	
	user_dict = {
		'id' : id,
		'email': email,
		'first_name': first_name,
		'last_name': last_name,
		'created_at': created_at,
		'updated_at': updated_at,
		'phone_number': phone_number,
		'username': username,
	}
	return render(request, 'users/account_home.html', user_dict)

@message_login_required
def update_user_info(request):
	if request.method == 'POST':
			user = User.objects.get(email=request.user.email)
			user.first_name = request.POST['first']
			user.last_name = request.POST['last']
			user.phone_number = request.POST['phone']
			user.updated_at = pytz.utc.localize(datetime.datetime.now())
			user.save()
			return redirect('subby:account_home')
	else:
		#User wants to enter info
		return render(request, 'application/base.html')




