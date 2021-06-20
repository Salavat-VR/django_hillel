from django import forms

from account.models import User


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
        #  todo: send email
        return instance
