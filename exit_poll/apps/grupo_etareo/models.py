# -*- coding: utf-8 -*-
'''Modelo para el Registro de Grupos Etáreos'''
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Grupo_Etareo(models.Model):
    '''Informacion del grupo'''
    #Informacion Princial
    descripcion = models.CharField(max_length=20, verbose_name="Descripción", null=True) 
    grupo_etareo = models.CharField(max_length=6, verbose_name="Grupo Etáreo") 
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        ordering = ('grupo_etareo',)  # Ordenado por

    def __unicode__(self):
        #return: Representacion en cadena de la clase Grupos Etareos
        return self.descripcion

    def get_absolute_url(self):
        return ('listar_grupo_etareo', [self.id, ])
