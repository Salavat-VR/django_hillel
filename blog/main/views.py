from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from faker import Faker

from .forms import PostForm, SubsForm, CommentForm
from .models import Author, Post, Subscriber, Comment, Book, Category
from .post_service import post_find
from .tasks import notification_by_email


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
    authors = Author.objects.all().prefetch_related('books')
    context = {
        'data': authors
    }
    return render(request, 'main/all_authors.html', context=context)


def author_generate(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    return redirect('all_authors')


def api_subscribe(request):
    subscribe_success = False
    if request.method == 'POST':
        form = SubsForm(request.POST)
        if form.is_valid():
            form.save()
            subscribe_success = True
    else:
        form = SubsForm()

    if subscribe_success:
        email_to = request.POST.get('email_to')
        author = request.POST.get('author')
        # author = Author.objects.get(id=author_id)

        notification_by_email.delay(email_to, author)
        return redirect('api_subscribe')

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
    cmts = Comment.objects.filter(post=pst)

    form = CommentForm(request.POST)
    if form.is_valid():
        com = form.save(commit=False)
        com.post = pst
        com.save()
        return redirect('post_show', post_id=post_id)

    context = {
        'form': form,
        'title': pst.title,
        'pst': pst,
        'cmts': cmts
    }
    return render(request, 'main/post_show.html', context=context)


def all_books(request):
    books = Book.objects.all().only('title', 'author', 'category').select_related('author', 'category')
    context = {
        'data': books
    }

    return render(request, 'main/all_books.html', context=context)


def all_categories(request):
    categories = Category.objects.all().prefetch_related('categories')
    context = {
        'data': categories
    }

    return render(request, 'main/all_categories.html', context=context)
