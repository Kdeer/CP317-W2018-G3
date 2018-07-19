from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Func, F
from subby.models.sublet import Sublet
from django.shortcuts import get_object_or_404
from subby.models.image import Image

import json

class SubletList(ListView):
	model = Sublet
	paginate_by = 10
	# product = get_object_or_404(Sublet, pk=1)
	# product.delete()
	
	
	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		print(ctx["sublet_list"])
		print(123)
		return ctx
	
	
	
	
class SubletDetail(DetailView):
	model = Sublet
	
# temp redir
def search(request):
	if request.method == 'POST':
		if request.POST['lat'] and request.POST['lng'] and request.POST['proximity']:
			places = Sublet.objects.nearby(request.POST['lat'], request.POST['lng'], request.POST['proximity'])
			return render(request, 'sublet/search_sublets.html',
						  {'place': places, 'lat' : request.POST['lat'],
						   'lng': request.POST['lng'],
						   'prox' : request.POST['proximity']})
		else:
			places = Sublet.objects.nearby( 43.471111, -80.545372, 20)
			return render(request, 'sublet/search_sublets.html', {'place' : places, 'lat' : 43.471111, 'lng' : -80.545372})
	else:
		return render(request, 'application/base.html')


	
@login_required(login_url="/signup/")
def create_sublet(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['street_address'] and request.POST['city'] and request.POST['postal_code'] and request.POST['price'] and request.POST['description'] and request.POST['lat'] and request.POST['lng'] and request.FILES.getlist('files'):
			sublet = Sublet()
			sublet.title = request.POST['title']
			sublet.street_address = request.POST['street_address']
			sublet.city = request.POST['city']
			sublet.postal_code = request.POST['postal_code']
			sublet.price = request.POST['price']
			sublet.description = request.POST['description']
			"""for file in request.FILES.getlist('files'):
				instance = Image(
					sublet=Sublet.objects.get(1),
					image=file
				)
				instance.save()
			"""
			sublet.front_image = request.FILES.getlist('files')[0]
			sublet.latitude = request.POST['lat']
			sublet.longitude = request.POST['lng']
			#sublet.user_id = request.user.id
			sublet.user = request.user
			sublet.save()
			return render(request, 'sublet/create_sublet.html', {'success': 'true'})
		else:
			return render(request, 'sublet/create_sublet.html', {'create_sublet_error': 'All fields are required' })
	else:
		return render(request, 'sublet/create_sublet.html')

		


	
	