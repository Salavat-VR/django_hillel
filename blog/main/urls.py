from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('about', views.about, name='about_page'),
    path('post', views.post, name='posts_page'),
    path('post/create', views.post_create, name='create_post')
]
