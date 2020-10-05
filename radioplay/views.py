from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Channel
from .serializers import ChannelSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/channels-list/',
        'Detail View': '/chanels-detail/<str:pk>/',
        'Create': '/channels-create/',
        'Update': '/channels-update/<str:pk>/',
        'Delete': '/channels-delete/<str:pk>/',
        
    }
    return JsonResponse(api_urls)

@api_view(['GET'])
def channelsList(request):
    channels = Channel.objects.all()
    serializer = ChannelSerializer(channels, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def channelDetail(request, pk):
    channel = Channel.objects.get(id=pk)
    serializer = ChannelSerializer(channel, many=False)

    return JsonResponse(serializer.data)

@api_view(['POST'])
def channelCreate(request):
    serializer = ChannelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)



