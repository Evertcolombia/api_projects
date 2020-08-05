from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers

from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test API View"""

    # the name serializer_class must be used always
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Function to Post an user"""

        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """"Handle a partial update of an object"""
        return Response({"Method": "PATCH"})

    def delete(self, request, pk=None):
        """"Deletes and object"""
        return Response({"Method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test api ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLs using  routers',
            'Provides more functionality with less code'
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset}) 

    def create(self, request):
        """Create """
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
        """ handle getting an objecst by id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ handle updating pan object"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle updating part of and object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handel removing an object"""
        return Response({'http_method': 'DELETE'})