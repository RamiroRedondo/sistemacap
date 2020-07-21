# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-17 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasocioscap', '0002_auto_20200715_0431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('nrosocio', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('cbu', models.IntegerField(null=True)),
            ],
        ),
    ]
