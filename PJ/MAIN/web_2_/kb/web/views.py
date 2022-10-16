from audioop import add
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User, Consume, Saving, Card
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from web.forms import UserForm

from .real_estate.test import logic_layer
# from .models import Myuser

from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
# Create your views here.

def index(request):
    return render(request,'../templates/index.html')

def home(request):
    return render(request,'../templates/Home.html')

def login(request):
    return render(request,'../templates/로그인.html')

def 소비(request):
    user_id = request.user.id
    my_info = Consume.objects.filter(username=user_id)
    return render(request,'../templates/마이_개인소비성향.html', {'my_info':my_info})

def 자산(request):
    return render(request,'../templates/마이_개인자산상태.html')

def 적금카드(request):
    user_age = request.user.age
    save_info = Saving.objects.filter(age=user_age)
    card_info = Card.objects.filter(age=user_age)
    return render(request,'../templates/적금카드.html', {'save_info':save_info, 'card_info':card_info})

def my(request):
    return render(request,'../templates/마이페이지.html')

def 주거(request):
    return render(request,'../templates/부동산_맞춤주거지역.html')
def 실거래가(request):
    if request.method == 'POST':
        addres_name = request.POST['address_name']
        addres_name = addres_name.split(' ')
        return render(request=request, template_name='../templates/부동산_실거래가조회.html', context={"SJ": [addres_name[1],addres_name[2],addres_name[3]]})
    else:
        x = [4.744323,28,2.772589,2001,16,195,3.653252,2025,6,0.0,24,0.0]
    return render(request=request, template_name='../templates/부동산_실거래가조회.html', context={"SJ": logic_layer(x)})
def 부동산(request):
    return render(request,'../templates/부동산.html')
def 설명회(request):
    return render(request,'../templates/설명회정보.html')
def 주식(request):
    return render(request,'../templates/주식.html')



# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, '../templates/로그인.html', {'error' : '아이디 또는 비밀번호가 일치하지 않습니다.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, '../templates/로그인.html')

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, '../templates/로그인.html')


def 회원가입(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)  # 사용자 인증
            # login(request, user)  # 로그인
            return redirect('login')
    else:
        form = UserForm()
    return render(request, '../templates/회원가입.html', {'form': form})