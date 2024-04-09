from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

class UploadedFile(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)
    # permission= models.IntegerField(choices=[(0,'No Permission'),(1,'Allow Permission')])

    def __str__(self):  
      return f"{self.owner.username}'s File: {self.file.name}"