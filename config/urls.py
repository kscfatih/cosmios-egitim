"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
'''
2 adet token var. 
access token -> Sisteme attığımız isteklerde kimliğimiz olmuş oluyor örn 5 dk
refresh token -> access tokenin süresi bitince yeni access token alabilmek için kullanılır. 
bunda bir süresi var örn 1gün
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_site.urls')), 
    path('rest-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # burası 2 det token veriyor access, refresh
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),# accessin süresi dolunca bu url ile yeni bir access alıyoruz bu url ile beraber refresh tokeni göndererek alıyoruz
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),# access tokenin durumunu kontrol eder bu sayede yeni bir token alıp almayacağımıza karar veririz
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
