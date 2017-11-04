# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatPais',
            fields=[
                ('idPais', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('idDepartamento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(max_length=15)),
                ('extension', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institucionfinanciera',
            fields=[
                ('idInstitucionFinanciera', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('calle', models.CharField(max_length=100)),
                ('coloniaMunicipio', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=5)),
                ('numExterior', models.CharField(max_length=7)),
                ('numeroInterior', models.CharField(blank=True, max_length=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('idLocalidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('idServicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombrePlan', models.CharField(max_length=300)),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True)),
                ('idDepartamento', models.ManyToManyField(to='aseguradoras.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='CatEstados',
            fields=[
                ('idEstado', models.IntegerField()),
                ('idPais', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='aseguradoras.CatPais')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='institucionfinanciera',
            name='idLocalidad',
            field=models.ForeignKey(db_column='idlocalidad', on_delete=django.db.models.deletion.CASCADE, to='aseguradoras.Localidades'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='idInstitucionFinanciera',
            field=models.ManyToManyField(to='aseguradoras.Institucionfinanciera'),
        ),
        migrations.AddField(
            model_name='localidades',
            name='catEstadoEstado',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aseguradoras.CatEstados'),
        ),
    ]