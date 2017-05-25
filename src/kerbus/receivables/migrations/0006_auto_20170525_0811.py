# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 08:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receivables', '0005_auto_20170525_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receivables_account_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receivables_account_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
