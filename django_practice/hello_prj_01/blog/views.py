from django.shortcuts import render

def index(request):
    # http:/127.0.0.1:8000/blog/
    # 필요한 작업코드작성
    # html 경로 반환
    return render(request,'blog/index.html',{"msg":"hello~"})
# Create your views here.
