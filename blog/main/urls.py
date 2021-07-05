from django.conf.urls import url
from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('about', views.about, name='about_page'),

    url(r'^favicon', RedirectView.as_view(
        url='main/static/imgs/favicon/my_favicon.ico')),

    path('post', cache_page(60 * 15)(views.PostListView.as_view()), name='post_lists'),
    path('post/create', views.post_create, name='post_create'),
    path('post/show/<int:post_id>', views.post_show, name='post_show'),
    path('post/xlsx', views.PostXlsx.as_view(), name='load_posts_via_xlsx'),

    path('post/update/<int:post_id>', views.post_update, name='post_update'),
    path('api/posts', views.post_api, name='api_posts'),

    path('api/subscribe', views.api_subscribe, name='api_subscribe'),
    path('api/all_subs', views.all_subs, name='all_subs'),

    path('api/all_authors', cache_page(60 * 15)(views.all_authors), name='all_authors'),
    path('author/generate', views.author_generate, name='author_generate'),

    path('books/all', views.all_books, name='all_books'),
    path('categories/all', cache_page(60 * 15)(views.all_categories), name='all_categories'),

    path('contact-us', views.ContactUsView.as_view(), name='contact-us'),
    path('post/delete/<int:post_id>', views.PostDeleteView.as_view(), name='post_delete'),
    path(r'author/delete/<int:author_id>', views.AuthorDeleteView.as_view(), name='author_delete'),

    path('author/show/<int:author_id>', views.author_show, name='author_show'),
    path('api/v1/', include('api.urls'))
]
