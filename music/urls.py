from django.urls import path,include
from .views import LandingPageApiView,ArtistDetailApiView,AlbumDetailApiView,TrackDetailApiView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register("albums", viewset=AlbumDetailApiView),
router.register("tracks", viewset=TrackDetailApiView),
router.register("artists", viewset=ArtistDetailApiView),

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]