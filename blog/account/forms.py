from django import forms

from account.models import User, Avatar
from account.tasks import send_confirmation_email


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password", "password_confirmation"]

    def clean(self):
        cleaned_data: dict = super().clean()

        if cleaned_data["password"] != cleaned_data['password_confirmation']:
            self.add_error("password_confirmation", "Password mismatch")
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            self.add_error("email", "This email already in use")
        return email

    def save(self, commit=True):
        instance: User = super().save(commit=False)
        instance.is_active = False

        instance.save()
        send_confirmation_email.apply_async(args=[instance.id], countdown=10)

        return instance


class ChangePasswordForm(forms.ModelForm):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["current_password", "new_password", "confirm_new_password"]

    def clean(self):
        cleaned_data: dict = super().clean()

        if cleaned_data["new_password"] != cleaned_data['confirm_new_password']:
            self.add_error("confirm_new_password", "Password mismatch")

        return cleaned_data


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('file_path',)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def save(self, commit=False):
        instance = super().save(commit=False)
        instance.user = self.request.user
        instance.save()
        return instance
