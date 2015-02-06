# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0002_auto_20150129_1844'),
        ('parroquias', '0002_auto_20150130_1504'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('municipios', '0002_auto_20150128_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=150, verbose_name=b'Nombre del Centro Electoral')),
                ('direccion', models.CharField(max_length=150)),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.ForeignKey(to='estados.Estado')),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='municipios.Municipio', chained_model_field=b'estado', chained_field=b'estado', null=True)),
                ('parroquia', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='parroquias.Parroquia', chained_model_field=b'municipio', chained_field=b'municipio', null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('codigo', 'nombre', 'estado', 'municipio', 'parroquia'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='centros',
            unique_together=set([('codigo', 'nombre', 'estado', 'municipio', 'parroquia')]),
        ),
    ]
