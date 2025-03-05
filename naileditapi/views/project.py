"""View module for handling requests about types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from naileditapi.models.project import Project

class ProjectView(ViewSet):
  #GETS A SINGLE OBJECT FROM THE DB BASED ON THE PK IN THE URL
  #USE ORM TO GET DATA
  #API ENDPOINTS GET GENERATED
  def retrieve(self, request, pk):
    try:
        project = Project.objects.get(pk=pk)
        serializer = SingleProjectSerializer(project)
        return Response(serializer.data)
    except Project.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    #GET... ALL OJECTS FROM DATABASE. ORM IS ALL
    project = Project.objects.all()
    
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)
  #POST.... REQUESTS
  
  def create(self, request):
    name = request.data.get("name")
    description = request.data.get("description")
    date_started = request.data.get('date_started')
    finish_time = request.data.get('finish_time')
    estimated_cost = request.data.get('estimated_cost')
    room = request.data.get('room')
    materials = request.data.get('materials')
    uid = request.data.get("uid")
    
    if not all([name, description, date_started, finish_time, estimated_cost, room, materials, uid]):
        return Response(
            {"error": "Fields 'name', 'description', date_started, finish_time, estimated_cost, room, mateirals and 'uid' are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    project = Project.objects.create(
        name=name,
        description=description,
        date_started=date_started,
        finish_time=finish_time,
        estimated_cost=estimated_cost,
        room=room,
        materials=materials,
        uid=uid
    )
    #CREATES NEW OBJECT AND SAVES TO DATABASE
    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  #SERIALIZES AND SHOWS A CREATED 201 STATUS
  
  def update(self, request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'message': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
    
    project.name=request.data.get("name", project.name)
    project.description=request.data.get("description", project.description)
    project.date_started=request.data.get("date_started", project.date_started)
    project.finish_time=request.data.get("finish_time", project.finish_time)
    project.estimated_cost=request.data.get("estimated_cost", project.estimated_cost)
    project.room=request.data.get("room", project.room)
    project.materials=request.data.get("materials", project.materials)
    project.uid=request.data.get("uid", project.uid)

    project.save()
    
    serializer = ProjectSerializer(project)    
    return Response(serializer.data, status=status.HTTP_200_OK)
    
  def destroy(self, request, pk):
    #DELETE....FETCHES THE OBJECT FROM DATABASE AND DELETES
    project = Project.objects.get(pk=pk)
    project.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  #RETURNS 204/SUCCESSFUL DELETION
  #SERIALIZER CLASS DETERMINES HOW PYTHON DATA SHOULD BE SERIALIZED TO BE SENT BACK TO CLIENT
class ProjectSerializer(serializers.ModelSerializer):
  #CONVERTS OBJECT TO JSON
  class Meta:
    model = Project
    fields = ('id', 'name', 'description', 'date_started', 'finish_time', 'estimated_cost', 'room_id', 'materials', 'uid')
    
class SingleProjectSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Project
    fields = ('id', 'name', 'description', 'date_started', 'finish_time', 'estimated_cost', 'room_id', 'materials', 'uid')
    depth = 1
