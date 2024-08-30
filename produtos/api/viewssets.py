from rest_framework import viewsets
from produtos.api import serializers
from produtos import models

class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductsSerializer
    queryset = models.Products.objects.all()
