from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import PostForm, SubsForm
from .models import Author, Post, Subscriber


def index(request):
    # some type of documentation
    return render(request, 'main/index.html')


def about(request):
    # some type of documentation
    return render(request, 'main/about.html', {'title': 'Dmytro | Lyrics page'})


def post(request):
    # some type of documentation
    return render(request, 'main/post.html', {'title': "Dmytro | Posts", 'posts': Post.objects.all()})


def post_create(request):
    """
    :param request:
    :return: the main page in case the post was created successfully
    """
    custom_error = ''
    if request.method == '':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_page')
        else:
            custom_error = 'Oops! Something wrong..'
    else:
        form = PostForm()
    context = {
        'form': form,
        'err_my': custom_error
    }
    return render(request, 'main/post_create.html', context=context)


def post_api(request):
    data = list(Post.objects.values())
    return JsonResponse(data, safe=False)


def all_subs(request):
    data = list(Subscriber.objects.values())
    return JsonResponse(data, safe=False)


def all_authors(request):
    data = list(Author.objects.values())
    return JsonResponse(data, safe=False)


def create_author(request):
    return 1


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
