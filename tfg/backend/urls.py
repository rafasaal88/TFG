from django.conf.urls import url
from .views import create_company, home, list_company, edit_company, delete_company, login, logout

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^login/',login, name = 'login'),
    url(r'^logout/',logout, name = 'logout'),
    url(r'^create_company/',create_company, name = "create_company"),
    url(r'^list_company/',list_company, name = "list_company"),
    url(r'^edit_company/(?P<id>\d+)/$',edit_company, name = "edit_company"),
    url(r'^delete_company/(?P<id>\d+)/$',delete_company, name = "delete_company"),

]