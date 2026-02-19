from django import forms
from django.forms import ModelForm
from .models import Article, UserFavoriteArticle
from django.utils.translation import gettext_lazy as _

class ArticleForm(ModelForm):
    title = forms.CharField(max_length=64, label=_("Title"))
    synopsis = forms.CharField(max_length=312, label=_("Synopsis"))
    content = forms.CharField(widget=forms.Textarea, label=_("Content"))
    class Meta:
        model = Article
        fields = ["title", "synopsis", "content"]

class FavoriteForm(ModelForm):
    class Meta:
        model = UserFavoriteArticle
        fields = []