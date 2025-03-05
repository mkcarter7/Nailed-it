# This code was generated with the assistance of ChatGPT
from rest_framework.test import APITestCase
from rest_framework import status
from naileditapi.models.user import User

class UserTests(APITestCase):

    def setUp(self):
        """Set up test data"""
        self.user1 = User.objects.create(uid="12345", name="John Doe", email="john@example.com")
        self.user2 = User.objects.create(uid="67890", name="Jane Doe", email="jane@example.com")

    def test_list_users(self):
        """Test retrieving the list of users"""
        response = self.client.get("/users")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_users_with_uid_filter(self):
        """Test retrieving users filtered by uid"""
        response = self.client.get(f"/users?uid={self.user1.uid}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['uid'], self.user1.uid)

    def test_retrieve_user(self):
        """Test retrieving a single user by id"""
        response = self.client.get(f"/users/{self.user1.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.user1.name)
        self.assertEqual(response.data["email"], self.user1.email)

    def test_retrieve_non_existent_user(self):
        """Test retrieving a user that does not exist"""
        response = self.client.get("/users/999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_user(self):
        """Test deleting a user"""
        response = self.client.delete(f"/users/{self.user1.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify user is deleted
        response = self.client.get(f"/users/{self.user1.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

