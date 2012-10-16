from django.contrib import admin
from hypemfinder.models import HypemSong

class HypemSongAdmin(admin.ModelAdmin):
    pass

admin.site.register(HypemSong, HypemSongAdmin)