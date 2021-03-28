from django.shortcuts import render

from .models import Post


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html', {'title': 'Dmytro | Lyrics page'})


def post(request):
    posts = Post.objects.all()

    return render(request, 'main/post.html', {'title': "Dmytro | Posts", 'posts': posts})
