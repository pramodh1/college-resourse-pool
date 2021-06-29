from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class youtuber(models.Model):
    name=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='media/youtubers/%Y/')
    vediourl=models.CharField(max_length=255)
    description=RichTextField()
    topic=models.CharField(max_length=255)
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    important=models.BooleanField(default=False)
    createddate=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.name


