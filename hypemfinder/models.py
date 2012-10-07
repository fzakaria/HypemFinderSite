from django.db import models
import json as simplejson

class Song(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  title = models.CharField(max_length=200)
  key = models.CharField(max_length=200)
  artist = models.CharField(max_length=200)
  cookie = models.CharField(max_length=200)
  url = models.URLField()

  def get_hype_url(self):
    return  "http://hypem.com/serve/source/{}/{}".format(self.id,self.key)

  #move to a classmethod at some point
  @staticmethod
  def get_by_tracklist(tracklist, cookie):
    songs = []
    for track in tracklist:
      key = track[u"key"]
      artist = track[u"artist"]
      song_id = track[u"id"]
      title = track[u"song"]
      song, created = Song.objects.get_or_create(id=song_id, defaults= {'title':title, 'key':key, 'artist':artist, 'cookie':cookie} )
      if created:
        song.url = generate_hype_url(song.get_hype_url(), song.cookie)
        song.save()
      songs.append(song)
    return songs

  def to_json(self):
    song = {}
    
    
    fields = []
    for field in self._meta.fields:
      fields.append(field.name)

    d = {}
    for attr in fields:
        d[attr] = getattr(self, attr)
    return simplejson.dumps(d)
