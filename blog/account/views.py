from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView

from account.forms import UserRegistrationForm, ChangePasswordForm, AvatarForm
from account.models import User, Avatar


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.filter(is_active=True)
    fields = ("first_name", "last_name")
    success_url = reverse_lazy('home_page')

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(CreateView):
    queryset = User.objects.filter(is_active=True)
    form_class = UserRegistrationForm
    template_name = 'account/user_sign_up.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        return super().form_valid(form)


class ActivateUserView(View):
    def get(self, request, confirmation_token):
        user = get_object_or_404(User, confirmation_token=confirmation_token)
        user.is_active = True
        user.save(update_fields=("is_active",))
        return redirect("home_page")


class ChangePasswordView(CreateView):
    queryset = User.objects.filter(is_active=True)
    form_class = ChangePasswordForm
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('home_page')


class AvatarCreate(LoginRequiredMixin, CreateView):
    model = Avatar
    form_class = AvatarForm
    success_url = reverse_lazy('home_page')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(request=self.request, **self.get_form_kwargs())

