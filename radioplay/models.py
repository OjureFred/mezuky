from django.db import models

from datetime import datetime

# Create your models here.
class Song(models.Model):
    ISRC = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)

class Channel(models.Model):
    channel_name = models.CharField(max_length=100)
    channel_city = models.CharField(max_length=100)
    channel_country = models.CharField(max_length=100)

class Plays(models.Model):
    song = models.ForeignKey(blank=True, null=True)
    Channel = models.ForeignKey(blank=True, null=True)
    date = models.DateTimeField(datetime=datetime.date)
    plays = models.IntegerField(default=1)
