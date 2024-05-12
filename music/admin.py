from django.contrib import admin

from django.contrib import admin
from .models import Album,Artist,Tracks

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Tracks)
