from django.db import models
from django.conf import settings
from django.db.models.aggregates import Sum

class RatingManager(models.Manager):
    use_in_migrations = True

    def create_rating(self, rating_number, comment, user_id, reviewed_user_id):
        r = self.model()

        if not r.validate_rating(rating_number):
            raise ValueError('Rating is not valid rating number')

        r.set_rating(rating_number)
        r.set_comment(comment)
        r.set_user_id(user_id)
        r.set_reviewed_user_id(reviewed_user_id)
        r.save()
        return r
		
    def delete_rating(self):
       r = self.model()
       r.delete()
		
       return
		
	#####bad code
    # def get_avg_ratings(self):
      # qs = self.get_queryset()
      # qs = qs.annotate(score=Sum('rating'))
      # total_rating = 0
      # rating_count = 0
      # for rate in qs:
        # total_rating += rate.rating
        # rating_count += 1
      # if rating_count != 0:
        # avg_rate = total_rating / rating_count
      # else:
        # avg_rate = 0
      # print(avg_rate)
      # return avg_rate
