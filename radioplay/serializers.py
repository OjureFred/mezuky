from rest_framework import serializers

from .models import Channel, Song, Plays

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class PlaysSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)
    channels = ChannelSerializer(many=True, read_only=True)
    class Meta:
        model = Plays
        
        exclude = ('date',)