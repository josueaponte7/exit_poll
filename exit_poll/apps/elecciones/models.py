# -*- coding: utf-8 -*-
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.tipos.categoria_eleccion.models import Categoria
from apps.tipos.tipo_eleccion.models import Tipo_eleccion
import datetime
from django.contrib.auth.models import User


class Eleccion(models.Model):
    '''Informacion del proceso Electoral'''
    #Informacion Principal
    nombre = models.CharField(verbose_name="Nombre del Proceso Electoral", max_length=100)
    categoria_eleccion = models.ForeignKey(Categoria)

    tipo_eleccion = ChainedForeignKey(Tipo_eleccion, chained_field="categoria_eleccion", chained_model_field="categoria",
                                      show_all=False, auto_choose=True)
    year_eleccion = models.DateField(verbose_name='Año')

    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        unique_together = ("nombre", "year_eleccion")
        ordering = ('year_eleccion', 'tipo_eleccion')

    def __unicode__(self):
        #return: Representacion en cadena de la clase Partidos
        return self.nombre

    def get_absolute_url(self):
        return ('listar_circuito', [self.id, ])
