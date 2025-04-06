from django.urls import path
from .views import CategoryApiView, ProductApiView

urlpatterns = [
    path('categories', CategoryApiView.as_view(), name='api-categories'),
    path('categories/<int:id>', CategoryApiView.as_view(), name='api-categories-detail'),
    path('products', ProductApiView.as_view(), name='products-api')
]
