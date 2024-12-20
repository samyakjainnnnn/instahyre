from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    is_spam = models.BooleanField(default=False)
