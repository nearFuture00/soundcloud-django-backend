from django.contrib import admin
from .models import *

admin.site.register(Artist)

admin.site.register(Track)
admin.site.register(TrackComment)
admin.site.register(TrackGenre)

admin.site.register(Playlist)