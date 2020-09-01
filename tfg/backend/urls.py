from django.conf.urls import url
from .views import *

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 



urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^user_login/',user_login, name = 'user_login'),
    url(r'^user_logout/',user_logout, name = 'user_logout'),

    #crud_user
    url(r'^users_list/',users_list, name = "users_list"),
    url(r'^user_profile_admin/',user_profile_admin, name = "user_profile_admin"),
    url(r'^user_profile/(?P<id>\d+)/$',user_profile, name = "user_profile"),
    url(r'^user_profile_edit/(?P<id>\d+)/$',user_profile_edit, name = "user_profile_edit"),
    url(r'^user_edit_email/(?P<id>\d+)/$',user_edit_email, name = "user_edit_email"),
    url(r'^user_edit_name/(?P<id>\d+)/$',user_edit_name, name = "user_edit_name"),
    url(r'^user_edit_picture/(?P<id>\d+)/$',user_edit_picture, name = "user_edit_picture"),
    url(r'^user_create/',user_create, name = "user_create"),
    url(r'^user_disable/(?P<id>\d+)/$',user_disable, name = "user_disable"),
    url(r'^user_enable/(?P<id>\d+)/$',user_enable, name = "user_enable"),



    #crud_publicity_campaign
    url(r'^publicity_campaign_create/',publicity_campaign_create, name = "publicity_campaign_create"),
    url(r'^publicity_campaign_list/',publicity_campaign_list, name = "publicity_campaign_list"),
    url(r'^publicity_campaign_edit/(?P<id>\d+)/$',publicity_campaign_edit, name = "publicity_campaign_edit"),
    url(r'^publicity_campaign_delete/(?P<id>\d+)/$',publicity_campaign_delete, name = "publicity_campaign_delete"),
    url(r'^publicity_campaign/(?P<id>\d+)/$',publicity_campaign, name = "publicity_campaign"),      
    url(r'^publicity_campaign_complete/(?P<id>\d+)/$',publicity_campaign_complete, name = "publicity_campaign_complete"),      


    #crud_product
    url(r'^product_create/',product_create, name = "product_create"),
    url(r'^product_list/',product_list, name = "product_list"),
    url(r'^product/(?P<id>\d+)/$',product, name = "product"),
    url(r'^product_history/(?P<id>\d+)/$',product_history, name = "product_history"),
    url(r'^product_disable/(?P<id>\d+)/$',product_disable, name = "product_disable"),
    url(r'^product_enable/(?P<id>\d+)/$',product_enable, name = "product_enable"),
    url(r'^product_edit/(?P<id>\d+)/$',product_edit, name = "product_edit"),
    url(r'^product_list_history/(?P<id>\d+)/$',product_list_history, name = "product_list_history"),

    #crud_recipe
    url(r'^recipe_create/',recipe_create, name = "recipe_create"),
    url(r'^recipe_list/',recipe_list, name = "recipe_list"),
    url(r'^recipe/(?P<id>\d+)/$',recipe, name = "recipe"),
    url(r'^recipe_edit/(?P<id>\d+)/$',recipe_edit, name = "recipe_edit"),
    url(r'^recipe_delete/(?P<id>\d+)/$',recipe_delete, name = "recipe_delete"),


    #crud tag_nfc
    url(r'^tag_nfc_create/',tag_nfc_create, name = "tag_nfc_create"),
    url(r'^tag_nfc_list/',tag_nfc_list, name = "tag_nfc_list"),
    url(r'^tag_nfc_disable/(?P<id>\d+)/$',tag_nfc_disable, name = "tag_nfc_disable"),
    url(r'^tag_nfc_enable/(?P<id>\d+)/$',tag_nfc_enable, name = "tag_nfc_enable"),
    url(r'^tag_nfc_edit/(?P<id>\d+)/$',tag_nfc_edit, name = "tag_nfc_edit"),
    url(r'^tag_nfc/(?P<id>\d+)/$',tag_nfc, name = "tag_nfc"),

    #staditics
    url(r'^register_activity_list/',register_activity_list, name = "register_activity_list"),
    url(r'^register_activity_sesions/',register_activity_sesions, name = "register_activity_sesions"),
    url(r'^register_activity_campaign/(?P<id>\d+)/$',register_activity_campaign, name = "register_activity_campaign"),
    url(r'^register_activity_product/(?P<id>\d+)/$',register_activity_product, name = "register_activity_product"),
    url(r'^register_activity_recipe/(?P<id>\d+)/$',register_activity_recipe, name = "register_activity_recipe"),
    url(r'^register_activity_nfc/',register_activity_nfc, name = "register_activity_nfc"),
    url(r'^register_activity_map/(?P<id>\d+)/$',register_activity_map, name = "register_activity_map"),
    url(r'^register_activity_promotion/',register_activity_promotion, name = "register_activity_promotion"),



    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)