from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib import messages
from users.models import MyUser
from .forms import MyRegisterForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from .utils import user_is_auth

class MyLogin(LoginView):
    redirect_authenticated_user = True

class MyLogoutView(LogoutView):
    next_page = '/'

@method_decorator(user_passes_test(user_is_auth, login_url="/"), name='dispatch')
class MyRegister(CreateView):
    model = MyUser
    form_class = MyRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')