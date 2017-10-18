# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BulletinPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(verbose_name='Date Posted')),
                ('post_user', models.CharField(max_length=35, verbose_name='Name')),
                ('post_message', models.TextField(max_length=10000, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=50, verbose_name='Project Name')),
                ('pub_date', models.DateTimeField(verbose_name='Date Created')),
                ('project_desc', models.TextField(default='', max_length=10000, verbose_name='Project Description')),
            ],
        ),
        migrations.AddField(
            model_name='bulletinpost',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
