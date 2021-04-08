from django.forms import ModelForm, Textarea, TextInput

from .models import Post, Subscriber


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "content"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "The title of your masterpiece",
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Description",
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Paste or Write it here :) ",
            }),
        }


class SubsForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email_to", "author"]
        widgets = {
            "email_to": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email to notify you about author's new articles",
            }),
            "author": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Type the id of author you wanna subscribe",
            }),
        }
