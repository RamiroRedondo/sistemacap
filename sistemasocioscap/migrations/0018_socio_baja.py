# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-27 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasocioscap', '0017_auto_20210126_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='baja',
            field=models.CharField(blank=True, choices=[('si', 'Si'), ('no', 'No')], default='no', max_length=32, null=True),
        ),
    ]