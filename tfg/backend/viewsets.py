from rest_framework import viewsets, permissions
from .models import *
from .serializer import *
from django.utils import timezone
from django.utils.timezone import datetime #important if using timezones

from rest_framework.permissions import IsAuthenticated
from .permissions import UserPermission

today = datetime.today()


class Product_ViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']

class Recipe_ViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = Recipe_Serializer
    http_method_names = ['get']


class User_ViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer
    http_method_names = ['get', 'post']
    permissions_classes = (IsAuthenticated, )

class Publicity_Campaign_ViewSet(viewsets.ModelViewSet):
    #queryset = Publicity_campaign.objects.filter(date_end__gte = today)
    queryset = Publicity_campaign.objects.all()
    serializer_class = Publicity_Campaign_Serializer
    http_method_names = ['get']

class Tag_nfc_ViewSet(viewsets.ModelViewSet):
    queryset = Tag_nfc.objects.all()
    serializer_class = Tag_nfc_Serializer
    http_method_names = ['get']

class Point_ViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all().order_by('id').reverse()
    #permission_classes = (UserPermission,)
    serializer_class = Point_Serializer
    
class Register_activity_ViewSet(viewsets.ModelViewSet):
    queryset = Register_activity.objects.all().order_by('id').reverse()
    serializer_class = Register_activity_Serializer


