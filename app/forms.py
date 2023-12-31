from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
        ]


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "header",
            "platform",
        ]
