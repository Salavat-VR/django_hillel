from django.http import JsonResponse
from django.shortcuts import render, redirect
from faker import Faker

from .forms import PostForm, SubsForm
from .models import Author, Post, Subscriber


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
        form.save()
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'main/post_create.html', context=context)


def post_api(request):
    data = list(Post.objects.values())
    return JsonResponse(data, safe=False)


def all_subs(request):
    data = list(Subscriber.objects.values())
    return JsonResponse(data, safe=False)


def all_authors(request):
    context = {'data': Author.objects}
    return render(request, 'main/all_authors.html', context=context)


def author_generate(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    return redirect('all_authors')


def api_subscribe(request):
    if request.method == "POST":
        form = SubsForm(request.POST)
        form.save()
    else:
        form = SubsForm()

    context = {
        'form': form,
    }
    return render(request, 'main/subscribe.html', context=context)
