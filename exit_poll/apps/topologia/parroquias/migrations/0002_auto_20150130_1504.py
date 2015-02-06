# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parroquias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parroquia',
            options={},
        ),
        migrations.AlterField(
            model_name='parroquia',
            name='parroquia',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='parroquia',
            unique_together=set([]),
        ),
    ]
