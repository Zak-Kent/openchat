# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openspaces', '0002_auto_20170503_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='should_ignore',
            field=models.BooleanField(default=False),
        ),
    ]
