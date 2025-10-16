from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    has_permission = models.BooleanField(default=False)
    can_downvote = models.BooleanField(default=False)
    reputation = models.IntegerField(default=0)
    def __str__(self):
        return self.username

class Tip(models.Model):
    contenu = models.TextField(max_length=1000)
    auteur = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    upvote = models.ManyToManyField(MyUser, related_name='upvote')
    downvote = models.ManyToManyField(MyUser, related_name='downvote')
    