# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-06 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasocioscap', '0013_auto_20201006_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuota',
            name='socio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistemasocioscap.Socio'),
        ),
        migrations.AlterField(
            model_name='anio',
            name='monto_cuota',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cuota',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
