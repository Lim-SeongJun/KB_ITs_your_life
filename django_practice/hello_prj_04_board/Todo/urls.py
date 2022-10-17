from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Todo_index ,name="main"), #대문페이지
    path('create/', views.Todo_create ,name='create'),
    path('list/', views.Todo_list, name='list'),
    path('<int:pk>/', views.Todo_detail, name='list'),
    path('update/<int:pk>', views.Todo_update, name='update'),
]