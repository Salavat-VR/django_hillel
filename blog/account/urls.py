from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('my_profile/', views.MyProfile.as_view(), name='my_profile'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('activate/<str:confirmation_token>', views.ActivateUserView.as_view(), name='activate_user'),

]
