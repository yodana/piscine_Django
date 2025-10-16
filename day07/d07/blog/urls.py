from django.contrib import admin
from django.urls import path, include
from .views import ArticleView, PublicationView, ArticleDetailView, FavoriteView

urlpatterns = [
    path('',  ArticleView.as_view(), name='article'),
    path('publication/',PublicationView.as_view(), name='article' ),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('favorite/', FavoriteView.as_view(), name='favorite')
]
