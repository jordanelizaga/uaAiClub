# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='desc',
            field=models.TextField(max_length=10000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='loc',
            field=models.CharField(max_length=1000, verbose_name='Location'),
        ),
    ]
