from django.contrib.auth.admin import UserAdmin
from .models import MyUser
from django.contrib import admin

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'password')
