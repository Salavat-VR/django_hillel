from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('about', views.about, name='about_page'),

    url(r'^favicon', RedirectView.as_view(
        url='main/static/imgs/favicon/my_favicon.ico')),

    path('post', views.post, name='posts_page'),
    path('post/create', views.post_create, name='post_create'),
    path('post/show/<int:post_id>', views.post_show, name='post_show'),

    path('post/update/<int:post_id>', views.post_update, name='post_update'),
    path('api/posts', views.post_api, name='api_posts'),

    path('api/subscribe', views.api_subscribe, name='api_subscribe'),
    path('api/all_subs', views.all_subs, name='all_subs'),

    path('api/all_authors', views.all_authors, name='all_authors'),
    path('author/generate', views.author_generate, name='author_generate')