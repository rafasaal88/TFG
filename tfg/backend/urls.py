from django.conf.urls import url
from .views import index, login_user, logout, list_users, profile, view_user

#publicity_campaign
from .views import create_publicity_campaign, list_publicity_campaign, edit_publicity_campaign, delete_publicity_campaign, list_publicity_campaign_edit, list_publicity_campaign_delete


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login_user/',login_user, name = 'login_user'),
    url(r'^logout/',logout, name = 'logout'),
    url(r'^list_users/',list_users, name = "list_users"),
    url(r'^profile/',profile, name = "profile"),
    url(r'^view_user/(?P<id>\d+)/$',view_user, name = "view_user"),

    #crud_publicity_campaign
    url(r'^create_publicity_campaign/',create_publicity_campaign, name = "create_publicity_campaign"),
    url(r'^list_publicity_campaign/',list_publicity_campaign, name = "list_publicity_campaign"),
    url(r'^edit_publicity_campaign/(?P<id>\d+)/$',edit_publicity_campaign, name = "edit_publicity_campaign"),
    url(r'^delete_publicity_campaign/(?P<id>\d+)/$',delete_publicity_campaign, name = "delete_publicity_campaign"),
    url(r'^list_publicity_campaign_edit/',list_publicity_campaign_edit, name = "list_publicity_campaign_edit"),
    url(r'^list_publicity_campaign_delete/',list_publicity_campaign_delete, name = "list_publicity_campaign_delete"),      
    ]
