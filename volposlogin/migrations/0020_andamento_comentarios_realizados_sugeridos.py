# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-16 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('volposlogin', '0019_auto_20161116_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Andamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizacao', models.CharField(max_length=100)),
                ('trabalho', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=4000, verbose_name='descricao')),
                ('image', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('comentario', models.TextField(max_length=4000, verbose_name='comentario')),
                ('image', models.CharField(max_length=400)),
                ('realizados', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Realizados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizacao', models.CharField(max_length=100)),
                ('trabalho', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=4000, verbose_name='descricao')),
                ('image', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Sugeridos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizacao', models.CharField(max_length=100)),
                ('trabalho', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=4000, verbose_name='descricao')),
                ('image', models.CharField(max_length=400)),
            ],
        ),
    ]
