# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20170927_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletinpost',
            name='post_message',
            field=models.CharField(max_length=10000),
        ),
    ]