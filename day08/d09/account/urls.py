from django.contrib import admin
from django.urls import path, include
from .views import MyLogin, MyLogoutView

urlpatterns = [
    path('', MyLogin.as_view(), name='account'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]
