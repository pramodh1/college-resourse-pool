# Generated by Django 3.0.7 on 2020-12-11 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='photo',
            field=models.ImageField(upload_to='slider/%Y/'),
        ),
    ]
