# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-17 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasocioscap', '0004_auto_20200717_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anual',
            name='anio',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cuota',
            name='nrocuota',
            field=models.CharField(max_length=200),
        ),
    ]
