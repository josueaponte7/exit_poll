from rest_framework import serializers
from .models import Eleccion


class EleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleccion
        fields = ('id', 'nombre', 'tipo_eleccion', 'tipo_candidatura', 'year_eleccion',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update',)
