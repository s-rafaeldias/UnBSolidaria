# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-15 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('senha', models.CharField(default='', max_length=400)),
            ],
        ),
    ]
