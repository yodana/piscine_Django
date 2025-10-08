from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ex03',  views.ex03, name='ex03'),
]
