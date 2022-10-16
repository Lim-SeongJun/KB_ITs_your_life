from django.shortcuts import render, redirect
from .models import Board
import datetime

def board_main(request):
    return render(request, "board/main.html",{"msg":"HELLO"})
	
def board_create(request):
    if request.method == 'POST': # POST방식 요청?
        post_data = request.POST #입력데이터
        data = Board(
            title=post_data.get('title'),
            content=post_data.get('content'),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now())
        data.save()
        return redirect('main')
    return render(request, "board/create.html")  # GET방식

def board_view(request, pk):
	board = board.objects.get(id=pk)
	return render(request,'board/board_view.html',{'board':board,})

def board_list(request):
    boards = Board.objects.all().order_by('-created_at')
    return render(request, 'board/board_list.html', {'boards':boards})

def board_update(request,pk):
    if request.method == 'POST': #데이터 변경작업
        post_data = request.POST

        my_post = Board.objects.get(id=pk)
        my_post.title = post_data.get('title')        
        my_post.content = post_data.get('content')        
        my_post.updated_at = datetime.datetime.now()        
        my_post.save()
        return redirect('list')
    else:
        my_post = Board.objects.get(id=pk)

    return render(
        request,
        'board/update.html',
        {'board':my_post})

def board_delete(request,pk):
    post = Board.objects.get(id=pk)
    post.delete()
    return redirect('list')