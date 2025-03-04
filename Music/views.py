from django.shortcuts import render
from musicbeats.models import song



def index(request):
    songs = song.objects.all()
    return render(request,'index.html',{'songs':songs})

