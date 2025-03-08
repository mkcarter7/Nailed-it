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
            project_id = request.data.get("project")  
            tool_id = request.data.get("tool")

            if project_id is None or tool_id is None:
                return Response({"message": "Both project and tool are required."}, status=status.HTTP_400_BAD_REQUEST)

            project = Project.objects.get(id=project_id)
            tool = Tool.objects.get(id=tool_id)

        except Project.DoesNotExist:
            return Response({"message": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
        except Tool.DoesNotExist:
            return Response({"message": "Tool not found."}, status=status.HTTP_404_NOT_FOUND)

        project_tool = ProjectTool.objects.create(
            project=project,
            tool=tool
        )

        serializer = ProjectToolSerializer(project_tool)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        try:
            projecttool = ProjectTool.objects.get(pk=pk)
            
            project = Project.objects.get(pk=request.data["project"])
            tool = Tool.objects.get(pk=request.data["tool"])

            if not project or not tool:
                return Response({"message": "Both project and tool are required."}, status=status.HTTP_400_BAD_REQUEST)

            projecttool.project = project
            projecttool.tool = tool
            projecttool.save()

            serializer = ProjectToolSerializer(projecttool)
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
            projecttools = ProjectTool.objects.get(pk=pk)
            projecttools.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ProjectTool.DoesNotExist:
            return Response({'message': 'ProjectTool not found'}, status=status.HTTP_404_NOT_FOUND)


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ('id', 'name', 'description')
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description')

class ProjectToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTool
        fields = ('id', 'tool', 'project' )
        depth = 1
