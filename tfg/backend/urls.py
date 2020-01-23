from django.conf.urls import url
from .views import index, login_user, logout, list_users, profile, view_user, edit_user_email, view_user_edit, edit_user_name

#publicity_campaign
from .views import create_publicity_campaign, list_publicity_campaign, edit_publicity_campaign, delete_publicity_campaign, list_publicity_campaign_edit, list_publicity_campaign_delete


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login_user/',login_user, name = 'login_user'),
    url(r'^logout/',logout, name = 'logout'),
    url(r'^list_users/',list_users, name = "list_users"),
    url(r'^profile/',profile, name = "profile"),
    url(r'^view_user/(?P<id>\d+)/$',view_user, name = "view_user"),
    url(r'^view_user_edit/(?P<id>\d+)/$',view_user_edit, name = "view_user_edit"),
    url(r'^edit_user_email/(?P<id>\d+)/$',edit_user_email, name = "edit_user_email"),
    url(r'^edit_user_name/(?P<id>\d+)/$',edit_user_name, name = "edit_user_name"),

    #crud_publicity_campaign
    url(r'^create_publicity_campaign/',create_publicity_campaign, name = "create_publicity_campaign"),
    url(r'^list_publicity_campaign/',list_publicity_campaign, name = "list_publicity_campaign"),
    url(r'^edit_publicity_campaign/(?P<id>\d+)/$',edit_publicity_campaign, name = "edit_publicity_campaign"),
    url(r'^delete_publicity_campaign/(?P<id>\d+)/$',delete_publicity_campaign, name = "delete_publicity_campaign"),
    url(r'^list_publicity_campaign_edit/',list_publicity_campaign_edit, name = "list_publicity_campaign_edit"),
    url(r'^list_publicity_campaign_delete/',list_publicity_campaign_delete, name = "list_publicity_campaign_delete"),      
    ]
