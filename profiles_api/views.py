from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
#from rest_framework.renderers import JSONRenderer

from . import serializers
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    #renderer_classes = [JSONRenderer]

    #get request
    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',

        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    #post request
    def post(self, request):
        """Create a hello message with out name"""
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    #put request is used to update a text
    #here arguement pk means primary key and it is used to update the selected id object
    def put(self, request, pk=None):
        """Handle updating an objext"""
        return Response({'method':'PUT'})

    #patch request is used to partial update the object
    #for example if u want to update the last name but not the first name then u use patch request to partially update an object
    def patch(self, request, pk=None):
        """Handle a partial update of object"""
        return Response({'method':'PATCH'})

    #Delete request is used to delete an objects in the database
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""
        a_viewset = [
        'Uses action(list, create, retrieve, update, partial_update)',
        'Autometically maps to url usin routers',
        'Provides more functionality with less code',
        ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message"""
        #retrieving serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle Getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle Updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})
