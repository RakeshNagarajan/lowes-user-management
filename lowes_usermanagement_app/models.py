from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

ROLES = (
      ('admin', 'admin'),
      ('normal_user', 'normal_user'),
) 

class user(AbstractUser):
    permission = models.CharField(max_length=200, choices=ROLES, default='normal_user')
    department = models.CharField(max_length=200)
    displayname = models.CharField(max_length=200)
    costcenter = models.CharField(max_length=200)