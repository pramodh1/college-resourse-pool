# Generated by Django 3.0.7 on 2020-12-29 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0003_auto_20201229_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtuber',
            name='chapter',
        ),
    ]
