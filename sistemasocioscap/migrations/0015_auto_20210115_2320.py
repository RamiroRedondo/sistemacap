# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-15 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasocioscap', '0014_auto_20201006_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='socio',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='socio',
            name='cobrador',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistemasocioscap.Cobrador'),
        ),
    ]