from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login(self):
        login_url = reverse('login') 
        response = self.client.post(login_url, {'username': self.username, 'password': self.password})

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)


    def test_login_with_wrong_credentials(self):
        login_url = reverse('login')  
        response = self.client.post(login_url, {'username': 'wronguser', 'password': 'wrongpassword'})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)


