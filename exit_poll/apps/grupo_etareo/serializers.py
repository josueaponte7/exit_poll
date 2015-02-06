from rest_framework import serializers
from .models import Grupo_Etareo


class Grupo_EtareoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo_Etareo
        fields = ('id', 'descripcion', 'grupo_etareo', 'user_create', 'user_update', 'fecha_create', 'fecha_update',)
