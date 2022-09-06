from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:institution_id>/', views.detail, name='detail'),
    path('answer/create/<int:institution_id>/', views.review_create, name='review_create'),
    path('answer/modify/<int:institution_id>/', views.review_modify, name='review_modify'),
    path('answer/delete/<int:review_id>/', views.review_delete, name='review_delete'),
]