from django.db import models


class Estado(models.Model):
    estado = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('estado',)  # Ordenado por

    def __unicode__(self):
        #return: Representacion en cadena de la clase Estado
        return self.estado

    def get_absolute_url(self):
        return ('listar_estado', [self.id, ])
