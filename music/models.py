from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=255)
    albumTitle = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    albumLogo = models.CharField(max_length=1500)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=100)
    songTitle = models.CharField(max_length=255)
