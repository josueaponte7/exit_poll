# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0002_auto_20150129_1844'),
        ('municipios', '0002_auto_20150128_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parroquia', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(to='estados.Estado')),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'estado', chained_field=b'estado', auto_choose=True, to='municipios.Municipio')),
            ],
            options={
                'ordering': ('estado', 'municipio', 'parroquia'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='parroquia',
            unique_together=set([('estado', 'municipio', 'parroquia')]),
        ),
    ]
