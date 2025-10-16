from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import MyUser

class MyRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ['username']
