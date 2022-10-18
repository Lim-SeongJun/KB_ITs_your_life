from django.db import models

# Create your models here.
# Create your models here.
class Money( models.Model ):
    title = models.CharField(max_length=200) #길이제한가능한 타입
    money = models.IntegerField() 
    # auto_now_add=True 자동으로 현재시간 저장
    created_at = models.DateTimeField(auto_now_add=True)