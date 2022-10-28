from django.contrib import admin
from .models import artiste_id, song_id, Lyric
# Register your models here.
admin.site.register(artiste_id)
admin.site.register(song_id)
admin.site.register(Lyric)