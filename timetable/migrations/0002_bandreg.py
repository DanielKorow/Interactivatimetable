# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BandReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
