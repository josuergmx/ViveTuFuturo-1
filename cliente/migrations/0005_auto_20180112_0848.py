# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-12 08:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20171126_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asesorcliente',
            name='link',
        ),
        migrations.RemoveField(
            model_name='asesorcliente',
            name='password',
        ),
    ]