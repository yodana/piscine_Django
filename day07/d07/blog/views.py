from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Article, UserFavoriteArticle
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import ArticleForm, FavoriteForm
# Create your views here.
class ArticleView(ListView):
    model = Article
    
    def get_queryset(self):
        return Article.objects.filter().order_by('-created')

@method_decorator(login_required, name='dispatch') #applique le decorator a la method dispatch
class PublicationView(ListView):
    model = Article
    template_name = 'blog/publication_list.html'
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).order_by('-created')

@method_decorator(login_required, name='dispatch') #applique le decorator a la method dispatch
class ArticleDetailView(CreateView, DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    form_class = FavoriteForm
    success_url = reverse_lazy('favorite')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article = self.get_object()
        if UserFavoriteArticle.objects.filter(user=self.request.user, article=self.get_object()).exists():
            return redirect('article', pk=self.get_object().id)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch') #applique le decorator a la method dispatch
class FavoriteView(ListView):
    model = UserFavoriteArticle
    template_name = 'blog/favorite_list.html'
    def get_queryset(self):
        return self.request.user.favourites.all()
    
@method_decorator(login_required, name='dispatch') #applique le decorator a la method dispatch
class PublishView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/publish.html'
    success_url = reverse_lazy('publication')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)