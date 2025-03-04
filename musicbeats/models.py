from django.db import models

# Create your models here.
class song(models.Model):
    song_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000) 
    singer = models.CharField(max_length=1000) 
    tags = models.CharField(max_length=100)
    Images = models.ImageField(upload_to='Images')
    song=models.FileField(upload_to='Images')
    movie=models.CharField(max_length=1000, default="")
def __str__(self):
    return self.name  

class Artist(models.Model):
    Artist_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000) 
    bio = models.TextField(blank=True)
    Images = models.ImageField(upload_to='Images')
    song=models.FileField(upload_to='Images')
def __str__(self):
    return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=1000) 
    description = models.TextField(blank=True)
    Images = models.ImageField(upload_to='Images')
    song=models.FileField(upload_to='Images')
def __str__(self):
    return self.name

