from server.models import Server, Category
from rest_framework import serializers

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'