from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # 기본적으로 제공하는 필드 외에 원하는 필드를 적어준다.
    age = models.CharField(max_length=50)
    child = models.CharField(max_length=10)
    Marriage = models.CharField(max_length=10)
    work = models.CharField(max_length=10)
    work_address = models.CharField(max_length=100)
    hope_address = models.CharField(max_length=100)

class Consume(models.Model): 
    username=models.ForeignKey(User,related_name="user",on_delete=models.CASCADE, db_column="username")
    food = models.IntegerField()
    cafe = models.IntegerField()
    shopping = models.IntegerField()
    education = models.IntegerField()
    leisure = models.IntegerField()
    medical = models.IntegerField()
    traffic = models.IntegerField()
    life  = models.IntegerField()
    travel  = models.IntegerField()

class Saving(models.Model):
    age=models.CharField(max_length=100)
    saving_name = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    interest_rate = models.CharField(max_length=100)

class Card(models.Model):
    age=models.CharField(max_length=100)
    card_name = models.CharField(max_length=100)
    benefit1 = models.CharField(max_length=100)
    benefit2 = models.CharField(max_length=100)
    benefit3 = models.CharField(max_length=100)


# Saving.objects.create(age="20대",saving_name="KB내맘대로적금", period="6~36개월", price="1만원 이상",interest_rate="최고 연 3.45% (36개월)")
# Saving.objects.create(age="30대",saving_name="직장인우대적금", period="1년,2년,3년", price="1만~3백만원",interest_rate="최고 연 3.75% (36개월)")
# Saving.objects.create(age="40대",saving_name="KB골든라이프연금우대적금", period="1년", price="1만~3백만원",interest_rate="최고 연 3.05%")

# Card.objects.create(age="20대", card_name="위글위글 첵첵 체크카드", benefit1="대중교통 2-4천원 청구할인 ", benefit2="온라인간편결제 2-4천원 환급할인", benefit3="스타벅스 2-4천원 환급할인")
# Card.objects.create(age="30대", card_name="노리 체크카드", benefit1="대중교통 10% 청구할인", benefit2="이동통신요금 2,500원 환급할인", benefit3="CGV 35% 환급할인")
# Card.objects.create(age="40대", card_name="골든대로 체크카드", benefit1="병원/약국 5% 적립", benefit2="대형마트/홈쇼핑 5% 적립", benefit3="골프/사우나 5% 적립")