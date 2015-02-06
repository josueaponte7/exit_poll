# -*- coding: utf-8 -*-
from django.db import models
from apps.candidatos.models import Candidatos
from apps.elecciones.models import Eleccion
from django.contrib.auth.models import User
#from smart_selects.db_fields import ChainedForeignKey


class ExitPoll(models.Model):
    '''Registro de Votos'''
    eleccion = models.ForeignKey(Eleccion, null=True)
    candidatos = models.ForeignKey(Candidatos)
  

   #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
