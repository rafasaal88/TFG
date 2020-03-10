from rest_framework import viewsets
from .models import Product, Publicity_campaign, User, Product, Recipe
from .serializer import ProductSerializer, Publicity_Campaign_Serializer, User_Serializer, Recipe_Serializer
from django.utils import timezone
from django.utils.timezone import datetime #important if using timezones

today = datetime.today()


class Product_ViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available = True)
    serializer_class = ProductSerializer
    http_method_names = ['get']

class Recipe_ViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = Recipe_Serializer


class User_ViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer
    http_method_names = ['get', 'post']

class Publicity_Campaign_ViewSet(viewsets.ModelViewSet):
    queryset = Publicity_campaign.objects.filter(date_end__gte = today)
    serializer_class = Publicity_Campaign_Serializer
    http_method_names = ['get']


