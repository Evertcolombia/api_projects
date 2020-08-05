from rest_framework import status
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
