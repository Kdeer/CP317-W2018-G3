from django.db import models
from django.conf import settings
from django.db.models.expressions import RawSQL
import datetime, pytz

class SubletManager(models.Manager):
	def get_cover_image(self):
		qs = self.get_queryset()
		print(qs)
		return qs

	def nearby(self, latitude, longitude, proximity):
		"""
        Return all object which distance to specified coordinates
        is less than proximity given in kilometers
        """
		# Great circle distance formula
		gcd = """
	          6371 * acos(
	           cos(radians(%s)) * cos(radians(latitude))
	           * cos(radians(longitude) - radians(%s)) +
	           sin(radians(%s)) * sin(radians(latitude))
	          )
	          """
		return self.get_queryset() \
			.exclude(latitude=None) \
			.exclude(longitude=None) \
			.annotate(distance=RawSQL(gcd, (latitude,
											longitude,
											latitude))) \
			.filter(distance__lt=proximity) \
			.order_by('distance')

	def create_sublet(self, sublet_title, duration, price, street_address, city, postal_code, description, lat, lng, user):
		sublet = self.model()
		sublet.set_sublet_title(sublet_title)
		sublet.set_duration(duration)
		sublet.set_price(price)
		sublet.set_street_address(street_address)
		sublet.set_city(city)
		sublet.set_postal_code(postal_code)
		sublet.set_description(description)
		sublet.set_lat(lat)
		sublet.set_lng(lng)
		sublet.user = user
		sublet.save()
		return sublet
		
	def delete_sublet(self, sublet_id):
		sublet = self.model.objects.get(id=sublet_id)
		sublet.delete()
		return
		