"""View module for handling requests about types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from naileditapi.models.tool import Tool

class ToolView(ViewSet):
  #GETS A SINGLE OBJECT FROM THE DB BASED ON THE PK IN THE URL
  #USE ORM TO GET DATA
  #API ENDPOINTS GET GENERATED
  def retrieve(self, request, pk):
  #SERIALIZER CONVERTS DATA TO JSON  
    try:
      tool = Tool.objects.get(pk=pk)
      #GETS A SINGLE OBJECT FROM DATA
      serializer = SingleToolSerializer(tool)
      #IF OBJECT IS FOUND SERIALIZES TOOL TO JSON
      return Response(serializer.data)
    #SENDS JSON RESPONSE
    except Tool.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    #IF OBJECT DOES NOT EXIST AN ERROR IS SENT
    
  def list(self, request):
    #GET... ALL OJECTS FROM DATABASE. ORM IS ALL
    tool = Tool.objects.all()
    
    serializer = ToolSerializer(tool, many=True)
    return Response(serializer.data)
  #POST.... REQUESTS
  
  def create(self, request):
    name = request.data.get("name")
    description = request.data.get("description")
    uid = request.data.get("uid")

    if not all([name, description, uid]):
        return Response(
            {"error": "Fields 'name', 'description', and 'uid' are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    tool = Tool.objects.create(
        name=name,
        description=description,
        uid=uid
    )
    #CREATES NEW OBJECT AND SAVES TO DATABASE
    serializer = ToolSerializer(tool)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  #SERIALIZES AND SHOWS A CREATED 201 STATUS
  
  def update(self, request, pk):
    tool = Tool.objects.get(pk=pk)

    tool.name = request.data.get("name", tool.name)
    tool.description = request.data.get("description", tool.description)
    tool.uid = request.data.get("uid", tool.uid)

    serializer = ToolSerializer(tool)    
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    #DELETE....FETCHES THE OBJECT FROM DATABASE AND DELETES
    tool = Tool.objects.get(pk=pk)
    tool.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  #RETURNS 204/SUCCESSFUL DELETION
  #SERIALIZER CLASS DETERMINES HOW PYTHON DATA SHOULD BE SERIALIZED TO BE SENT BACK TO CLIENT
class ToolSerializer(serializers.ModelSerializer):
  #CONVERTS OBJECT TO JSON
  class Meta:
    model = Tool
    fields = ('id', 'name', 'description', 'uid')
    
class SingleToolSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Tool
    fields = ('id', 'name', 'description', 'uid')
    depth = 1
