# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20171013_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletinpost',
            name='post_message',
            field=models.TextField(max_length=10000, verbose_name='Message'),
        ),
    ]
