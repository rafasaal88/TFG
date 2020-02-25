from rest_framework import viewsets
from .models import Product, Publicity_campaign
from .serializer import ProductSerializer, Publicity_Campaign_Serializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Publicity_Campaign_ViewSet(viewsets.ModelViewSet):
    queryset = Publicity_campaign.objects.all()
    serializer_class = Publicity_Campaign_Serializer