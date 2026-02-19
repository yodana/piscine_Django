from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    favourites = models.ManyToManyField('blog.Article', through='blog.UserFavoriteArticle', related_name='favourites')
    def __str__(self):
        return self.username
