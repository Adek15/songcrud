from django.urls import path
from apis.views import LyricAPIView, artiste_idAPIView, song_idAPIView

urlpatterns = [
    path("song", song_idAPIView.as_view(), name="song"),
    path("lyrics", LyricAPIView.as_view(), name="lyrics"),
    path("artiste", artiste_idAPIView.as_view(), name="artiste"),
]
