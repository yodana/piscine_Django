from . import views
from django.urls import path

urlpatterns = [
    path('', views.ShowsRoom, name='show-room'),
    path('<str:room_name>/', views.MessageView, name='room'),
]