from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.renderers import JSONRenderer
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""

    #renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',

        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
