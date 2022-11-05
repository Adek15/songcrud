from rest_framework import serializers
from apis.models import artiste_id, song_id, Lyric


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ("song_id", "content")


class artiste_idSerializer(serializers.ModelSerializer):
    class Meta:
        model: artiste_id
        fields = ("first_name", "last_name", "age")


class song_idSerializer(serializers.ModelSerializer):
    class Meta:
        model: song_id
        fields = ("artiste_id", "title", "date_released", "likes")
