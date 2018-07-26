from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from subby.models.rating import Rating
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

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
	else:
		current = request.user.email
		current_id = request.user.id
		for rater in raters:
			if rater == current:
				posted = True
	avg_rating = Rating.objects.get_ratings()
	# print(avg_rating)
	return render(request, 'rating/rating_list.html', {'ratings': ratings, 'raters': raters, 'lister': lister, 'current': current, 'avg_rating':avg_rating, 'posted': posted, 'current_id':current_id, 'reviewed_user_id': reviewed_user_id})

	


@login_required(login_url="/signup/")
def write_review(request):
    if request.method == 'POST':
        current = request.user.email
        if request.POST['rating'] and request.POST['comment']:
            Rating.objects.create_rating(float(request.POST['rating']), request.POST['comment'], request.user.id, request.POST['reviewedid'])
            print(request.POST['reviewedid'])
            ratings = Rating.objects.filter(reviewed_user_id=request.POST['reviewedid'])
            lister = User.objects.get(id=request.POST['reviewedid'])
            raters = []
            for rating in ratings:
                rater = User.objects.get(id=rating.user_id)
                raters.append(rater.email)
            # return render(request, 'rating/rating_list.html',
                          # {'ratings': ratings,
                           # 'raters': raters,
                           # 'lister': lister,
                           # 'success': 'You have successfully left a review!',
                           # 'current': current})
            return redirect('subby:RatingList', request.POST['reviewedid'])
        else:
            ratings = Rating.objects.filter(user_id=request.POST['reviewedid'])
            lister = User.objects.get(id=request.POST['reviewedid'])
            raters = []
            for rating in ratings:
                rater = User.objects.get(id=rating.user_id)
                raters.append(rater.email)
            return render(request, 'rating/rating_list.html',
                          {'ratings': ratings,
                           'raters': raters,
                           'lister': lister,
                           'error': 'Please fill in all fields when leaving a review.',
                           'current': current})
    else:
        return redirect('subby:RatingList')

		
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
        if request.POST['comment'] != rating.comment:
            rating.set_comment(request.POST['comment'])
        rating.save()
        ratings = Rating.objects.filter(reviewed_user_id=request.POST['reviewedid'])
        lister = User.objects.get(id=request.POST['reviewedid'])
        raters = []
        for rating in ratings:
            rater = User.objects.get(id=rating.user_id)
            raters.append(rater.email)
        return render(request, 'rating/rating_list.html',
                          {'ratings': ratings,
                           'raters': raters,
                           'lister': lister,
                           'current': current,
                           'success': 'You have successfully updated your review!'})


@login_required(login_url="/signup/")
def my_review(request, pk):
	rating = Rating.objects.filter(reviewed_user_id=pk, user_id=request.user.id)
	lister = User.objects.get(id=pk)
	print(rating[0].rating)
	return render(request, 'rating/rating_detail.html', {'rating': rating[0], 'lister': lister})
	
	
@login_required(login_url="/signup/")
def delete_review(request, rating_id, reviewed_user_id):
	Rating.objects.filter(id=rating_id).delete()
	
	return redirect('subby:RatingList', user_id=reviewed_user_id)
	