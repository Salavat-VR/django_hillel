from django import forms
from django.forms import ModelForm, Select, Textarea, TextInput

from .models import Author, Post, Subscriber, Comment


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
    author = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by('name'),
        empty_label='Select an author to follow',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
    )

    class Meta:
        model = Subscriber
        fields = ["subs_name", "email_to", "author"]
        widgets = {
            "subs_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your name, sir/mis",
            }),
            "author": Select(attrs={
                "class": "form-control",
                "placeholder": "Type the id of author you wanna subscribe",
            }),
            "email_to": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email to notify you about author's new articles",
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your name/nickname",
            }),
            "body": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Comment this article",
            }),
        }
