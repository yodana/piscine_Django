from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ex01/django',  views.django, name='django'),
    path('ex01/template',  views.template, name='template'),
    path('ex01/affichage',  views.affichage, name='affichage'),
]
