# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 04:11
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
            name='CatEstados',
            fields=[
                ('idEstado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CatPais',
            fields=[
                ('idPais', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('idDepartamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('extension', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitucionFinanciera',
            fields=[
                ('idInstitucion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('calle', models.CharField(blank=True, max_length=100, null=True)),
                ('colonia', models.CharField(blank=True, max_length=100, null=True)),
                ('cp', models.CharField(blank=True, max_length=5, null=True)),
                ('num_int', models.CharField(blank=True, max_length=7, null=True)),
                ('num_ext', models.CharField(blank=True, max_length=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('idLocalidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('CatEstados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.CatEstados')),
                ('CatPais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.CatPais')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idServicio', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=300)),
                ('nombre', models.CharField(max_length=300)),
                ('idDepartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Departamento')),
            ],
        ),
        migrations.AddField(
            model_name='institucionfinanciera',
            name='idLocalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Localidad'),
        ),
        migrations.AddField(
            model_name='institucionfinanciera',
            name='idPersona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Persona'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='idInstitucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.InstitucionFinanciera'),
        ),
        migrations.AddField(
            model_name='catestados',
            name='idPais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.CatPais'),
        ),
    ]
