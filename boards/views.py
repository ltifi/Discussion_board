from email import message
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Board
from django.contrib.auth.models import User
from .models import Topic, Post
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    boards = Board.objects.all()
    # boards_names=[]
    # for board in boards:
    #     boards_names.append(board.name)
    # print(boards_names)
    # responce_html='<br>'.join(boards_names)
    # return HttpResponse(responce_html)
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, board_id):
    # try:
    #     board=Board.objects.get(pk=board_id)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'topics.html', {'board': board})


@login_required
def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                created_by=request.user,
                topic=topic

            )
            return redirect('board_topics', board_id=board.pk)
    else:
        form = NewTopicForm()
    # if request.method == 'POST':
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     user = User.objects.first()
    #     # topic = Topic.objects.create(
    #     #     subject=subject, board=board, created_by=user)
    #     # post = Post.objects.create(
    #     #     message=message, topic=topic, created_by=user)
    #     return redirect('board_topics',board_id=board.pk)
    return render(request, 'new_topic.html', {'board': board, 'form': form})


def topic_posts(request, board_id, topic_id):
    topic = get_object_or_404(Topic, board__pk=board_id, pk=topic_id)
    return render(request, 'topic_posts.html', {'topic': topic})


def about(request):
    return HttpResponse(request, "yes")
