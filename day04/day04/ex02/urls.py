from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ex02',  views.ex02, name='ex02'),
]
