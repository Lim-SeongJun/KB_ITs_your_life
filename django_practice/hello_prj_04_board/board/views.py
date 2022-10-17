from django.shortcuts import render , redirect
from .models import Board
# Create your views here.
# url에 따른 작업코드를 실행할 함수 작성
# urls.py에서 지정
def index(request):
    #필요한 작업코드작성
    #html에 표시할 데이터는 사전타입의 context에 저장
    ctx = {"msg":"Welcome 장고"}
    return render(request,"board/index.html",ctx)

def board_create(request):
    
    if request.method == "POST": #파라미터추출, 데이터저장
        board = Board(
            title = request.POST["title"],
            content = request.POST["content"],
        )
        board.save()
        return redirect("main")
        # return render(request,"board/index.html")

    return render(request,"board/create.html")

def board_list(request):
    board_list = Board.objects.all()
    ctx = {"brd_list": board_list}
    return render(request, "board/list.html",ctx)

def board_detail(request, pk): # Primary Key(주키- 중복없고 생략없는)
    brd = Board.objects.get(pk = pk)
    ctx = {"brd": brd}
    return render(request, "board/detail.html",ctx)

def board_update(request, pk): # Primary Key(주키- 중복없고 생략없는)

    if request.method == 'POST': #데이터 변경작업
        post_data = request.POST

        my_post = Board.objects.get(id=pk)
        my_post.title = post_data.get('title')        
        my_post.content = post_data.get('content')        
        my_post.save() #DBMS에 저장
        return redirect('list') #게시물 목록

    brd = Board.objects.get(pk = pk)
    ctx = {"brd": brd}
    return render(request, "board/update.html",ctx)


