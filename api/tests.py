from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Contact

User = get_user_model()

class UserTests(APITestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpass123',
            'phone_number': '1234567890'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.client.login(username='testuser', password='testpass123')

    def test_create_user(self):
        url = reverse('user-list')
        response = self.client.post(url, {
            'username': 'newuser',
            'password': 'newpassword',
            'phone_number': '9876543210'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_obtain_token(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_mark_contact_as_spam(self):
        contact = Contact.objects.create(user=self.user, name='Test Contact', phone_number='1234567891')
        url = reverse('contact-mark-as-spam', args=[contact.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        contact.refresh_from_db()
        self.assertTrue(contact.is_spam)

    def test_search_user_by_name(self):
        url = reverse('user_search') + '?q=testuser'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
