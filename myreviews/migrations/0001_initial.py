# Generated by Django 3.2.4 on 2021-07-06 10:44

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('body', tinymce.models.HTMLField()),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
