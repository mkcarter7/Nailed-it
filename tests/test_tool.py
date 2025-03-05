# This code was generated with the assistance of ChatGPT
from rest_framework.test import APITestCase
from rest_framework import status
from naileditapi.models import Tool
from django.urls import reverse

class ToolViewSetTest(APITestCase):

    def setUp(self):
        # Set up test data for tools
        self.tool_1 = Tool.objects.create(name="Hammer", description="For hammering nails", uid="test_tool_uid_1")
        self.tool_2 = Tool.objects.create(name="Saw", description="For cutting wood", uid="test_tool_uid_2")
        self.url = reverse('tool-list')

    def test_create_tool(self):
        data = {
            'name': 'Drill',
            'description': 'For drilling holes',
            'uid': 'test_tool_uid_3',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Drill')
        self.assertEqual(response.data['description'], 'For drilling holes')
        self.assertEqual(response.data['uid'], 'test_tool_uid_3')

    def test_get_tools(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Since we have two tools in the setup

    def test_get_tool(self):
        response = self.client.get(reverse('tool-detail', args=[self.tool_1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Hammer')
        self.assertEqual(response.data['description'], 'For hammering nails')
        self.assertEqual(response.data['uid'], 'test_tool_uid_1')

    def test_update_tool(self):
        data = {
            'name': 'Updated Hammer',
            'description': 'For hammering nails with more precision',
            'uid': 'updated_tool_uid_1',
        }
        response = self.client.put(reverse('tool-detail', args=[self.tool_1.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Hammer')
        self.assertEqual(response.data['description'], 'For hammering nails with more precision')
        self.assertEqual(response.data['uid'], 'updated_tool_uid_1')

    def test_delete_tool(self):
        response = self.client.delete(reverse('tool-detail', args=[self.tool_1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify it has been deleted
        response = self.client.get(reverse('tool-detail', args=[self.tool_1.id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
