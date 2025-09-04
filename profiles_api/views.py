from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer
    def get(self,request, format=None):
        """Returns a list of apiview features"""
        an_apiview=[
            'Uses HTTP methods as function (get , post etc.)',
            'Is similar to a traditional django view',
            'gives you the most control over your app logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'hello','an_apiview':an_apiview})

    def post(self,request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """handle updateing object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """"partial update"""
        return Response({'method':'PATCH'})


    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test APi ViewSet"""

    def list(self,request):
        """Return a hello message"""
        a_viewset =[
        'USes actions (list , create,retrieve,update,partial_update)',
        'Automatically maps to URLs using router.',
        'Provide More FUnctionalitywith less code',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})
