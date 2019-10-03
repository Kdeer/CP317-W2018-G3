from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime, pytz

from ..managers import UserManager

# Extend Django's user model so we can enforce our own auth policies
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length = 80, blank = True, null = True)
    last_name = models.CharField(max_length = 80, blank = True, null = True)
    phone_number = models.CharField(max_length = 31, null = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    username = models.CharField(max_length=20,blank=False,null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "{} - admin: {}".format(self.email, self.is_admin)

    def email_user(self, subject, message, from_email = None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
    # Required method based on Django assumptions
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    # Required method based on Django assumptions
    def get_short_name(self):
        return self.first_name

    # Required for Django; we aren't using this functionality, so return False
    def is_staff(self):
        return False

    # Required for extending Django's user model
    class Meta:
        app_label = 'subby'
        verbose_name = 'user'
        verbose_name_plural = 'users'
		
    def set_username(self, username):
       self.username = username
       return

# Object Lifecycle Callbacks
@receiver(pre_save, sender=User)
def pre_save(sender, **kwargs):
    sender.updated_at = pytz.utc.localize(datetime.datetime.now())
	