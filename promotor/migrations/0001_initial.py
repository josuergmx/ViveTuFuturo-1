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
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='promotorAsesor',
            fields=[
                ('idAsesorPromotor', models.AutoField(primary_key=True, serialize=False)),
                ('activo', models.NullBooleanField()),
                ('idAsesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Persona')),
                ('idPromotor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.InstitucionFinanciera')),
            ],
        ),
    ]
