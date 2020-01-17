from django.conf.urls import url
from .views import index, login, logout, list_users

#publicity_campaign
from .views import create_publicity_campaign, list_publicity_campaign, edit_publicity_campaign, delete_publicity_campaign, list_publicity_campaign_edit, list_publicity_campaign_delete


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/',login, name = 'login'),
    url(r'^logout/',logout, name = 'logout'),
    url(r'^list_users/',list_users, name = "list_users"),
    #crud_publicity_campaign
    url(r'^create_publicity_campaign/',create_publicity_campaign, name = "create_publicity_campaign"),
    url(r'^list_publicity_campaign/',list_publicity_campaign, name = "list_publicity_campaign"),
    url(r'^edit_publicity_campaign/(?P<id>\d+)/$',edit_publicity_campaign, name = "edit_publicity_campaign"),
    url(r'^delete_publicity_campaign/(?P<id>\d+)/$',delete_publicity_campaign, name = "delete_publicity_campaign"),
    url(r'^list_publicity_campaign_edit/',list_publicity_campaign_edit, name = "list_publicity_campaign_edit"),
    url(r'^list_publicity_campaign_delete/',list_publicity_campaign_delete, name = "list_publicity_campaign_delete"),      
    ]
