# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-15 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0012_photo_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='daechul',
            field=models.CharField(blank=True, max_length=10, verbose_name='전세자금대출'),
        ),
    ]
