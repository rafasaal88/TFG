from rest_framework import viewsets
from .models import Product, Publicity_campaign, User
from .serializer import ProductSerializer, Publicity_Campaign_Serializer, User_Serializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Publicity_Campaign_ViewSet(viewsets.ModelViewSet):
    queryset = Publicity_campaign.objects.all()
    serializer_class = Publicity_Campaign_Serializer

class User_ViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer