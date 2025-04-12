from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories',CategoryModelViewSet, basename='category')
router.register(r'products',ProductModelViewSet, basename='product')
router.register(r'reservations', ReservationViewset, basename='reservation')


urlpatterns = [
    path('categories', CategoryApiView.as_view(), name='api-categories'),
    path('categories/<int:id>', CategoryApiView.as_view(), name='api-categories-detail'),
    path('products', ProductApiView.as_view(), name='products-api'),
    path('productsf', products_api_view, name='productsf'),
    path('category-generic', CategoryGenericViewListCreate.as_view(), name='categories'),
    path('category-generic/<int:pk>', CategoryGenericView.as_view(), name='category-detail'),
    path('delete-category/<int:pk>', CategoryDeleteView.as_view(), name='category-delete'),
    path('update-category/<int:pk>', CategoryUpdateView.as_view(), name='update-category'),
    path('contacts', ContactApiView.as_view(), name='contacts-api'),
    path('contacts/<int:id>', ContactApiView.as_view(), name='contacts-api'),
    path('router/', include(router.urls))
    
]
