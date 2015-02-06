from rest_framework import serializers
from .models import Circuito


class CircuitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = ('id', 'estado', 'n_circuito', 'municipio', 'num_max_candidatos',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update',)
