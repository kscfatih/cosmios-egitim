from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories',CategoryModelViewSet, basename='category')
router.register(r'products',ProductModelViewSet, basename='product')


urlpatterns = [

    path('router/', include(router.urls))
    
]
