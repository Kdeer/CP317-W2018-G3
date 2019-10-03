from django.db import models
from django.conf import settings
from subby.models.sublet import Sublet

class SubletImage(models.Model):
	sublet = models.ForeignKey(Sublet, related_name='sublet_image', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='image/')
