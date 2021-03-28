from django.forms import ModelForm, TextInput, Textarea

from .models import Post


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
