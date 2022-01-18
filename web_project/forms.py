from django import forms
from web_project.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegisterForm(UserCreationForm):
    # we inherite username from UserCreationForm
    # we then add the following extra fields:
    name = forms.CharField(max_length=20, required=True)
    phone_number = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ('name', 'phone_number', 'email','username', 'password1', 'password2',)
