from django.contrib.auth.admin import UserAdmin
from .models import Article, UserFavoriteArticle
from users.models import MyUser
from django.contrib import admin

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content')

@admin.register(UserFavoriteArticle)
class FavoriteArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'article')