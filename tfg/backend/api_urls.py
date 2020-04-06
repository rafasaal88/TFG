
#REST

from rest_framework import routers


from django.conf.urls import url
from rest_framework import routers
from . import views

from django.urls import include, path
from rest_framework import routers
from backend import views
from django.contrib import admin
from django.urls import path, include

from .viewsets import Product_ViewSet, Publicity_Campaign_ViewSet, User_ViewSet, Recipe_ViewSet, Tag_nfc_ViewSet, Point_ViewSet

router = routers.DefaultRouter()

router.register('recipe_list', Recipe_ViewSet)
router.register('product_list', Product_ViewSet)
router.register('publicity_campaign_list', Publicity_Campaign_ViewSet)
router.register('user', User_ViewSet)
router.register('tag_nfc', Tag_nfc_ViewSet)
router.register('point', Point_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]