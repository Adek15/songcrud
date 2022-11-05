from django.db import models
from datetime import datetime

# Create your models here.
class artiste_id(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.last_name


class song_id(models.Model):
    artiste_id = models.ForeignKey(artiste_id, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()

    def __str__(self):
        return self.title


class Lyric(models.Model):
    song_id = models.ForeignKey(song_id, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000000)

    def __str__(self):
        return self.content
