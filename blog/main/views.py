from django.shortcuts import render

from .forms import PostForm
from .models import Post


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html', {'title': 'Dmytro | Lyrics page'})


def post(request):
    posts = Post.objects.all()
    return render(request, 'main/post.html', {'title': "Dmytro | Posts", 'posts': posts})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'main/post_create.html', context=context)
