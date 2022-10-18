from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index , name="main"),
    path('increate/',views.InMoneyCreateView.as_view(), name="increate" ),
    path('outcreate/',views.OutMoneyCreateView.as_view(), name="outcreate" ),
    path('list/',views.MoneyListView.as_view(), name="list" ),
    path('detail/<int:pk>',views.MoneyDetailView.as_view(), name="detail" ),
]
