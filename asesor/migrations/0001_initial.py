# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('idAsesor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='login.Persona')),
                ('tipoLicencia', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReporteActividad',
            fields=[
                ('idReporte', models.AutoField(primary_key=True, serialize=False)),
                ('fechaReporte', models.DateField()),
                ('recomendadosObtenidos', models.IntegerField()),
                ('recomendadosContactados', models.IntegerField()),
                ('llamadasRealizadas', models.IntegerField()),
                ('citasObtenidas', models.IntegerField()),
                ('citasTotales', models.IntegerField()),
                ('citasNuevas', models.IntegerField()),
                ('entrevistasInicialesPlaneadas', models.IntegerField()),
                ('entrevistasInicialesRealizadas', models.IntegerField()),
                ('entrevistasCierrePlaneadas', models.IntegerField()),
                ('entrevistasCierreRealizadas', models.IntegerField()),
                ('solicitudesSucritas', models.IntegerField()),
                ('idAsesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asesor.Asesor')),
            ],
        ),
    ]
