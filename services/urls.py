from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='services'),
    path('computer_laptop_repair', views.computer_laptop_repair, name='computer_laptop_repair'),
    path('computer_laptop_upgrade', views.computer_laptop_upgrade, name='computer_laptop_upgrade'),
    path('iot', views.iot, name='iot'),
    path('networking', views.networking, name='networking'),
    path('webdevelopment', views.webdevelopment, name='webdevelopment'),
    


]