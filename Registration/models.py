from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class CustomUser(AbstractUser): #AbstractUser changed to model.Model
    # Additional fields
    usertype=models.CharField(max_length=50, null=True)
    username=models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    branch = models.CharField(max_length=100, blank=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    # Define any other fields you may need

    def __str__(self):
        return self.username
    
