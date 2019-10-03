from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User
from .models.rating import Rating
from .models.sublet import Sublet
from .models.favourite import Favourite
from .models.report import Report

admin.site.register(User)

class UserAdmin(DjangoUserAdmin):
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal info', {'fields': ('first_name', 'last_name')}),
    ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions')}),
    ('Important dates', {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2'),
    }),
  )
  list_display = ('email', 'first_name', 'last_name', 'is_admin')
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email')

class SubletData(admin.ModelAdmin):
	list_display = ('title', 'street_address', 'created_at', 'updated_at')
admin.site.register(Sublet, SubletData)


class RatingData(admin.ModelAdmin):
	list_display = ('pk', 'rating')
	
admin.site.register(Rating, RatingData)

admin.site.register(Favourite)
admin.site.register(Report)

