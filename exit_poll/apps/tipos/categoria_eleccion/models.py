#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Modelos Para Categorias de Elecciones'''
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Categoria(models.Model):
    '''Informacion de la Categoria'''
    #Informacion Principal
    categoria = models.CharField(max_length=50, unique=True)
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        ordering = ('categoria', )  # Ordenado por

    def __unicode__(self):
        #return: Representacion en cadena de la clase Categoria
        return self.categoria

    def get_absolute_url(self):
        return ('listar_circuito', [self.id, ])
