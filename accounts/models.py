from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone





class CustomUser(AbstractUser):
    email = models.EmailField(null= False, blank=False ,max_length=254)
    is_author = models.BooleanField(default=False, verbose_name=_('author_status'))
    is_special = models.DateTimeField(default=timezone.now, verbose_name=_('special_user'))

    def is_special_user(self):
        if self.is_special > timezone.now() :
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description = _('special_user')
