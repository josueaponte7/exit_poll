from rest_framework import serializers
from .models import Tipo_eleccion


class Tipo_eleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_eleccion
        fields = fields = ('id', 'categoria', 'tipo', 'user_create', 'user_update', 'fecha_create', 'fecha_update',)
