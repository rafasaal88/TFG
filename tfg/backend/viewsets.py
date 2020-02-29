from rest_framework import viewsets
from .models import Product, Publicity_campaign, User
from .serializer import ProductSerializer, Publicity_Campaign_Serializer, User_Serializer
from django.utils import timezone
from django.utils.timezone import datetime #important if using timezones

today = datetime.today()

products_filter = Publicity_campaign.objects.filter(date_end = today)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Publicity_Campaign_ViewSet(viewsets.ModelViewSet):
    queryset = Publicity_campaign.objects.filter(date_end__gte = today)
    serializer_class = Publicity_Campaign_Serializer

class User_ViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer