from django.conf import settings
from .models import MyLogin

def login(request):
    return {'login_form': MyLogin().get_form_class()}