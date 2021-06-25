from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AdminRegistrationForm(ModelForm):
    class Meta:
        model = 'User'
        fields = ['username', 'email', 'password']