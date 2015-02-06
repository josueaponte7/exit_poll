from django.db import models
from apps.topologia.estados.models import Estado 


class Municipio(models.Model):
    estado = models.ForeignKey(Estado)
    municipio = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        #return: Representacion en cadena de la clase Estado
        return self.municipio

    class Meta:
        unique_together = ("estado", "municipio")  # Municipio unico por Estado seleccionado
        ordering = ('estado', 'municipio')  # Ordenado por

    def get_absolute_url(self):
        return ('listar_municipio', [self.id, ])
