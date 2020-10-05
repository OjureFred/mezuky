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
    class Meta:
        model = Plays
        fields = '__all__'