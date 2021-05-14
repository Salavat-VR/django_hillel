from django.urls import reverse_lazy
from django.views.generic import UpdateView

from account.models import User


class MyProfile(UpdateView):
    queryset = User.objects.filter(is_active=True)
    fields = ("first_name", "last_name")
    success_url = reverse_lazy('home_page')
