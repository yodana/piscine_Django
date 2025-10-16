from django.urls import path
from . import views

urlpatterns = [
    path('', views.ex01, name='ex01'),
]