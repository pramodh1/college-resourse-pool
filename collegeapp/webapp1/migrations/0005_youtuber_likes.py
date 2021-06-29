# Generated by Django 3.0.7 on 2020-12-29 15:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp1', '0004_remove_youtuber_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]