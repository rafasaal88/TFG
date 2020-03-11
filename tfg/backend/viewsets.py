from rest_framework import viewsets
from .models import Product, Publicity_campaign, User, Product, Recipe, Tag_nfc, Point
from .serializer import ProductSerializer, Publicity_Campaign_Serializer, User_Serializer, Recipe_Serializer, Tag_nfc_Seralizer, Point_Seralizer
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

class Tag_nfc_ViewSet(viewsets.ModelViewSet):
    queryset = Tag_nfc.objects.filter(available = True)
    serializer_class = Tag_nfc_Seralizer
    http_method_names = ['get']

class Point_Seralizer_ViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = Point_Seralizer



