from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import gettext_lazy as _




# UserAdmin.fieldsets[2][1]['fields'] =  (
#                             "is_active",
#                             "is_staff",
#                             "is_superuser",
#                             'is_author',
#                             'is_special',
#                             "groups",
#                             "user_permissions",
#                         ),

# UserAdmin.list_display +=('is_author','is_special_user',)

@admin.register(CustomUser)
class AdminCustomUser(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','is_author','is_staff','is_special_user']
