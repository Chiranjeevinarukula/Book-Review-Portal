from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class SignUpTestCases(TestCase):
    def test_signup_get(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'form')
    
    def test_signup_post(self):
        data = {
            'username':'testuser',
            'email':'nchiru@gmail.com',
            'password1':'test@@@@',
            'password2':'test@@@@'
        }
        response = self.client.post(reverse('signup'),data)
        self.assertEqual(response.status_code,302)
        self.assertTrue(User.objects.get(username='tesetuser'))
    
    def test_signup_view_post_existing_username(self):
        data = {
            'username':'testuser',
            'email':'nchiru@gmail.com',
            'password1':'test@@@@',
            'password2':'test@@@@'
        }
        response = self.client.post(reverse('signup'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A user with that username already exists.')
    