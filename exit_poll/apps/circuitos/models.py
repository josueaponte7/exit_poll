from django.db import models
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from django.contrib.auth.models import User


class Circuito(models.Model):
    estado = models.ForeignKey(Estado)
    #Informacion Princial
    n_circuito = models.CharField(max_length=2, verbose_name="Numero del circuito",)
    municipio = models.ManyToManyField(Municipio, related_name="+")
    num_max_candidatos = models.IntegerField(verbose_name="Numero maximo de candidatos")
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __unicode__(self):
        #return: Representacion en cadena de la clase Estado
        return self.n_circuito

    def get_absolute_url(self):
        return ('listar_circuito', [self.id, ])
