# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 16:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsesorCliente',
            fields=[
                ('idAsesorCliente', models.AutoField(primary_key=True, serialize=False)),
                ('clienteProspecto', models.BooleanField()),
                ('fechaActualizacion', models.DateField()),
                ('ocupacion', models.CharField(blank=True, max_length=150, null=True)),
                ('dependientes', models.CharField(blank=True, max_length=150, null=True)),
                ('ingresos', models.FloatField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=300, null=True)),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('activo', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('idEstatus', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrigenRecomendacion',
            fields=[
                ('idOrigen', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecomendadoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('celular', models.IntegerField(blank=True, null=True)),
                ('hijos', models.BooleanField()),
                ('asesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Persona')),
                ('estadoCivil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.EstadoCivil')),
            ],
        ),
        migrations.AddField(
            model_name='asesorcliente',
            name='Estatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Estatus'),
        ),
        migrations.AddField(
            model_name='asesorcliente',
            name='Origen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.OrigenRecomendacion'),
        ),
        migrations.AddField(
            model_name='asesorcliente',
            name='idAsesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asesorcliente',
            name='idCliente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.Persona'),
        ),
    ]
