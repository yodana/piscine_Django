from django.conf import settings
from core.models import MyLogin

def login(request):
    return {'login': MyLogin().get_form_class()}