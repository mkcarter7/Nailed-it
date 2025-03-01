from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from naileditapi.models.room import Room
from naileditapi.models.project_tool import ProjectTool
from naileditapi.models.tool import Tool
from naileditapi.models.project import Project


class ProjectToolView(ViewSet):
    """ types view"""

    def retrieve(self, request, pk):
      try:
          projectTool = ProjectTool.objects.get(pk=pk)
          serializer = ProjectToolSerializer(projectTool)
          return Response(serializer.data)
      except ProjectTool.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
      try:
        projectTools = ProjectTool.objects.all()
    
        serializer = ProjectToolSerializer(projectTools, many=True)
        return Response(serializer.data)
      except:
        return Response({'message': 'Check query'}, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request):
      try:
        projectId = Project.objects.get(pk=request.data["project_id"])
        toolId = Tool.objects.get(pk=request.data["tool_id"])
      except Tool.DoesNotExist:
        return Response({"message": "Tool not found."}, status=status.HTTP_404_NOT_FOUND)
      except Tool.DoesNotExist:
            return Response({"message": "Tool not found."}, status=status.HTTP_404_NOT_FOUND)

      projectTool = ProjectTool.objects.create(
          tool=toolId,
          project=projectId,
      )
      serializer = ProjectToolSerializer(projectTool)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """PUT - Update a project-tool relation"""
        try:
            project_tool = ProjectTool.objects.get(pk=pk)
            project = Project.objects.get(pk=request.data["project_id"])
            tool = Tool.objects.get(pk=request.data["tool_id"])

            project_tool.project = project
            project_tool.tool = tool
            project_tool.save()

            serializer = ProjectToolSerializer(project_tool)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProjectTool.DoesNotExist:
            return Response({"message": "ProjectTool not found."}, status=status.HTTP_404_NOT_FOUND)
        except Project.DoesNotExist:
            return Response({"message": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
        except Tool.DoesNotExist:
            return Response({"message": "Tool not found."}, status=status.HTTP_404_NOT_FOUND)

    
    
    def destroy(self, request, pk):
        """DELETE - Remove a project-tool relation"""
        try:
            project_tool = ProjectTool.objects.get(pk=pk)
            project_tool.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ProjectTool.DoesNotExist:
            return Response({'message': 'ProjectTool not found'}, status=status.HTTP_404_NOT_FOUND)

class ProjectToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTool
        fields = ('id', 'tool', 'project' )
        depth = 1
