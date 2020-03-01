#NFC TOOLS

from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from django_markdown.models import MarkdownField
from django.utils import timezone
from django.utils.timezone import now

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

unit_choices = (
    ('kg','Kilogramo'),
    ('litros', 'Litro'),
    ('unidad','Unidad'),
)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    image = models.ImageField(upload_to='profile_image', blank=True, default=profile_default)

class Product (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True)
    price = models.FloatField(max_length=10)
    description = models.TextField()
    date = models.DateTimeField(default=now, editable=True)
    available = models.BooleanField(null=True, default=True)
    unit = models.CharField(max_length=6, choices=unit_choices, default='Unidad')
    user = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to='product_image', blank=True)

    def __str__(self):

        return "{}, {} €".format(self.name, self.price)

class Product_history (models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, default=None)
    name = models.TextField(blank=True)
    price = models.FloatField(max_length=10)
    description = models.TextField()
    date = models.DateTimeField()
    available = models.BooleanField(null=True, default=True)
    unit = models.CharField(max_length=6, choices=unit_choices, default='Unidad')
    user = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to='product_image', blank=True)

    def __str__(self):

        return "{}, {} €".format(self.name, self.price)


class Publicity_campaign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='publicity_campaign_image', blank=True)
    user = models.CharField(max_length=40, blank=True)
    product = models.ManyToManyField(Product, blank=True, related_name='products')



#falta relacion N a N

class Recipe (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_image', blank=True)
    product = models.ManyToManyField(Product, blank=True)
    user = models.CharField(max_length=40, blank=True)
    date = models.DateTimeField(default=now, editable=True)


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