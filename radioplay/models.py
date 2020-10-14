from django.db import models

from datetime import datetime

# Create your models here.
class Song(models.Model):
    ISRC = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)

    def __str__(self):
        return self.ISRC

class Channel(models.Model):
    channel_name = models.CharField(max_length=100)
    channel_city = models.CharField(max_length=100)
    channel_country = models.CharField(max_length=100)

    def __str__(self):
        return self.channel_name

class Plays(models.Model):
    song = models.ForeignKey(Song, blank=True, null=True, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
       
    channels = models.ManyToManyField(Channel, related_name='plays')
    
    def __str__(self):
        return self.song.ISRC
