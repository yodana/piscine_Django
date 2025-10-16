from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, UserFavoriteArticle
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class ArticleView(ListView):
    model = Article

@method_decorator(login_required, name='dispatch') #applique le decorator a la method dispatch
class PublicationView(ListView):
    model = Article
    template_name = 'blog/publication_list.html'
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

@method_decorator(login_required, name='dispatch') #applique le decorator a la method dispatch
class FavoriteView(ListView):
    model = UserFavoriteArticle
    template_name = 'blog/favorite_list.html'
    def get_queryset(self):
        return UserFavoriteArticle.objects.filter(user=self.request.user)
