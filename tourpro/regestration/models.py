from django.contrib.auth.models import User
from django.db import models

class Managers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    ROLE_CHOICES = (
        ('Hotel Manager', 'Hotel Manager'),
        ('Transport Manager', 'Transport Manager'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

