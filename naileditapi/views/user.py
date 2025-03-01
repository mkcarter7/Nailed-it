"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from naileditapi.models.user import User


class UserView(ViewSet):

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        users = User.objects.all()
        
        uid = request.query_params.get('uid', None)
        if uid is not None:
            users = users.filter(uid=uid)
    
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
      
    def destroy(self, request, pk):
      user = User.objects.get(pk=pk)
      user.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')
        depth = 1
