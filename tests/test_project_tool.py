# This code was generated with the assistance of ChatGPT
from rest_framework.test import APITestCase
from rest_framework import status
from naileditapi.models import Project, Tool, ProjectTool, Room
from django.urls import reverse

class ProjectToolViewSetTest(APITestCase):
    
    def setUp(self):
        # Create room and project
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

        # Create tools
        self.tool_1 = Tool.objects.create(name="Hammer", description="For hammering nails", uid="test_tool_uid_1")
        self.tool_2 = Tool.objects.create(name="Saw", description="For cutting wood", uid="test_tool_uid_2")

        # Create project-tool relationship (ProjectTool)
        self.project_tool_1 = ProjectTool.objects.create(project=self.project, tool=self.tool_1)
        self.project_tool_2 = ProjectTool.objects.create(project=self.project, tool=self.tool_2)

        self.url = reverse('projecttools-list')

    def test_create_project_tool(self):
        data = {
            'project_id': self.project.id,
            'tool_id': self.tool_1.id,  # Ensure we're sending 'tool_id' here
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['project']['id'], self.project.id)
        self.assertEqual(response.data['tool']['id'], self.tool_1.id)

    def test_get_project_tools(self):
        response = self.client.get(reverse('projecttools-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two tools should be linked to the project

    def test_get_project_tool(self):
        response = self.client.get(reverse('projecttools-detail', args=[self.project_tool_1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tool']['id'], self.tool_1.id)  # Compare the tool ID
        self.assertEqual(response.data['project']['id'], self.project.id)  # Compare the project ID

    def test_update_project_tool(self):
        data = {
            'project_id': self.project.id,
            'tool_id': self.tool_2.id,  # Update to link the project to a different tool
        }
        response = self.client.put(reverse('projecttools-detail', args=[self.project_tool_1.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tool']['id'], self.tool_2.id)  # Compare the updated tool ID

    def test_delete_project_tool(self):
        response = self.client.delete(reverse('projecttools-detail', args=[self.project_tool_1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify it has been deleted
        response = self.client.get(reverse('projecttools-detail', args=[self.project_tool_1.id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
