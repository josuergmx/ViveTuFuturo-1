# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20171003_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='asesorcliente',
            name='activo',
            field=models.NullBooleanField(),
        ),
    ]
