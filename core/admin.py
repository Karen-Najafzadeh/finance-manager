from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as x
from .models import User

@admin.register(User)
class UserAdmin(x):
    pass