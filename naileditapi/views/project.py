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
  #SERIALIZER CONVERTS DATA TO JSON  
    try:
      project = Project.objects.get(pk=pk)
      #GETS A SINGLE OBJECT FROM DATA
      serializer = SingleProjectSerializer(project)
      #IF OBJECT IS FOUND SERIALIZES TOOL TO JSON
      return Response(serializer.data)
    #SENDS JSON RESPONSE
    except Project.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    #IF OBJECT DOES NOT EXIST AN ERROR IS SENT
    
  def list(self, request):
    #GET... ALL OJECTS FROM DATABASE. ORM IS ALL
    project = Project.objects.all()
    
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)
  #POST.... REQUESTS
  
  def create(self, request):
    #VALUES FROM DATA/FIXTURES
    project = Project.objects.create(
      name=request.data["name"],
      description=request.data["description"],
      date_started=request.data["date_started"],
      finish_time=request.data["finishe_time"],
      estimated_cost=request.data["estimated_cost"],
      user_id=request.data["user_id"],
      room_id=request.data["room_id"],
      materials=request.data["materials"],
      uid=request.data["uid"]
    )
    if "materials" in request.data:
      project.materials.set(request.data["materials"])  
      #MANYTOMANY
      
    #CREATES NEW OBJECT AND SAVES TO DATABASE
    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  #SERIALIZES AND SHOWS A CREATED 201 STATUS
  
  def update(self, request, pk):
    #PUT...UPDATES OBJECT ATTRIBUTES
    id = pk
    project = Project.objects.get(pk=pk)
    project.name=request.data["name"]
    project.description = request.data["description"]
    project.date_started = request.data["date_started"]
    project.finish_time = request.data["finish_time"]
    project.estimated_cost = request.data["estimated_cost"]
    project.user_id = request.data["user_id"]
    project.room_id = request.data["room_id"]
    project.materials = request.data["materials"]
    project.uid = request.data["uid"]
    
    project.save()
    #SAVES UPDATE TO DATABASE
    
    #MANYTOMANY
    if "materials" in request.data:
      project.materials.set(request.data["materials"])  
      
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
    fields = ('id', 'name', 'description', 'date_started', 'finish_time', 'estimated_cost', 'user_id', 'room_id', 'materials', 'uid')
    
class SingleProjectSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Project
    fields = ('id', 'name', 'description', 'date_started', 'finish_time', 'estimated_cost', 'user_id', 'room_id', 'materials', 'uid')
    depth = 1
