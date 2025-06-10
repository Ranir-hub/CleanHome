from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import SignUpForm
from accounts.models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    model = CustomUser
    list_display = ['username', 'email', 'phone', 'is_superuser', 'is_staff', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)
