# -*- coding: utf-8 -*-
from django.db import models
from apps.exitpoll.models import ExitPoll
from apps.grupo_etareo.models import Grupo_Etareo
from apps.candidatos.models import Candidatos
from django.contrib.auth.models import User
#from smart_selects.db_fields import ChainedForeignKey


class Votacion(models.Model):
    '''Registro de Votos'''
    grupo_etareo  = models.ForeignKey(Grupo_Etareo)
    candidatos    = models.ForeignKey(Candidatos)
