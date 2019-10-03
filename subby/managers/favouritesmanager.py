from django.db import models
from django.conf import settings

class FavouriteManager(models.Manager):

    def create_favourite(self, sublet, user):
        favourite = self.model()
        favourite.sublet = sublet
        favourite.user = user
        favourite.save()
        return favourite
    
    def remove_favourite(self, sublet, user):
        self.model.objects.filter(sublet=sublet, user=user).delete()
        return
        
    def remove_by_id(self, fav_id):
        favourite = self.model.objects.get(id=fav_id)
        favourite.delete()
        return
			
			
    def remove_favourite_list(self, user):
      self.model.objects.filter(user=uesr).delete()
      return 