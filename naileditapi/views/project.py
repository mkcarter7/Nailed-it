"""View module for handling requests about types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from naileditapi.models.project import Project
from naileditapi.models.room import Room

class ProjectView(ViewSet):
    # GETS A SINGLE OBJECT FROM THE DB BASED ON THE PK IN THE URL
    # USE ORM TO GET DATA
    # API ENDPOINTS GET GENERATED
    def retrieve(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            serializer = SingleProjectSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({'message': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

    # GET... ALL OBJECTS FROM DATABASE. ORM IS ALL
    def list(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    # POST.... REQUESTS
    def create(self, request):
        name = request.data.get("name")
        description = request.data.get("description")
        date_started = request.data.get('date_started')
        finish_time = request.data.get('finish_time')
        estimated_cost = request.data.get('estimated_cost')
        room = request.data.get('room')  # room should be fetched from the request
        materials = request.data.get('materials')
        uid = request.data.get("uid")

        if not all([name, description, date_started, finish_time, estimated_cost, room, materials, uid]):
            return Response(
                {"error": "Fields 'name', 'description', date_started, finish_time, estimated_cost, room, materials and 'uid' are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Retrieve the Room instance from the database using the ID
        try:
            room = Room.objects.get(id=room)
        except Room.DoesNotExist:
            return Response({"error": "Room not found."}, status=status.HTTP_404_NOT_FOUND)

        # Create the project instance
        project = Project.objects.create(
            name=name,
            description=description,
            date_started=date_started,
            finish_time=finish_time,
            estimated_cost=estimated_cost,
            room=room,  # Use the Room instance, not the ID
            materials=materials,
            uid=uid
        )

        # Serialize and return the created project
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Update method to handle project updates
    def update(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'message': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update project fields, fetch room instance if room_ is provided
        project.name = request.data.get("name", project.name)
        project.description = request.data.get("description", project.description)
        project.date_started = request.data.get("date_started", project.date_started)
        project.finish_time = request.data.get("finish_time", project.finish_time)
        project.estimated_cost = request.data.get("estimated_cost", project.estimated_cost)

        room = request.data.get("room", None)
        if room:
            try:
                room = Room.objects.get(id=room)
                project.room = room  # Assign the Room instance
            except Room.DoesNotExist:
                return Response({"error": "Room not found."}, status=status.HTTP_404_NOT_FOUND)

        project.materials = request.data.get("materials", project.materials)
        project.uid = request.data.get("uid", project.uid)

        # Save the project instance
        project.save()

        # Serialize and return the updated project
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # DELETE....FETCHES THE OBJECT FROM DATABASE AND DELETES
    def destroy(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            project.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response({'message': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)


# SERIALIZER CLASS DETERMINES HOW PYTHON DATA SHOULD BE SERIALIZED TO BE SENT BACK TO CLIENT
class ProjectSerializer(serializers.ModelSerializer):
    # CONVERTS OBJECT TO JSON
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'date_started', 'finish_time', 'estimated_cost', 'room', 'materials', 'uid')


class SingleProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'date_started', 'finish_time', 'estimated_cost', 'room', 'materials', 'uid')
        depth = 1
