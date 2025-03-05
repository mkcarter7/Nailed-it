# This code was generated with the assistance of ChatGPT
from rest_framework.test import APITestCase
from rest_framework import status
from naileditapi.models import User
from django.urls import reverse

class UserViewSetTest(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com'
        )
        self.url = reverse('user-list')

    def test_create_user(self):
        data = {
            'username': 'newuser',
            'password': 'password123',
            'email': 'newuser@example.com'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertNotIn('password', response.data)  # Ensure password is not returned

    def test_get_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one user in the setup

    def test_get_user(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['email'], self.user.email)

    def test_update_user(self):
        data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com'
        }
        response = self.client.put(reverse('user-detail', args=[self.user.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])

    def test_delete_user(self):
        response = self.client.delete(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify the user has been deleted
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
