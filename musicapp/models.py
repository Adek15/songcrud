from django.db import models
from datetime import datetime

# Create your models here.
class artiste_id(models.Model):
    first_name = models.CharField(max_length= 40)
    last_name = models.CharField(max_length= 40)
    age = models.IntegerField()

class song_id(models.Model):
    artiste_id = models.ForeignKey(artiste_id, on_delete = models.CASCADE)
    title = models.CharField(max_length= 400)
    date_released = models.DateField(default= datetime.today)
    likes = models.IntegerField()

class Lyric(models.Model):
    Song = models.ForeignKey(song_id, on_delete= models.CASCADE)
    content = models.CharField(max_length= 1000000)
    