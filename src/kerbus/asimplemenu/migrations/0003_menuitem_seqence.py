# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asimplemenu', '0002_auto_20170227_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='seqence',
            field=models.IntegerField(default=0),
        ),
    ]
