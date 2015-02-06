from rest_framework import serializers
from .models import Centros


class CentrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centros
        fields = ('id', 'codigo', 'nombre', 'estado', 'municipio', 'parroquia', 'direccion',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update',)
