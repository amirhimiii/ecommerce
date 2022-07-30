from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserCreationForm, UserChangeForm



@admin.register(CustomUser)
class AdminCustomUser(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ['email','username',]
