from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog_main, name="main"),
    path('<int:pk>/', views.blog_view ,name='view'),
    path('create/', views.blog_create ,name='create'),
    path('list/', views.blog_list, name='list'),
    path('update/<int:pk>', views.blog_update, name='update'),
    path('delete/<int:pk>', views.blog_delete, name='delete'),
]