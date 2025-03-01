"""View module for handling requests about types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from naileditapi.models.room import Room

class RoomView(ViewSet):
  #GETS A SINGLE OBJECT FROM THE DB BASED ON THE PK IN THE URL
  #USE ORM TO GET DATA
  def retrieve(self, request, pk):
  #SERIALIZER CONVERTS DATA TO JSON  
    try:
      room = Room.objects.get(pk=pk)
      serializer = SingleRoomSerializer(room)
      return Response(serializer.data)
    except Room.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    #GET ALL OJECTS FROM DATABASE. ORM IS ALL
    rooms = Room.objects.all()
    
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)
  #POST REQUESTS
  def create(self, request):
    #VALUES FROM CLIENT/FIXTURES
    room = Room.objects.create(
      name=request.data["name"],
      description=request.data["description"],
      image=request.data["image"],
      uid=request.data["uid"]
    )
    serializer = RoomSerializer(room)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    
    id = pk
    room = Room.objects.get(pk=pk)
    room.name=request.data["name"]
    room.description = request.data["description"]
    room.image = request.data["image"]
    room.uid = request.data["uid"]
    
    room.save()
    
    serializer = RoomSerializer(room)    
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    
    room = Room.objects.get(pk=pk)
    room.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  #SERIALIZER CLASS DETERMINES HOW PYTHON DATA SHOULD BE SERIALIZED TO BE SENT BACK TO CLIENT
class RoomSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Room
    fields = ('id', 'name', 'description', 'image', 'uid')
    
class SingleRoomSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Room
    fields = ('id', 'name', 'description', 'image', 'uid')
    depth = 1
