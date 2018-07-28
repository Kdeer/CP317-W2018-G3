from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from subby.models.rating import Rating
from django.contrib.auth import get_user_model
from subby.decorators.loginrequiredmessage import message_login_required
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from subby.decorators.loginrequiredmessage import message_login_required

User = get_user_model()



def list_user_rating(request, user_id):
	ratings = Rating.objects.filter(reviewed_user_id=user_id)
	lister = User.objects.get(id=user_id)
	raters = []
	posted = False
	reviewed_user_id = user_id
	for rating in ratings:
		rater = User.objects.get(id=rating.user_id)
		raters.append(rater.email)
			 
	if request.user.is_anonymous:
		current = None
		current_id = None
	else:
		current = request.user.email
		current_id = request.user.id
		for rater in raters:
			if rater == current:
				posted = True
	avg_rating = Rating.objects.get_ratings()
	int_rating = int(avg_rating)
	float_rating = avg_rating - int_rating
	if float_rating > 0.5:
		float_rating = 0.5
		rest_rating = 4 - int_rating
	else:
		float_rating = 0
		rest_rating = 5 - int_rating
	avg = format(avg_rating, '.2f')
	return render(request, 'rating/rating_list.html', {'ratings': ratings, 'raters': raters, 'lister': lister, 'current': current, 'avg_rating':{'int_rating':range(int_rating), 'float_rating':float_rating,'rest_rating':range(rest_rating), 'avg':avg}, 'posted': posted, 'current_id':current_id, 'reviewed_user_id': reviewed_user_id})

	


@message_login_required
def write_review(request):
    if request.method == 'POST':
        current = request.user.email
        if request.POST['rating'] and request.POST['comment']:
            Rating.objects.create_rating(float(request.POST['rating']), request.POST['comment'], request.user.id, request.POST['reviewedid'])

            return redirect('subby:RatingList', request.POST['reviewedid'])
        else:
            return redirect('subby:RatingList', request.POST['reviewedid'])

		
@login_required(login_url="/signup/")	
def update_review(request):
    if request.method == 'POST':
        if request.user.is_anonymous:
            current = None
        else:
            current = request.user.email
        rating = Rating.objects.get(id=request.POST['ratingid'])
        if float(request.POST['rating']) != rating.rating:
            rating.set_rating(float(request.POST['rating']))
            rating.set_updated_at()
        if request.POST['comment'] != rating.comment:
            rating.set_comment(request.POST['comment'])


        rating.save()
        done = True
        return redirect(reverse('subby:RatingList', kwargs={'user_id':rating.reviewed_user_id}))
        # return render(request, 'rating/rating_detail.html', {'rating': rating, 'lister': request.user, 'done':done})
        


@login_required(login_url="/signup/")
def my_review(request, pk):
	rating = Rating.objects.filter(reviewed_user_id=pk, user_id=request.user.id)
	print(rating[0].rating)
	return render(request, 'rating/rating_detail.html', {'rating': rating[0], 'lister': request.user})
	
	
@login_required(login_url="/signup/")
def delete_review(request, rating_id, reviewed_user_id):
	Rating.objects.filter(id=rating_id).delete()
	
	return redirect('subby:RatingList', user_id=reviewed_user_id)

	