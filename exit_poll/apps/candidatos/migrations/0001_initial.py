# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tipo_eleccion', '0001_initial'),
        ('estados', '0002_auto_20150129_1844'),
        ('elecciones', '0001_initial'),
        ('categoria_eleccion', '0001_initial'),
        ('municipios', '0002_auto_20150128_1900'),
        ('circuitos', '0002_auto_20150129_1331'),
        ('parroquias', '0002_auto_20150130_1504'),
        ('partidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre del Candidato')),
                ('apellido', models.CharField(max_length=100, verbose_name=b'Apellido del Candidato')),
                ('cedula', models.CharField(unique=True, max_length=8, verbose_name=b'C\xc3\xa9dula')),
                ('foto', models.ImageField(upload_to=b'')),
                ('sexo', models.CharField(default=0, max_length=15, choices=[(b'0', b'Femenino'), (b'1', b'Masculino')])),
                ('edad', models.IntegerField()),
                ('twitter', models.CharField(unique=True, max_length=200)),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('circuito', models.ForeignKey(to='circuitos.Circuito', null=True)),
                ('eleccion', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='elecciones.Eleccion', chained_model_field=b'tipo_eleccion', chained_field=b'tipo_candidatura', null=True)),
                ('estado', models.ForeignKey(to='estados.Estado', null=True)),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='municipios.Municipio', chained_model_field=b'estado', chained_field=b'estado', null=True)),
                ('parroquia', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='parroquias.Parroquia', chained_model_field=b'municipio', chained_field=b'municipio', null=True)),
                ('part_politico', models.ForeignKey(verbose_name=b'Partido Pol\xc3\xadtico', to='partidos.Partidos')),
                ('tipo_candidatura', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'categoria', chained_field=b'tipo_eleccion', auto_choose=True, to='tipo_eleccion.Tipo_eleccion')),
                ('tipo_eleccion', models.ForeignKey(verbose_name=b'Tipo de Elecci\xc3\xb3n', to='categoria_eleccion.Categoria')),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('nombre', 'apellido'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='candidatos',
            unique_together=set([('cedula', 'nombre', 'apellido')]),
        ),
    ]
