from django.db import models
from django.conf import settings
from subby.managers.ratingmanager import RatingManager

import datetime, pytz
from . import User


ALLOWED_REVIEW_VALS = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

class Rating(models.Model):

    rating = models.FloatField()
    comment = models.CharField(max_length = 250, blank = True, null = True)
    user_id = models.PositiveIntegerField()
    reviewed_user_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    


    objects = RatingManager()

    def __str__(self):
        return "{} - {}".format(self.rating, self.comment)
    # Getters
    def get_rating(self):
        return self.rating
    def get_user_id(self):
        return self.user_id
    def get_reviewed_user_id(self):
        return self.reviewed_user_id
    def get_comment(self):
        return self.comment
    def get_created_at(self):
        return self.created_at
    def get_updated_at(self):
        return self.updated_at

    # Setters
    def set_rating(self, rating):
        self.rating = rating
        return

    def set_user_id(self, user_id):
        self.user_id = user_id
        return
    def set_reviewed_user_id(self, reviewed_user_id):
        self.reviewed_user_id = reviewed_user_id
        return
    def set_comment(self, comment):
        self.comment = comment
        return
    def set_created_at(self, created_at):
        self.created_at = created_at
        return
    def set_updated_at(self):
        self.updated_at = pytz.utc.localize(datetime.datetime.now())
        return

    # Helpers
    def validate_rating(self, rating):
        if rating in ALLOWED_REVIEW_VALS:
            return True
        else:
            return False
				
    class Meta:
       unique_together = ('user_id', 'reviewed_user_id')