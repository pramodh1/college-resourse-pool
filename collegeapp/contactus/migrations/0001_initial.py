# Generated by Django 3.0.7 on 2020-12-18 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=255)),
                ('currentdate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
