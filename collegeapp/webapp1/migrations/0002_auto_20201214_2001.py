# Generated by Django 3.0.7 on 2020-12-14 14:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
