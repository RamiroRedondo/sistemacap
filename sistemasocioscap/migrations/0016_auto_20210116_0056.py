# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-16 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasocioscap', '0015_auto_20210115_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='nrosocio',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]