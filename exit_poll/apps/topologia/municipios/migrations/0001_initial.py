# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('municipio', models.CharField(unique=True, max_length=50)),
                ('estado', models.ForeignKey(to='estados.Estado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
