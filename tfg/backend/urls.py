from django.conf.urls import url
from .views import create_company, home

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^company_form/',create_company, name = "create_company")
]