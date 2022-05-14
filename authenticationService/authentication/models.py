from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    email = models.CharField(max_length=249, null=True, blank=True, unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email
