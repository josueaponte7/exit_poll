#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Modelos Para tipos de Elecciones'''
from django.db import models
from django.core.urlresolvers import reverse
from apps.tipos.categoria_eleccion.models import Categoria
from django.contrib.auth.models import User

class Tipo_eleccion(models.Model):
    '''Informacion del Municipio'''
    #Informacion Principal
    categoria = models.ForeignKey(Categoria)  # Categoria Padre
    tipo = models.CharField(max_length=100, )  # Sub-tipo o sub-categoria
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        unique_together = ("categoria", "tipo")  # tipo unico por categoria seleccionada
        ordering = ('categoria', 'tipo')

    def __unicode__(self):
        #return: Representacion en cadena de la clase tipo
        return self.tipo

    def get_absolute_url(self):
        return ('listar_circuito', [self.id, ])
