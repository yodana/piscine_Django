from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import MyUser
from django.utils.translation import gettext_lazy as _

class MyRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label=_("Username"))
    password1 = forms.CharField(widget=forms.PasswordInput, label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_("Password confirmation"))
    class Meta:
        model = MyUser
        fields = ['username']
