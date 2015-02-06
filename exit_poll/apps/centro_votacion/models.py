# -*- coding: utf-8 -*-
'''Modelo para el Registro de Centros Electorales'''
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from django.contrib.auth.models import User


class Centros(models.Model):
    '''Informacion del Candidato'''
    #Informacion Princial
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(verbose_name="Nombre del Centro Electoral", max_length=150)
    estado = models.ForeignKey(Estado)
    municipio = ChainedForeignKey(Municipio, chained_field="estado", chained_model_field="estado", show_all=False,
                                  auto_choose=True, null=True)
    parroquia = ChainedForeignKey(Parroquia, chained_field="municipio", chained_model_field="municipio", show_all=False,
                                  auto_choose=True, null=True)
    direccion = models.CharField(max_length=150)
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        unique_together = ("codigo", "nombre", "estado", "municipio", "parroquia")
        ordering = ('codigo', 'nombre', 'estado', 'municipio', 'parroquia')

    def __unicode__(self):
        #return: Representacion en cadena de la clase Partidos
        return self.nombre

    def get_absolute_url(self):
        return ('listar_centro', [self.id, ])
