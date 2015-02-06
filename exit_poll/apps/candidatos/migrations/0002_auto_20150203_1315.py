# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatos',
            name='eleccion',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='elecciones.Eleccion', chained_model_field=b'tipo_eleccion', chained_field=b'tipo_candidatura', null=True),
            preserve_default=True,
        ),
    ]
