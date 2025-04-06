from django.contrib import admin
from .models import *

admin.site.register([Contact, Reservation, Product, Category, Settings, SubText])
