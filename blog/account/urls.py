from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path("my_profile/", views.MyProfile.as_view(), name='my_profile'),
    path('my_profile/edit', views.MyProfileEdit.as_view(), name='my_profile_edit'),
    path('my_profile/avatar/create', views.AvatarCreate.as_view(), name='avatar_create'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('activate/<str:confirmation_token>', views.ActivateUserView.as_view(), name='activate_user'),
    path("change_password/", views.ChangePasswordView.as_view(), name='change_password'),


]
