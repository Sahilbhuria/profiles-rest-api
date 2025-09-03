from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""
    def get(self,request, format=None):
        """Returns a list of apiview features"""
        an_apiview=[
            'Uses HTTP methods as function (get , post etc.)',
            'Is similar to a traditional django view',
            'gives you the most control over your app logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'hello','an_apiview':an_apiview})
