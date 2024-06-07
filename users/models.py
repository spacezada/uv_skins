from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
   

    def __str__(self):
        return self.name