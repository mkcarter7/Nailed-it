# This code was generated with the assistance of ChatGPT
from rest_framework.test import APITestCase
from rest_framework import status
from naileditapi.models import Room, Project, Material, Tool, User
from rest_framework import serializers
from django.urls import reverse
from rest_framework.utils import json

class ProjectViewSetTest(APITestCase):

    def setUp(self):
        self.room = Room.objects.create(
            name="Living Room",
            description="A spacious living room",
            image="http://example.com/image.jpg",
            uid="test_uid_1"
        )
        self.project = Project.objects.create(
            name="Project 1",
            description="A renovation project",
            date_started="2025-03-01T10:00:00Z",
            finish_time="2025-03-10T10:00:00Z",
            estimated_cost=5000,
            room=self.room,
            uid="test_project_uid",
            materials="Wood, Metal"
        )
        self.url = reverse('project-list')

    def test_create_project(self):
        data = {
            'name': 'Project 2',
            'description': 'A new construction project',
            'date_started': '2025-04-01T10:00:00Z',
            'finish_time': '2025-04-10T10:00:00Z',
            'estimated_cost': 10000,
            'room': self.room.id,
            'uid': 'test_project_uid_2',
            'materials': 'Concrete, Steel'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Project 2')

    def test_get_project(self):
        response = self.client.get(reverse('project-detail', args=[self.project.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Project 1')

    def test_update_project(self):
        data = {
            'name': 'Updated Project 1',
            'description': 'An updated renovation project',
            'date_started': '2025-03-01T10:00:00Z',
            'finish_time': '2025-03-15T10:00:00Z',
            'estimated_cost': 5500,
            'room': self.room.id,
            'uid': 'test_project_uid_updated',
            'materials': 'Wood, Concrete'
        }
        response = self.client.put(reverse('project-detail', args=[self.project.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Project 1')

    def test_delete_project(self):
        response = self.client.delete(reverse('project-detail', args=[self.project.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
