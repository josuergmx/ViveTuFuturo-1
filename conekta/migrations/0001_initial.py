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
            name='Creditos',
            fields=[
                ('idCredito', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Estatuscredito',
            fields=[
                ('idestatuscredito', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='creditos',
            name='estatusCredito',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='conekta.Estatuscredito'),
        ),
        migrations.AddField(
            model_name='creditos',
            name='idAsesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asesor.Asesor'),
        ),
        migrations.AddField(
            model_name='creditos',
            name='idCliente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.AsesorCliente'),
        ),
    ]
