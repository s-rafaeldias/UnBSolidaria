# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-16 06:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgposlogin', '0012_andamento_realizados_solicitacao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Andamento',
        ),
        migrations.DeleteModel(
            name='Realizados',
        ),
        migrations.DeleteModel(
            name='Solicitacao',
        ),
    ]
