# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Partidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('n_partidos', models.CharField(unique=True, max_length=150, verbose_name=b'Nombre del Partido')),
                ('siglas', models.CharField(unique=True, max_length=10)),
                ('foto_partido', models.ImageField(upload_to=b'')),
                ('nom_presidente', models.CharField(unique=True, max_length=100, verbose_name=b'Nombre del Presidente')),
                ('ape_presidente', models.CharField(unique=True, max_length=100, verbose_name=b'Apellido del Presidente')),
                ('correo', models.EmailField(unique=True, max_length=200)),
                ('twitter', models.CharField(unique=True, max_length=200)),
                ('telefono', models.CharField(unique=True, max_length=11, verbose_name=b'Tel\xc3\xa9fono')),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('n_partidos', 'siglas'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='partidos',
            unique_together=set([('n_partidos', 'siglas')]),
        ),
    ]
