from .models import Partidos
from .serializers import PartidosSerializer
from rest_framework import serializers, viewsets


class PartidosViewSet(viewsets.ModelViewSet):

    serializer_class = PartidosSerializer
    queryset = Partidos.objects.all()
