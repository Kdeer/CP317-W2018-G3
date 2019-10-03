from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from .views import application, user, sublet, account, rating, favourite, report

app_name = 'subby'

urlpatterns = [

    # Base application view
    path('', application.index, name='index'),

    # User Admin views
    path('users/', user.index, name='user_index'),
    path('users/<int:user_id>', user.show, name='user_show'),
    path('users/<int:user_id>/sublets', user.sublets, name='user_sublets'),
    path('users/<int:user_id>/lock_account', user.lock_account, name='user_lock_account'),

    # User session views
    path('login/', user.login, name='login'),
    path('logout/', user.logout, name='logout'),
    path('signup/', user.signup, name='signup'),
    # url(r'^auth/', include('social_django.urls', namespace='social')),


    # Account Paths
    path('account/', account.account_home, name='account_home'),
    path('account/update', account.update_user_info, name='update_user_info'),

    # Sublet paths
    path('sublets/', sublet.SubletList.as_view(template_name='sublet/sublet_list.html'), name='SubletList'),
    path('sublets/<int:pk>/', sublet.SubletDetail.as_view(template_name='sublet/sublet_detail.html'), name='SubletDetail'),
    path('sublets/create_sublet', sublet.create_sublet, name='create_sublet'),
    path('sublets/search', sublet.search, name='search'),
    path('sublets/contact', user.contact_user, name='contact_user'),
    path('sublets/update_sublet', sublet.update_sublet, name='update_sublet'),
    path('sublets/my_sublets', sublet.my_sublets, name='my_sublets'),
    path('sublets/my_sublets/delete_sublet/<int:sublet_id>', sublet.delete_sublet, name='delete_sublet'),

    # Rating paths

    path('ratings/<int:user_id>', rating.list_user_rating, name='RatingList'),
    path('ratings/write_review/', rating.write_review, name='write_review'),
    path('ratings/update_review/', rating.update_review, name='update_review'),
    path('ratings/reviews/<int:pk>/', rating.my_review, name='my_review'),
    path('ratings/delete/<int:rating_id>/<int:reviewed_user_id>/', rating.delete_review, name='delete_review'),

    # Favourite paths
    path('favourites/', favourite.FavouriteLister, name='favourite_list'),
    path('favourites/fav_unfav_sublet/', favourite.fav_unfav_sublet, name='fav_unfav_sublet'),
    path('favourites/unfav_sublet/<int:fav_id>', favourite.unfav_sublet, name='unfav_sublet'),

    # Report paths
    path('report/<int:user_id>/<int:sublet_id>/', report.create_report, name='create_report'),
    path('report_list/', report.report_list, name='report_list'),
    path('search_report/', report.search_report, name='search_report'),

]
