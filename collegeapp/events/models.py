from django.db import models

# Create your models here.
class event1(models.Model):
    topic=models.CharField(max_length=255)
    platform=models.CharField(max_length=255)
    start_date_time=models.CharField(max_length=255)
    end_date_time=models.CharField(max_length=255)
    link=models.CharField(max_length=255)    