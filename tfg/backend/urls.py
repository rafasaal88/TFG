from django.conf.urls import url
from .views import index, user_login, user_logout, users_list, user_profile_admin, user_profile, user_edit_email, user_profile_edit, user_edit_name, user_edit_picture

#publicity_campaign
from .views import publicity_campaign_create, publicity_campaign_list, publicity_campaign_edit, publicity_campaign_delete, publicity_campaign
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^user_login/',user_login, name = 'user_login'),
    url(r'^user_logout/',user_logout, name = 'user_logout'),
    url(r'^users_list/',users_list, name = "users_list"),
    url(r'^user_profile_admin/',user_profile_admin, name = "user_profile_admin"),
    url(r'^user_profile/(?P<id>\d+)/$',user_profile, name = "user_profile"),
    url(r'^user_profile_edit/(?P<id>\d+)/$',user_profile_edit, name = "user_profile_edit"),
    url(r'^user_edit_email/(?P<id>\d+)/$',user_edit_email, name = "user_edit_email"),
    url(r'^user_edit_name/(?P<id>\d+)/$',user_edit_name, name = "user_edit_name"),
    url(r'^user_edit_picture/(?P<id>\d+)/$',user_edit_picture, name = "user_edit_picture"),


    #crud_publicity_campaign
    url(r'^publicity_campaign_create/',publicity_campaign_create, name = "publicity_campaign_create"),
    url(r'^publicity_campaign_list/',publicity_campaign_list, name = "publicity_campaign_list"),
    url(r'^publicity_campaign_edit/(?P<id>\d+)/$',publicity_campaign_edit, name = "publicity_campaign_edit"),
    url(r'^publicity_campaign_delete/(?P<id>\d+)/$',publicity_campaign_delete, name = "publicity_campaign_delete"),
    url(r'^publicity_campaign/(?P<id>\d+)/$',publicity_campaign, name = "publicity_campaign"),      
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)