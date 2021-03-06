"""tfg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls import handler404
from django.views import debug
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views  




urlpatterns = [
    path('',include('backend.urls')),
    path('admin/', admin.site.urls),
    path('backend/',include('backend.urls')),
    path('api/v1.0/',include('backend.api_urls')),
    path('api/v1.0/auth',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/v1.0/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'backend.views.mi_error_404'

