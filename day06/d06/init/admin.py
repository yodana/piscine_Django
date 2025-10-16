from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'has_permission', 'is_active', 'can_downvote')
    fieldsets =  UserAdmin.fieldsets + (
        ('Permissions personnalisées', {'fields': ('has_permission','can_downvote')}),
    )