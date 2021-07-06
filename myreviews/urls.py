from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='myreviews'),
    path('<int:myreview_id>/', views.myreview, name='myreview'),
    path('search/', views.search, name='search'),

] 