from django.contrib import admin
from .models import *
from .models.sublet101 import Sublet101


admin.site.register(User)
admin.site.register(Sublet101)
