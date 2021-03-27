from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('It is main page')


def about(request):
    return render(request, 'main/about.html')
