from django.urls import path
from . import views

app_name = 'map'

urlpatterns = [
    path('', views.index, name='index'),
    path('seoul/', views.seoul, name='seoul'),
    path('teenager/', views.teenager, name='teenager'),
]