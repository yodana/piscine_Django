from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    favourites = models.ManyToManyField('blog.UserFavoriteArticle', related_name='favourite')
    def __str__(self):
        return self.username
