from django.contrib import admin

from.models import Song, Channel, Plays

# Register your models here.
admin.site.register(Song)
admin.site.register(Channel)
admin.site.register(Plays)