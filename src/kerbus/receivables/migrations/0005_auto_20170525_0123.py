# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 01:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receivables', '0004_auto_20170407_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receivables_person_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receivables_person_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
