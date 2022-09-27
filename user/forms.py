from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Passwrod", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modify E-Mail")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Modify your name")
    last_name = forms.CharField(label="Modify your lastname")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}


class AvatarForm(forms.Form):
    image = forms.ImageField(label="avatar")


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = [
            "receiver",
            "msg",
        ]
        widgets = {"msg": forms.Textarea(attrs={"cols": 80})}
