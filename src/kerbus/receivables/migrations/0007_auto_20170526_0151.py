# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-26 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receivables', '0006_auto_20170525_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='person',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
