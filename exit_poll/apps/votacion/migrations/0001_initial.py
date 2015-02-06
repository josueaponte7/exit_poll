# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupo_etareo', '0001_initial'),
        ('candidatos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidatos', models.ForeignKey(to='candidatos.Candidatos')),
                ('grupo_etareo', models.ForeignKey(to='grupo_etareo.Grupo_Etareo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
