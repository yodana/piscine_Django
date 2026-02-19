from django.db import models
from django.contrib.auth.views import LoginView

class MyLogin(LoginView):
    redirect_authenticated_user = True
    