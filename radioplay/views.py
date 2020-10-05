from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Channel, Song, Plays
from .serializers import ChannelSerializer, SongSerializer

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
    
    return JsonResponse(serializer.data)

@api_view(['POST'])
def channelUpdate(request, pk):
    channel = Channel.objects.get(id=pk)
    serializer = ChannelSerializer(instance=channel, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return JsonResponse(serializer.data)

@api_view(['DELETE'])
def channelDelete(request, pk):
    channel = Channel.objects.get(id=pk)
    serializer = ChannelSerializer(data=request.data)
    channel.delete()

    return JsonResponse(serializer.data)

@api_view(['GET'])
def songsList(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)

    return JsonResponse(serializer.data, safe=False)




