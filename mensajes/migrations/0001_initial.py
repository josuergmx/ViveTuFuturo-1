# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-20 18:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0009_recomendadocliente_edad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=240)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('tipo', models.IntegerField(blank=True, null=True)),
                ('leido', models.BooleanField(default=False)),
                ('asesorCliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.AsesorCliente')),
            ],
        ),
    ]