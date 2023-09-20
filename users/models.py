from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    organisation = models.CharField(max_length=100,blank=False,null=False)
    REQUIRED_FIELDS=['organisation']

    def __str__(self):
        return self.username