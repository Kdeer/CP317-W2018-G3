from django.db import models
from django.conf import settings
from subby.managers.subletmanager import SubletManager
import datetime, pytz


class Sublet(models.Model):
	objects = SubletManager()

	title = models.CharField(max_length=50)
	description = models.TextField()
	price = models.FloatField()
	duration = models.IntegerField(default=4)
	is_sold = models.BooleanField(default=False)
	latitude = models.FloatField()
	longitude = models.FloatField()
	street_address = models.CharField(max_length=250)
	postal_code = models.CharField(max_length=7)
	city = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sublets', on_delete=models.CASCADE)

	def summary(self):
		if len(self.description) > 150:
			return self.description[:150] + "......"
		else:
			return self.description

	def __str__(self):
		return "{} - {} at ${}/mo".format(self.title, self.description, self.price)

	# Getters
	def get_sublet_id(self):
		return self.id
	def get_is_sold(self):
		return self.is_sold
	def get_sublet_title(self):
		return self.title
	def get_description(self):
		return self.description
	def get_duration(self):
		return self.duration
	def get_price(self):
		return self.price
	def get_lat(self):
		return self.latitude
	def get_lng(self):
		return self.longitude
	def get_street_address(self):
		return self.street_address
	def get_postal_code(self):
		return self.postal_code
	def get_city(self):
		return self.city
	def get_created_at(self):
		return self.created_at
	def get_updated_at(self):
		return self.updated_at

	# Setters
	def set_is_sold(self, status):
		self.is_sold = status
		return
	def set_sublet_title(self, title):
		self.title = title
		return
	def set_description(self, description):
		self.description = description
		return
	def set_duration(self, duration):
		self.duration = duration
		return
	def set_price(self, price):
		self.price = price
		return
	def set_lat(self, lat):
		self.latitude = lat
		return
	def set_lng(self, lng):
		self.longitude = lng
		return
	def set_street_address(self, street_address):
		self.street_address = street_address
		return
	def set_postal_code(self, postal_code):
		self.postal_code = postal_code
		return
	def set_city(self, city):
		self.city = city
		return
	def set_created_at(self, created_at):
		self.created_at = created_at
		return
	def set_updated_at(self):
		self.updated_at = pytz.utc.localize(datetime.datetime.now())
		return

		
	def pub_date_pretty(self):
		return self.created_at.strftime('%b %e, %Y')


