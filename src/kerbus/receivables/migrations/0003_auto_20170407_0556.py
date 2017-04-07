# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 05:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receivables', '0002_person_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('last_name', 'first_name', 'middle_name')},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='midde_name',
            new_name='middle_name',
        ),
    ]