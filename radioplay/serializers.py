from rest_framework import serializers

from .models import Channel, Song, Plays

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'