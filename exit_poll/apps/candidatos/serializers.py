from rest_framework import serializers
from .models import Candidatos,SEXO


class CandidatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatos
        fields = ('id', 'nombre', 'apellido', 'cedula', 'foto', 'sexo',
                  'edad',
                  'twitter', 'part_politico', 'tipo_eleccion', 'tipo_candidatura', 'eleccion',
                  'estado', 'circuito', 'municipio', 'parroquia',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update',)
