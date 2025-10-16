from django import forms
from django.forms import ModelForm
from .models import Article, UserFavoriteArticle

class ArticleForm(ModelForm):
    title = forms.CharField(max_length=64)
    class Meta:
        model = Article
        fields = ["title", "synopsis", "content"]

class FavoriteForm(ModelForm):
    class Meta:
        model = UserFavoriteArticle
        fields = []