from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('my_profile/', views.MyProfile.as_view(), name='my_profile'),

]
