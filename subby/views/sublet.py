from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from subby.models.sublet import Sublet, SubletImage
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db import connection


class SubletList(ListView):
	model = Sublet
	paginate_by = 10
	
	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		images = SubletImage.objects.all()
		image_list = []
		sublet_id_list = []
		for image in images:
			# element<> = <image.sublet.id, image.image>
			image_list.append(image)
			if image.sublet.id not in sublet_id_list:
				sublet_id_list.append(image.sublet.id)
		
		n = 1
		while n < len(image_list):
			if image_list[n].sublet.id == image_list[n-1].sublet.id:
				image_list.pop(n)
			else:
				n += 1
		

		print(image_list)
		# print(images)
		# print(self.object_list)
		ctx['image_list'] = image_list
		ctx['sublet_id_list'] = sublet_id_list
		return ctx
	
	
	
	
class SubletDetail(DetailView):
	model = Sublet
	
	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		images = SubletImage.objects.filter(sublet=self.object)
		if len(images) > 0:
			cover_image = images[0].image
			ctx['cover_image'] = cover_image
			rest_images = []
			for n in range(1, len(images)):
				rest_images.append(images[n].image)
			ctx['rest_images'] = rest_images
		return ctx
		
	
	
@login_required(login_url="/signup/")
def create_sublet(request):
	print(settings.STATIC_ROOT)
	if request.method == 'POST':
		if request.POST['title'] and request.POST['street_address'] and request.POST['city'] and request.POST['postal_code'] and request.POST['price'] and request.POST['description'] and request.POST['lat'] and request.POST['lng']:
			sublet = Sublet()
			sublet.title = request.POST['title']
			sublet.street_address = request.POST['street_address']
			sublet.city = request.POST['city']
			sublet.postal_code = request.POST['postal_code']
			sublet.price = request.POST['price']
			sublet.description = request.POST['description']
			sublet.latitude = request.POST['lat']
			sublet.longitude = request.POST['lng']
			sublet.user = request.user
			sublet.save()
			image_list = request.FILES.getlist('image')
			if len(image_list) > 0:
				for image in image_list:
					sublet_image = SubletImage(sublet=sublet)
					sublet_image.image = image
					sublet_image.save()

			return redirect('subby:index')
		else:
			sublet.delete()
			return render(request, 'sublet/create_sublet.html', {'error': 'All fields are required' })
	else:
		return render(request, 'sublet/create_sublet.html')
		


	
	