from django.test import TestCase, Client
from users.models import MyUser
from blog.models import Article, UserFavoriteArticle
from django.urls import reverse
from django.utils.translation import activate

class ArticleViewTests(TestCase):
    def setUp(self):
        # Create a user for authentication
        activate('en') # pour bien dire que /en/ est la langue et le bon chemin
        self.user = MyUser.objects.create_user(username='testuser', password='pass')
        self.article = Article.objects.create(title='test', author=self.user, content='test')

    def test_authorize_pages_not_logged(self):
        response = self.client.get(reverse('publication'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('favorite'))
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('publish'))
        self.assertEqual(response.status_code, 302)

    def test_authorize_pages_logged(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('publication'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('favorite'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('publish'))
        self.assertEqual(response.status_code, 200)

    def test_authorize_pages_not_logged_form(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('register'), {'username': 'testuser', 'password1': 'password123', 'password2': 'password123'})
        self.assertEqual(response.status_code, 302)

    def test_favorite_twice(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('article', kwargs={'pk': self.article.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.favourites.count(), 1)
        response = self.client.post(reverse('article', kwargs={'pk': self.article.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.favourites.count(), 1)