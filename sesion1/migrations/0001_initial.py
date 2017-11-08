# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blindajefinanciero',
            fields=[
                ('idbl', models.AutoField(primary_key=True, serialize=False)),
                ('column', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Capitalizacion',
            fields=[
                ('idcapitalizacion', models.AutoField(primary_key=True, serialize=False)),
                ('column', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libertadfinanciera',
            fields=[
                ('idlf', models.AutoField(primary_key=True, serialize=False)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('montoObjetivo', models.IntegerField(blank=True, null=True)),
                ('anos', models.IntegerField(blank=True, null=True)),
                ('ahorro', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sesion1',
            fields=[
                ('idSesion', models.AutoField(primary_key=True, serialize=False)),
                ('videoPresentacion', models.CharField(blank=True, max_length=100, null=True)),
                ('cartaConfidencialidad', models.CharField(blank=True, max_length=100, null=True)),
                ('blindajeFinancieroidbl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sesion1.Blindajefinanciero')),
                ('idAsesorCliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cliente.AsesorCliente')),
                ('idCapitalizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sesion1.Capitalizacion')),
                ('libertadFinancieraiDlf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sesion1.Libertadfinanciera')),
            ],
        ),
    ]
