# Generated by Django 3.0.7 on 2020-12-30 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='postsub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
    ]