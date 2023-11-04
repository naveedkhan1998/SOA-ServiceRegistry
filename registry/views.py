from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Server, ServiceEndpoint, Url
from rest_framework.response import Response
from .serializers import ServerSerializer, ServiceEndpointSerializer, UrlSerializer
from .helper import ping_websocket
from rest_framework import status


@api_view(["GET"])
@permission_classes([AllowAny])
def update_clients(request):
    ping_websocket()
    return Response({"msg": "OK!"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_endpoints(request):
    url = Url.objects.filter(is_active=True)
    url_serializer = UrlSerializer(url, many=True).data
    endpoints = ServiceEndpoint.objects.filter(is_active=True)
    endpoints_serializer = ServiceEndpointSerializer(endpoints, many=True).data

    return Response(
        {"urls": url_serializer, "endpoints": endpoints_serializer},
        status=status.HTTP_200_OK,
    )
