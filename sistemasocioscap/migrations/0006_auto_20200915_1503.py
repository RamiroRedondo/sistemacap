# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-15 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasocioscap', '0005_auto_20200915_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socio',
            name='registro',
        ),
        migrations.AddField(
            model_name='registropagos',
            name='socio',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistemasocioscap.Socio'),
        ),
    ]
