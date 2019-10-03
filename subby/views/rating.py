from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse

from subby.decorators.loginrequiredmessage import message_login_required
from subby.models.rating import Rating

User = get_user_model()


def list_user_rating(request, user_id):
    ratings = Rating.objects.filter(reviewed_user_id=user_id)
    lister = User.objects.get(id=user_id)
    raters = []
    posted = False
    reviewed_user_id = user_id

    total_rating = 0
    total_count = len(ratings)
    print(total_count)
    for rating in ratings:
        rater = User.objects.get(id=rating.user_id)
        raters.append(rater.username)

        total_rating += rating.rating

    if request.user.is_anonymous:
        current = None
        current_id = None
    else:
        current = request.user.email
        current_id = request.user.id
        for rater in raters:
            if rater == request.user.username:
                posted = True

    
    if total_count != 0:
        avg = total_rating / total_count
        avg_detail = format(avg, '.2f')
        avg = round(avg * 2) / 2
    else:
        avg = 0
        avg_detail = 0
    rating_dict = {
        'ratings': ratings,
        'raters': raters,
        'lister': lister,
        'current': current,
        'avg_rating': avg,
        'avg_detail': avg_detail,
        'posted': posted,
        'current_id': current_id,
        'reviewed_user_id': reviewed_user_id
    }
    return render(request, 'rating/rating_list.html', rating_dict)


@message_login_required
def write_review(request):
    if request.method == 'POST':
        current = request.user.email
        if request.POST['rating'] and request.POST['comment']:
            Rating.objects.create_rating(float(request.POST['rating']), request.POST['comment'], request.user.id,
                                         request.POST['reviewedid'])
            messages.add_message(request, messages.SUCCESS, "You have successfully left your review!")
            return redirect('subby:RatingList', request.POST['reviewedid'])
        else:
            messages.add_message(request, messages.ERROR, "All fields must be filled in to write a review")
            return redirect('subby:RatingList', request.POST['reviewedid'])


@message_login_required
def update_review(request):
    if request.method == 'POST':
        rating = Rating.objects.get(id=request.POST['ratingid'])
        if request.POST.get('rating'):
            if float(request.POST['rating']) != rating.rating:
                rating.set_rating(float(request.POST['rating']))
                rating.set_updated_at()
            if request.POST['comment'] != rating.comment:
                rating.set_comment(request.POST['comment'])
            rating.save()
            messages.add_message(request, messages.SUCCESS, "You have successfully updated your review!")
            return redirect(reverse('subby:RatingList', kwargs={'user_id': rating.reviewed_user_id}))
        else:
            messages.add_message(request, messages.ERROR, "Rating must be updated to edit review.")
            return redirect(reverse('subby:RatingList', kwargs={'user_id': rating.reviewed_user_id}))


@message_login_required
def my_review(request, pk):
    rating = Rating.objects.filter(reviewed_user_id=pk, user_id=request.user.id)
    print(rating[0].rating)
    return render(request, 'rating/rating_detail.html', {'rating': rating[0], 'lister': request.user})


@message_login_required
def delete_review(request, rating_id, reviewed_user_id):
    Rating.objects.filter(id=rating_id).delete()

    return redirect('subby:RatingList', user_id=reviewed_user_id)
