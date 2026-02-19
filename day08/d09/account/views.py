from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token

class MyLogin(LoginView):
    redirect_authenticated_user = False
    template_name = 'account.html'

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({
                "success": True,
                "user": {
                    "username": request.user.username,
                }
            })
        else:
            errors = form.errors
            if "__all__" in errors:
                message = errors["__all__"][0]
            else:
                first_field = list(errors.keys())[0]
                message = errors[first_field][0]
            return JsonResponse({
                "success": False,
                "errors": message,
            }, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class MyLogoutView(LogoutView):
    next_page = '/account'

    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({
                "success": True,
                'csrf_token': get_token(request)
            })
        else:
            return JsonResponse({
                "success": False,
            }, status=400)