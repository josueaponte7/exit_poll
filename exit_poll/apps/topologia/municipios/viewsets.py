from .models import Municipio
from .serializers import MunicipioSerializer
from rest_framework import serializers, viewsets


class MunicipioViewSet(viewsets.ModelViewSet):

    serializer_class = MunicipioSerializer
    queryset = Municipio.objects.all()
