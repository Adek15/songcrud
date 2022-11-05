from django.shortcuts import render
from apis.serializers import LyricSerializer, artiste_idSerializer, song_idSerializer
from apis.models import Lyric, song_id, artiste_id
from rest_framework import generics

# Create your views here.
class LyricAPIView(generics.ListAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer


class artiste_idAPIView(generics.ListAPIView):
    queryset = artiste_id.objects.all()
    serializer_class = artiste_idSerializer


class song_idAPIView(generics.ListAPIView):
    queryset = song_id.objects.all()
    serializer_class = song_idSerializer
