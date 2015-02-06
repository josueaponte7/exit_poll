# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('elecciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExitPoll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('candidatos', models.ForeignKey(to='candidatos.Candidatos')),
                ('eleccion', models.ForeignKey(to='elecciones.Eleccion', null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
