from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="name", max_length=100, widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),label="password", max_length=100)
    verif_password = forms.CharField(widget=forms.PasswordInput(attrs={
     'class': 'form-control' 
     }), label="verif password", max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100, widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }), max_length=100)

class TipForm(forms.Form):
    contenu = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control',
        }), label="Contenu", max_length=1000)