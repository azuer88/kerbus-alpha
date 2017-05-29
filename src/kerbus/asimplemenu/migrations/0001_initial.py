# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 01:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80)),
                ('description', models.CharField(default='', max_length=80)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asimplemenu.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=80)),
                ('link', models.CharField(blank=True, default='', max_length=80)),
                ('sequence', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(related_name='items', to='asimplemenu.Group')),
                ('load', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submenu', to='asimplemenu.Group')),
            ],
            options={
                'ordering': ['sequence'],
            },
        ),
    ]
