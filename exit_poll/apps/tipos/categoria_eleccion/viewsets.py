from .models import Categoria
from .serializers import CategoriaSerializer
from rest_framework import serializers, viewsets


class CategoriaViewSet(viewsets.ModelViewSet):

    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
