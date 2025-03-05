# This code was generated with the assistance of ChatGPT
from rest_framework.test import APITestCase
from rest_framework import status
from naileditapi.models import Room, Project, Material, Tool, User
from rest_framework import serializers
from django.urls import reverse
from rest_framework.utils import json

class MaterialViewSetTest(APITestCase):

    def setUp(self):
        self.material = Material.objects.create(
            name="Wood",
            description="High-quality wood for construction",
            uid="test_uid_material"
        )
        self.url = reverse('material-list')

    def test_create_material(self):
        data = {
            'name': 'Metal',
            'description': 'Strong and durable metal',
            'uid': 'test_uid_material_2'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Metal')

    def test_get_material(self):
        response = self.client.get(reverse('material-detail', args=[self.material.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Wood')

    def test_update_material(self):
        data = {
            'name': 'Updated Wood',
            'description': 'Updated high-quality wood for construction',
            'uid': 'test_uid_material_updated'
        }
        response = self.client.put(reverse('material-detail', args=[self.material.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Wood')

    def test_delete_material(self):
        response = self.client.delete(reverse('material-detail', args=[self.material.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
