# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-14 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_auto_20181214_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='yogum',
        ),
        migrations.AddField(
            model_name='photo',
            name='bojunggum',
            field=models.TextField(blank=True, verbose_name='보증금/월세'),
        ),
    ]