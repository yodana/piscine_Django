from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib import messages
from users.models import MyUser
from .forms import MyRegisterForm

class MyLogin(LoginView):
    redirect_authenticated_user = True

class MyLogoutView(LogoutView):
    next_page = '/'

class MyRegister(CreateView):
    model = MyUser
    form_class = MyRegisterForm
    template_name = 'register.html'
