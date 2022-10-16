from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User, Consume, Saving, Card   #같은 경로의 models.py에서 User라는 클래스를 임포트한다.

admin.site.register(User)
admin.site.register(Consume)
admin.site.register(Saving)
admin.site.register(Card)