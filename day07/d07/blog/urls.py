from django.contrib import admin
from django.urls import path, include
from .views import ArticleView, PublicationView, ArticleDetailView, FavoriteView, PublishView

urlpatterns = [
    path('',  ArticleView.as_view(), name='articles'),
    path('publication/',PublicationView.as_view(), name='publication' ),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('favorite/', FavoriteView.as_view(), name='favorite'),
    path('publish/', PublishView.as_view(), name='publish')
]
