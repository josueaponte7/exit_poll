# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categoria_eleccion', '0001_initial'),
        ('tipo_eleccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre del Proceso Electoral')),
                ('year_eleccion', models.DateField(verbose_name=b'A\xc3\xb1o')),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('categoria_eleccion', models.ForeignKey(to='categoria_eleccion.Categoria')),
                ('tipo_eleccion', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'categoria', chained_field=b'categoria_eleccion', auto_choose=True, to='tipo_eleccion.Tipo_eleccion')),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('year_eleccion', 'tipo_eleccion'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='eleccion',
            unique_together=set([('nombre', 'year_eleccion')]),
        ),
    ]
