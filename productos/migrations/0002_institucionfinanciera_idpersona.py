# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucionfinanciera',
            name='idPersona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Persona'),
        ),
    ]
