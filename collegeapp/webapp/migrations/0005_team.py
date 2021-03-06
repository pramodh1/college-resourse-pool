# Generated by Django 3.0.7 on 2020-12-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_slide_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('flink', models.CharField(max_length=255)),
                ('ilink', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/team/%Y/')),
                ('currentdate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
