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
    ]

    operations = [
        migrations.CreateModel(
            name='CatTipodireccion',
            fields=[
                ('idtipoDireccion', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=15)),
                ('telcasa', models.CharField(blank=True, max_length=15, null=True)),
                ('oficina', models.CharField(blank=True, max_length=15, null=True)),
                ('facebookid', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('iddireccion', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(blank=True, max_length=150, null=True)),
                ('colonia', models.CharField(blank=True, max_length=100, null=True)),
                ('delegacion', models.CharField(blank=True, max_length=100, null=True)),
                ('cp', models.CharField(blank=True, max_length=5, null=True)),
                ('numinterior', models.CharField(blank=True, max_length=7, null=True)),
                ('numexterior', models.CharField(blank=True, max_length=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('idEstadoCivil', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curp', models.CharField(blank=True, max_length=18, null=True)),
                ('rfc', models.CharField(blank=True, max_length=13, null=True)),
                ('fechaDeNacimiento', models.CharField(blank=True, max_length=10, null=True)),
                ('estadoCivil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.EstadoCivil')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('idRole', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='idRol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Roles'),
        ),
        migrations.AddField(
            model_name='persona',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='direccion',
            name='idpersona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direccion', to='login.Persona'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='idtipodireccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.CatTipodireccion'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='idpersona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacto', to='login.Persona'),
        ),
    ]
