"""kb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import include
from web import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')), 
    path('',views.index, name='index'),
    path('home/',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('소비/',views.소비, name='소비'),
    path('자산/',views.자산, name='자산'),
    path('적금카드/',views.적금카드, name='적금카드'),
    path('my/',views.my, name='my'),
    path('주거/',views.주거, name='주거'),
    path('실거래가/',views.실거래가, name='실거래가'),
    path('부동산/',views.부동산, name='부동산'),
    path('설명회/',views.설명회, name='설명회'),
    path('주식/',views.주식, name='주식'),
    path('회원가입/',views.회원가입, name='회원가입'),
    path('signup/', account.views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
urlpatterns = ...

urlpatterns += staticfiles_urlpatterns()