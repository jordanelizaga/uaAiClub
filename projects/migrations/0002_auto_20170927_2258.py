# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='project_desc',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date Created'),
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
