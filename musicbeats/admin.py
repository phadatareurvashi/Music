from django.contrib import admin
from .models import song,Artist,Playlist
# Register your models here.

admin.site.register(song)
admin.site.register(Artist)
admin.site.register(Playlist)