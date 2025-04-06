from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home_index'),
    path('home', views.Home.as_view(), name='home'),
    path('reservation', views.Reservation.as_view(), name='reservation'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('menu', views.Menu.as_view(), name='menu'),
    path('api/', include('web_site.api.urls'))
]
