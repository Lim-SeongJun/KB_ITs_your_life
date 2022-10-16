from django.contrib import admin
from .models import Board

# Register your models here.
# 관리자페이지를 통해 Board데이터관리기능제공

admin.site.register(Board)