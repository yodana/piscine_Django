from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.init, name='init'),
    path('register',  views.register, name='register'),
    path('login',  views.mylogin, name='login'),
    path('logout',  views.mylogout, name='logout'),
    path('delete/<int:id>',  views.mydelete, name='delete'),
    path('upvote/<int:id>',  views.upvote, name='upvote'),
    path('downvote/<int:id>',  views.downvote, name='downvote'),
]
