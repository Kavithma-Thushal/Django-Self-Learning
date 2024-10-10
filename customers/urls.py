from django.urls import path
from customers.views import home

urlpatterns = [path('', home, name='home')]
