from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns =[
    path('',views.blog_main),
    path('calc_1/',views.calc_1),
    path('calc_2/',views.calc_2),
    path('gugudan/',views.gugudan),
]