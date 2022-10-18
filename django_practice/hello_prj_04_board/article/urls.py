from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index ,name="main"), 
    path('create/', views.ArticleCreateView.as_view ,name="create"), 
    path('list/', views.ArticleListView.as_view ,name="list"), 

]