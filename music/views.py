# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from django.db.transaction import atomic
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Album, Artist, Tracks
from .serializers import ArtistSerializer, AlbumSerializer, TracksSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status
from rest_framework.pagination import LimitOffsetPagination

class LandingPageApiView(APIView):
    def get(self, request):
        return Response(data={"get api": 'Landing Page'})

    def post(self, request):
        return Response(data={"post api": ' This is post request'})



class ArtistDetailApiView(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', ]
    pagination_class = LimitOffsetPagination




class AlbumDetailApiView(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', ]
    pagination_class = LimitOffsetPagination


class TrackDetailApiView(ModelViewSet):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', ]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def listen(self, request, *args, **kwargs):
        track = self.get_object()
        with atomic():
            track.listened +=1
            track.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        tracks = self.get_queryset()
        tracks = tracks.order_by('-listened')[:3]
        serializer = TracksSerializer(tracks, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def album(self, request, *args, **kwargs):
        track = self.get_object()
        album = track.album
        serializer = AlbumSerializer(album)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def artist(self, request, *args, **kwargs):
        track = self.get_object()
        artist = track.album.artist
        serializer = ArtistSerializer(artist)
        return Response(data=serializer.data)









