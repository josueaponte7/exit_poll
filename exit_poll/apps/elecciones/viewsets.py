from .models import Eleccion
from .serializers import EleccionSerializer
from rest_framework import serializers, viewsets


class EleccionViewSet(viewsets.ModelViewSet):

    serializer_class = EleccionSerializer
    queryset = Eleccion.objects.all()


