from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from account.forms import UserRegistrationForm
from account.models import User


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
