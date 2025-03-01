"""View module for handling requests about types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from naileditapi.models.material import Material

class MaterialView(ViewSet):
  #GETS A SINGLE OBJECT FROM THE DB BASED ON THE PK IN THE URL
  #USE ORM TO GET DATA
  #API ENDPOINTS GET GENERATED
  def retrieve(self, request, pk):
  #SERIALIZER CONVERTS DATA TO JSON  
    try:
      material = Material.objects.get(pk=pk)
      #GETS A SINGLE OBJECT FROM DATA
      serializer = SingleMaterialSerializer(material)
      #IF OBJECT IS FOUND SERIALIZES TOOL TO JSON
      return Response(serializer.data)
    #SENDS JSON RESPONSE
    except Material.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    #IF OBJECT DOES NOT EXIST AN ERROR IS SENT
    
  def list(self, request):
    #GET... ALL OJECTS FROM DATABASE. ORM IS ALL
    material = Material.objects.all()
    
    serializer = MaterialSerializer(material, many=True)
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

    material = Material.objects.create(
        name=name,
        description=description,
        uid=uid
    )
    serializer = MaterialSerializer(material)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    #CREATES NEW OBJECT AND SAVES TO DATABASE
    serializer = MaterialSerializer(material)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  #SERIALIZES AND SHOWS A CREATED 201 STATUS
  
  def update(self, request, pk):
    material = Material.objects.get(pk=pk)

    material.name = request.data.get("name", material.name)
    material.description = request.data.get("description", material.description)
    material.uid = request.data.get("uid", material.uid)
    
    material.save()
    #SAVES UPDATE TO DATABASE
    serializer = MaterialSerializer(material)    
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    #DELETE....FETCHES THE OBJECT FROM DATABASE AND DELETES
    material = Material.objects.get(pk=pk)
    material.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  #RETURNS 204/SUCCESSFUL DELETION
  #SERIALIZER CLASS DETERMINES HOW PYTHON DATA SHOULD BE SERIALIZED TO BE SENT BACK TO CLIENT
class MaterialSerializer(serializers.ModelSerializer):
  #CONVERTS OBJECT TO JSON
  class Meta:
    model = Material
    fields = ('id', 'name', 'description', 'uid')
    
class SingleMaterialSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Material
    fields = ('id', 'name', 'description', 'uid')
    depth = 1
