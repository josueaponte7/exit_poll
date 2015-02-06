from .models import Centros
from .serializers import CentrosSerializer
from rest_framework import serializers, viewsets


class CentrosViewSet(viewsets.ModelViewSet):

    serializer_class = CentrosSerializer
    queryset = Centros.objects.all()
