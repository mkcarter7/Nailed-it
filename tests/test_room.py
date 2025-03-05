# This code was generated with the assistance of ChatGPT
from rest_framework.test import APITestCase
from rest_framework import status
from naileditapi.models import Room
from rest_framework import serializers
from django.urls import reverse
from rest_framework.utils import json

class RoomViewSetTest(APITestCase):
    
    def setUp(self):
        self.room = Room.objects.create(
            name="Living Room",
            description="A spacious living room",
            image="http://example.com/image.jpg",
            uid="test_uid_1"
        )
        self.url = reverse('room-list')

    def test_create_room(self):
        data = {
            'name': 'Kitchen',
            'description': 'A modern kitchen',
            'image': 'http://example.com/kitchen.jpg',
            'uid': 'test_uid_2'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Kitchen')

    def test_get_room(self):
        response = self.client.get(reverse('room-detail', args=[self.room.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Living Room')

    def test_update_room(self):
        data = {
            'name': 'Updated Living Room',
            'description': 'A spacious updated living room',
            'image': 'http://example.com/updated_living_room.jpg',
            'uid': 'test_uid_1_updated'
        }
        response = self.client.put(reverse('room-detail', args=[self.room.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Living Room')

    def test_delete_room(self):
        response = self.client.delete(reverse('room-detail', args=[self.room.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
