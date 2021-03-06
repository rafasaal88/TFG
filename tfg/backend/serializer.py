from rest_framework import serializers, permissions
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'available', 'unit', 'image')



class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        print(user)
        Token.objects.create(user=user)
        return user


class Publicity_Campaign_Serializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True) 
    
    class Meta:
        model = Publicity_campaign
        fields = ('id', 'name', 'date_start', 'date_end', 'description', 'image', 'product')


class Recipe_Serializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id','name', 'description', 'image', 'product', 'product')
        depth = 1


class Tag_nfc_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tag_nfc
        fields = ('__all__')

class Point_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('__all__')

class Register_activity_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Register_activity
        fields = ('__all__')
