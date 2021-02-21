# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2021-02-17 18:24
from __future__ import unicode_literals

import ProjectsApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='avtar',
            field=models.ImageField(upload_to=ProjectsApp.models.get_filepath_with_name),
        ),
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
