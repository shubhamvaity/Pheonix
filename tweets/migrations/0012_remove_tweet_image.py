# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-04 18:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0011_auto_20180302_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='image',
        ),
    ]
