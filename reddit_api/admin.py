from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from reddit_api.models import *
# Register your models here.

admin.site.register(User, UserAdmin)