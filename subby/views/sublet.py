from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from subby.decorators.loginrequiredmessage import message_login_required
from subby.models.favourite import Favourite
from subby.models.image import SubletImage
from subby.models.sublet import Sublet


User = get_user_model()


class SubletList(ListView):
    model = Sublet
    paginate_by = 10

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        images = SubletImage.objects.all()
        image_list = []
        sublet_id_list = []
        for image in images:
            image_list.append(image)
            if image.sublet.id not in sublet_id_list:
                sublet_id_list.append(image.sublet.id)

        n = 1
        while n < len(image_list):
            if image_list[n].sublet.id == image_list[n - 1].sublet.id:
                image_list.pop(n)
            else:
                n += 1

        ctx['image_list'] = image_list
        ctx['sublet_id_list'] = sublet_id_list
        return ctx


class SubletDetail(DetailView):
    model = Sublet

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        lister = User.objects.get(id=self.object.user_id)
        fav = False
        if self.request.user.is_authenticated:
            fav = Favourite.objects.filter(sublet=self.object, user=self.request.user)
            if len(fav) > 0:
                fav = True
            else:
                fav = False
        user = self.request.user.id
        ctx['fav'] = fav
        ctx['lister'] = lister
        ctx['cur_user'] = user
        images = SubletImage.objects.filter(sublet=self.object)
        if len(images) > 0:
            cover_image = images[0].image
            ctx['cover_image'] = cover_image
            rest_images = []
            for n in range(len(images)):
                rest_images.append(images[n].image)
            ctx['rest_images'] = rest_images
        return ctx


def search(request):
    if request.method == 'POST':
        if request.POST['lat'] and request.POST['lng'] and request.POST['proximity']:
            places = Sublet.objects.nearby(request.POST['lat'], request.POST['lng'], request.POST['proximity'])

            data = {'place': places, 'lat': request.POST['lat'],
                    'lng': request.POST['lng'],
                    'prox': request.POST['proximity']}
                    #'address':request.POST['search_address']}
            if request.POST.get('duration'):
                places = places.filter(duration=request.POST.get('duration'))
                data.update(place=places)
                data['duration'] = request.POST.get('duration')
            if request.POST.get('price'):
                places = places.filter(price__lte=float(request.POST.get('price')))
                data.update(place=places)
                data['price'] = request.POST.get('price')
            images = []
            for p in places:
                image = SubletImage.objects.filter(sublet=p.id)
                images.append(image[0].image.url)
            data.update(cover=images)
            return render(request, 'sublet/search_sublets.html', data)
        else:
            places = Sublet.objects.nearby(43.471111, -80.545372, 20)
            images = []
            for p in places:
                image = SubletImage.objects.filter(sublet=p.id)
                images.append(image[0].image.url)
            return render(request, 'sublet/search_sublets.html',
                          {'place': places, 'cover': images, 'lat': 43.471111, 'lng': -80.545372, 'prox': 20})
    else:
        return render(request, 'application/base.html')


@message_login_required
def create_sublet(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['street_address'] and request.POST['city'] and request.POST[
            'postal_code'] and request.POST['price'] and request.POST['description'] and request.POST['lat'] and \
                request.POST['lng'] and request.FILES.getlist('files'):
            city = request.POST['city']
            if city not in ['Kitchener', 'Waterloo', 'kitchener', 'waterloo']:
                return render(request, 'sublet/create_sublet.html',
                              {'create_sublet_error': 'City can only be Kitchener or Waterloo'})
            sublet = Sublet.objects.create_sublet(request.POST['title'],
                                                  request.POST['duration'],
                                                  request.POST['price'],
                                                  request.POST['street_address'],
                                                  request.POST['city'],
                                                  request.POST['postal_code'],
                                                  request.POST['description'],
                                                  request.POST['lat'],
                                                  request.POST['lng'],
                                                  request.user)

            image_list = request.FILES.getlist('files')
            if len(image_list) > 0:
                for image in image_list:
                    sublet_image = SubletImage(sublet=sublet)
                    sublet_image.image = image
                    sublet_image.save()
            messages.add_message(request, messages.INFO, 'You have successfully created your listing.')
            return redirect('subby:SubletDetail', sublet.get_sublet_id())
        else:
            return render(request, 'sublet/create_sublet.html', {'create_sublet_error': 'All fields are required'})
    else:
        return render(request, 'sublet/create_sublet.html')


def update_sublet(request):
    if request.method == 'POST':
        sublet = Sublet.objects.get(id=request.POST['subletid'])
        if request.POST['title'] != sublet.get_sublet_title():
            sublet.set_sublet_title(request.POST['title'])
            sublet.set_updated_at()
        if request.POST['duration'] != sublet.get_duration():
            sublet.set_duration(request.POST['duration'])
            sublet.set_updated_at()
        if request.POST['is-sold'] == 'Not Sold' and sublet.get_is_sold():
            sublet.set_is_sold(False)
            sublet.set_updated_at()
        if request.POST['is-sold'] == 'Sold' and not sublet.get_is_sold():
            sublet.set_is_sold(True)
            sublet.set_updated_at()
        if request.POST['street_address'] != sublet.get_street_address():
            sublet.set_street_address(request.POST['street_address'])
        if request.POST['city'] != sublet.get_city():
            sublet.set_city(request.POST['city'])
            sublet.set_updated_at()
        if request.POST['postal_code'] != sublet.get_postal_code():
            sublet.set_postal_code(request.POST['postal_code'])
            sublet.set_updated_at()
        if request.POST['price'] != sublet.get_price():
            sublet.set_price(request.POST['price'])
            sublet.set_updated_at()
        if request.POST['description'] != sublet.get_description():
            sublet.set_description(request.POST['description'])
            sublet.set_updated_at()
        if request.POST['lat'] != sublet.get_lat():
            sublet.set_lat(request.POST['lat'])
            sublet.set_updated_at()
        if request.POST['lng'] != sublet.get_lng():
            sublet.set_lng(request.POST['lng'])
            sublet.set_updated_at()
        if request.FILES.getlist('files'):
            image_list = request.FILES.getlist('files')
            sublet.set_updated_at()
            if len(image_list) > 0:
                for image in image_list:
                    sublet_image = SubletImage(sublet=sublet)
                    sublet_image.image = image
                    sublet_image.save()
        sublet.save()
        messages.add_message(request, messages.INFO, 'You have successfully updated your listing.')
        return redirect('subby:SubletDetail', sublet.get_sublet_id())
    else:
        messages.add_message(request, messages.INFO, 'Something went wrong!')
        return redirect('subby:SubletDetail', request.POST['subletid'])


@message_login_required
def my_sublets(request):
    my_postings = Sublet.objects.filter(user=request.user)
    print(my_postings)
    image_dict = {}
    image_list = []
    for post in my_postings:
        print(post.id)
        images = SubletImage.objects.filter(sublet=post)
        image_dict = images[0]
        image_list.append(images[0])
    posting_dict = {
        'my_postings': my_postings,
        'image_dict': image_dict,
        'image_list': image_list,
    }
    return render(request, 'sublet/my_sublets.html', posting_dict)

@message_login_required
def delete_sublet(request, sublet_id):
	title = Sublet.objects.get(id=sublet_id).title
	Sublet.objects.delete_sublet(sublet_id)

	messages.add_message(request, messages.INFO, "Sublet \""+title+'\" is deleted')
	return redirect('subby:my_sublets')
