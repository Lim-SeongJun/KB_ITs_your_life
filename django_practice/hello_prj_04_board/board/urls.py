from django.contrib import admin
from django.urls import path, include
from . import views
# 요청 url을 처리할 함수 연결
urlpatterns = [
    path('', views.index ,name="main"), #대문페이지
    path('create/', views.board_create ,name='create'),
    path('list/', views.board_list, name='list'),
    path('<int:pk>/', views.board_detail, name='list'),
    path('update/<int:pk>', views.board_update, name='update'),
]
