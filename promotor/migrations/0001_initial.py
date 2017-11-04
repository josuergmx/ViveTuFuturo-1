# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 18:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0001_initial'),
        ('aseguradoras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='promotorAsesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAsesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Persona')),
                ('idPromotor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aseguradoras.Institucionfinanciera')),
            ],
        ),
    ]