# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-15 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasocioscap', '0004_auto_20200915_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registropagos',
            name='socio',
        ),
        migrations.AddField(
            model_name='socio',
            name='registro',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistemasocioscap.RegistroPagos'),
        ),
    ]
