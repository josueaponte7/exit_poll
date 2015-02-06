from rest_framework import serializers
from .models import ExitPoll


class ExitPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExitPoll
        fields = ('eleccion','candidatos','g_etareo',
                  'user_create','user_update','fecha_create','fecha_update',)

