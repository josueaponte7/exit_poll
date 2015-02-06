# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votacion',
            name='candidatos',
            field=models.ForeignKey(to='candidatos.Candidatos'),
            preserve_default=True,
        ),
    ]
