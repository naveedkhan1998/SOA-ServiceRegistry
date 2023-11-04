from rest_framework import serializers
from .models import Server,ServiceEndpoint,Url

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'

class ServiceEndpointSerializer(serializers.ModelSerializer):
    server = ServerSerializer()
    class Meta:
        model = ServiceEndpoint
        fields = '__all__'

class UrlSerializer(serializers.ModelSerializer):
    server = ServerSerializer()
    class Meta:
        model = Url
        fields = '__all__'
