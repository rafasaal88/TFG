from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from django_markdown.models import MarkdownField
from django.utils import timezone

# Create your models here.

"""
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    nif = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=12)
    mail = models.EmailField(max_length=40)
    web_adress = models.CharField(max_length=50)
"""

profile_default = 'profile_image/profile_default.png'


""" default="blabla.jpg" """

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    image = models.ImageField(upload_to='profile_image', blank=True, default=profile_default)



class Publicity_campaign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='publicity_campaign_image', blank=True)

class Product (models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField(max_length=10)
    description = models.TextField(blank=True)
    summary = models.TextField()
    picture = models.ImageField(blank=True)
    publicity_campaing = models.ManyToManyField(Publicity_campaign, blank=True)

#falta relacion N a N

class Recipe (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    picture = models.ImageField()
    product = models.ManyToManyField(Product, blank=True)


class Tag_nfc(models.Model):
    id = models.AutoField(primary_key=True)
    date_start = models.DateField()
    date_end = models.DateField()
    identify = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, default=None)

class Shopping_bag(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

class Register_activity(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    tag_nfc = models.ForeignKey(Tag_nfc, on_delete=models.CASCADE, null=True, default=None)