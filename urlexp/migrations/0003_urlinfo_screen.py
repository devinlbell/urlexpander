# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlexp', '0002_auto_20160812_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlinfo',
            name='screen',
            field=models.CharField(default='https://s3.amazonaws.com/laburlexpander/yolo', max_length=500),
            preserve_default=False,
        ),
    ]
