from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """test API View."""

    def get(self, request, format=None):
        """return a list of APIView features."""

        an_apiview = [
            'uses HTTP methods as functions (get, post, patch, put, delete)',
            'it is similar to a traditional Djando view',
            'Gives you the most control over your logic',
            'is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
        
