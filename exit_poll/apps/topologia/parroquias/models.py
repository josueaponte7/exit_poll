#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Modelo Parroquia del país'''


from django.db import models
from smart_selects.db_fields import ChainedForeignKey 
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio


class Parroquia(models.Model):
    parroquia = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = ChainedForeignKey(Municipio, chained_field="estado", chained_model_field="estado",
                                  show_all=False, auto_choose=True)

    def __unicode__(self):
        #return: Representacion en cadena de la clase Estado
        return self.parroquia

    def get_absolute_url(self):
        return ('listar_parroquia', [self.id, ])
