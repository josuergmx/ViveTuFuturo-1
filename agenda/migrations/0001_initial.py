# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asesor', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatEstatuscita',
            fields=[
                ('idEstatus', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatTipocita',
            fields=[
                ('idTipoCita', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('idCita', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('direccionCita', models.CharField(blank=True, max_length=200, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('idAsesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asesor.Asesor')),
                ('idAsesorCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.AsesorCliente')),
                ('idEstatus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agenda.CatEstatuscita')),
                ('idTipoCita', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agenda.CatTipocita')),
            ],
        ),
    ]
