from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.

def home (request):
    boards=Board.objects.all()
    # boards_names=[]
    # for board in boards:
    #     boards_names.append(board.name)
    # print(boards_names)
    # responce_html='<br>'.join(boards_names)
    # return HttpResponse(responce_html)
    return render(request,'home.html',{'boards':boards})
    