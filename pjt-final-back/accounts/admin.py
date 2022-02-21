from django.contrib import admin
# from django.conf import settings


from .models import User
from django.contrib.auth.admin import UserAdmin
admin.site.register(User, UserAdmin)


# admin.site.register(settings.AUTH_USER_MODEL)
