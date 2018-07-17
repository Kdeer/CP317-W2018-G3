from django.db import models
from datetime import datetime

class Sublet101(models.Model):
    # CITY = (
    # ('W', 'Waterloo'),
    # ('K', 'Kitchener'),
    # )
    # TERMS = (
    # ('1', '4 Months'),
    # ('2', '8 Months'),
    # ('3', '12 Months'),
    # )
    name = models.CharField(max_length=200)
    # description = models.TextField()
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    # updated_at = models.DateTimeField(default=datetime.now, blank=True)
    # is_available = models.BooleanField()
    # number_roomates = models.SmallIntegerField()
    # rent_date = models.DateField()
    # returned_date = models.DateField()
    # #price_per_month = models.DoubleField()
    # city = models.CharField(max_length=1, choices=CITY)
    # num_terms = models.CharField(max_length=1, choices=TERMS)
    # longitude = models.FloatField()
    # latitude = models.FloatField()
    # primary_pic = models.ImageField(null = True)
    #owner_id = models.ForeignKey(user.User, on_delete=models.CASCADE)
