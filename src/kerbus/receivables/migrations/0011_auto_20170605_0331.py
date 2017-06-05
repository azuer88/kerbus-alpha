# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-05 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receivables', '0010_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='person',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='receivables.Person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=4, default='0.00', max_digits=12),
        ),
        migrations.AddField(
            model_name='transaction',
            name='particulars',
            field=models.CharField(default='Payment', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='t_type',
            field=models.SmallIntegerField(choices=[(1, 'Credit'), (2, 'Debit')], default=2, verbose_name='Type'),
        ),
    ]