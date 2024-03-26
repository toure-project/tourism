from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    F_name= models.CharField(max_length=30)
    L_name= models.CharField(max_length=30)
    Email= models.EmailField(max_length=30)
    Address= models.CharField(max_length=30)  
    Phone= models.IntegerField()

def __str__(self):
    return self.H_Name
