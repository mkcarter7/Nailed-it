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
    name = request.data.get("name")
    description = request.data.get("description")
    image = request.data.get("image")
    uid = request.data.get("uid")

    if not all([name, description, uid]):
        return Response(
            {"error": "Fields 'name', 'description', 'image' and 'uid' are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    room = Room.objects.create(
        name=name,
        description=description,
        image=image,
        uid=uid
    )
    serializer = RoomSerializer(room)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    room = Room.objects.get(pk=pk)

    room.name = request.data.get("name", room.name)
    room.description = request.data.get("description", room.description)
    room.image = request.data.get('image', room.image)
    room.uid = request.data.get("uid", room.uid)
    
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
