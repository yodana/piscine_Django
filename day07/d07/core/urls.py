from django.urls import path
from .views import MyLogin, MyLogoutView, MyRegister

urlpatterns = [
    path('login/', MyLogin.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', MyRegister.as_view(), name='register'),
]