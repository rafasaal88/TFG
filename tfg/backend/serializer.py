from rest_framework import serializers
from .models import Product, Publicity_campaign

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Publicity_Campaign_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Publicity_campaign
        fields = '__all__'