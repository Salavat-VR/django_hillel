from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from faker import Faker

from .forms import PostForm, SubsForm, CommentForm
from .models import Author, Post, Subscriber, Comment
from .post_service import post_find


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html', {'title': 'Dmytro | Lyrics page'})


def post(request):
    posts = Post.objects.all()
    return render(request, 'main/posts_all.html', {'title': "Dmytro | Posts", 'posts': posts})


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
    return render(request, 'main/all_subs.html', {'data': Subscriber.objects.all()})


def all_authors(request):
    return render(request, 'main/all_authors.html', {'data': Author.objects.all()})


def author_generate(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    return redirect('all_authors')


def api_subscribe(request):
    if request.method == 'POST':
        form = SubsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('api_subscribe')
    else:
        form = SubsForm()

    context = {
        'form': form,
    }
    return render(request, 'main/subscribe.html', context=context)


def post_update(request, post_id):
    err = ''
    pst = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_page')
        else:
            err = 'Error on update Post'
    else:
        form = PostForm(instance=pst)
    context = {
        'form': form,
        'err': err,
    }
    return render(request, 'main/post_update.html', context=context)


def post_show(request, post_id):
    pst = post_find(post_id)
    print(pst)
    cmts = Comment.objects.filter(post=pst)
    for cmt in cmts:
        print(cmt)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            form.post = pst
            form.save()
            redirect('post_show', post_id=post_id)
        else:
            print("wrong!  "*5)
    else:

        form = CommentForm()
        form.post = pst

    context = {
        'form': form,
        'title': pst.title,
        'pst': pst,
    }
    return render(request, 'main/post_show.html', context=context)
