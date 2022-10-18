from django.shortcuts import render , redirect
from .models import Todo
# Create your views here.

def Todo_index(request):
    todo_count = len(Todo.objects.all())
    ctx={
        "msg":"Hello Todo",
        "todo_count":todo_count,
    }
    return render(request,"Todo/index.html",ctx)

def Todo_list(request):
    todo_list = Todo.objects.all()
    ctx = {"td_list": todo_list}
    return render(request, "Todo/list.html",ctx)

def Todo_create(request):
    
    if request.method == "POST": #파라미터추출, 데이터저장
        todo = Todo(
            title = request.POST["title"],
            content = request.POST["content"],
        )
        todo.save()
        return redirect("main")
        # return render(request,"board/index.html")

    return render(request,"Todo/create.html")

def Todo_detail(request, pk): # Primary Key(주키- 중복없고 생략없는)
    td = Todo.objects.get(pk = pk)
    ctx = {"td": td}
    return render(request, "Todo/detail.html",ctx)

def Todo_update(request, pk): # Primary Key(주키- 중복없고 생략없는)

    if request.method == 'POST': #데이터 변경작업
        post_data = request.POST

        my_post = Todo.objects.get(id=pk)
        my_post.title = post_data.get('title')        
        my_post.content = post_data.get('content')        
        my_post.save() #DBMS에 저장
        return redirect('list') #게시물 목록

    td = Todo.objects.get(pk = pk)
    ctx = {"todo": td}
    return render(request, "Todo/update.html",ctx)