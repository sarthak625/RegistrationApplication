# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-14 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='description',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]