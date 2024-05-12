from rest_framework import serializers
from music.models import Artist, Album, Tracks


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name','last_update','created_date']

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    class Meta:
        model = Album
        fields = '__all__'

class TracksSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)
    class Meta:
        model = Tracks
        fields = '__all__'
