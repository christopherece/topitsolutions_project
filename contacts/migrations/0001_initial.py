# Generated by Django 3.2.4 on 2021-06-14 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
