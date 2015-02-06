from .models import Tipo_eleccion
from .serializers import Tipo_eleccionSerializer
from rest_framework import serializers, viewsets


class Tipo_eleccionViewSet(viewsets.ModelViewSet):

    serializer_class = Tipo_eleccionSerializer
    queryset = Tipo_eleccion.objects.all()
