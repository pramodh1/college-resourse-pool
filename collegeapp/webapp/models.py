from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class team(models.Model):
    platform=models.CharField(max_length=255)
    conceptname=models.CharField(max_length=255)
    conceptlink=models.CharField(max_length=255)
    
   
    photo=models.ImageField(upload_to='media/team/%Y/')
    currentdate=models.DateField( auto_now_add=True)
    def __str__(self):
        return self.platform

    



class slide(models.Model):
    hline=models.CharField(max_length=255)
    subline=models.CharField(max_length=255)
    buttontxt=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='media/slider/%Y/')
    link = models.URLField(max_length = 200 )
    created_date=models.DateTimeField(auto_now_add=True)