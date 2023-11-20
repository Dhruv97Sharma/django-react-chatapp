from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from server.models import Server
from server.serializers import ServerSerializer

# Create your views here.
class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        
        if category:
            queryset = self.queryset.filter(category=category)

        serializer = ServerSerializer(queryset, many=True)
        return Response(serializer.data)