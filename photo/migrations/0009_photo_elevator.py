# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-15 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0008_auto_20181215_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='elevator',
            field=models.CharField(blank=True, max_length=10, verbose_name='엘레베이터'),
        ),
    ]