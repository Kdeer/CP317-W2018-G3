from django.db import models
from django.conf import settings



######################
##Temporary sublet model for report prototype purpose
######################

class SubletManager(models.Manager):
	def get_cover_image(self):
		qs = self.get_queryset()
		print(qs)
		return qs


class Sublet(models.Model):
	
	latitude = models.FloatField()
	longitude = models.FloatField()

	street_address = models.CharField(max_length=250)
	postal_code = models.CharField(max_length=7)
	city = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(blank=True, null=True)
	description = models.TextField()
	title = models.CharField(max_length=50)
	price = models.FloatField()
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
	objects = SubletManager()
	
	
	def summary(self):
		if len(self.description) > 150:
			return self.description[:150] + "......"
		else:
			return self.description


class SubletImage(models.Model):
	sublet = models.ForeignKey(Sublet, related_name='sublet', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='image/')
	

	
	

		
		
		