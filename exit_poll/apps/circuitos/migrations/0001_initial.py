# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('municipios', '0001_initial'),
        ('estados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('n_circuito', models.CharField(max_length=2, verbose_name=b'Numero del circuito')),
                ('num_max_candidatos', models.IntegerField(verbose_name=b'Numero maximo de candidatos')),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.ForeignKey(to='estados.Estado')),
                ('municipio', models.ManyToManyField(related_name='+', to='municipios.Municipio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
