from django.conf.urls import url
from .views import create_company, index, list_company, edit_company, delete_company, login, logout, list_users

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/',login, name = 'login'),
    url(r'^logout/',logout, name = 'logout'),
    #crud methods company
    url(r'^create_company/',create_company, name = "create_company"),
    url(r'^list_company/',list_company, name = "list_company"),
    url(r'^edit_company/(?P<id>\d+)/$',edit_company, name = "edit_company"),
    url(r'^delete_company/(?P<id>\d+)/$',delete_company, name = "delete_company"),

    #crud methods user
    url(r'^list_users/',list_users, name = "list_users"),



]