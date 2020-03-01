from rest_framework import serializers
from .models import Product, Publicity_campaign, User
from rest_framework.authtoken.models import Token

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Publicity_Campaign_Serializer(serializers.ModelSerializer):
    class Meta:        
        model = Publicity_campaign
        fields = ('id', 'name', 'date_start', 'date_end', 'description', 'image', 'product')



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


class Product_Serializer_New(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True) 
    
    class Meta:
        model = Publicity_campaign
        fields = ('id', 'name', 'product')




