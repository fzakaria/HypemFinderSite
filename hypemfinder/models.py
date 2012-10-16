from django.db import models
import urllib2, urllib
import json as simplejson
import logging
from bs4 import BeautifulSoup
from time import time
import json
import httplib2
logger = logging.getLogger(__name__)

class Song(models.Model):
    SOUNDCLOUD = 'SC'
    HYPEM = 'HM'
    SONG_CHOICES = (
        (SOUNDCLOUD, 'SoundCloud'),
        (HYPEM, 'HypeMachine'),
    )
    song_id = models.CharField(max_length=20)
    song_type = models.CharField(max_length=2,choices=SONG_CHOICES, default=HYPEM)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    time = models.PositiveIntegerField(default=0)
    download_count = models.PositiveIntegerField(default=0)
    download_url = models.URLField()
    post_url = models.URLField()
    class Meta:
        abstract = True

    def get_download_url(self):
        raise NotImplementedError


class SoundSong(Song):
    token = models.CharField(max_length=200)
    waveform_url = models.URLField()


class HypemSong(Song):
    key = models.CharField(max_length=200)
    cookie = models.CharField(max_length=200)

    def get_download_url(self):
        return self.get_hype_download_url()

    def get_hype_url(self):
        """Gets the URL that serves the streaming URL for the song"""
        return  "http://hypem.com/serve/source/{}/{}".format(self.song_id, self.key)

    def get_hype_download_url(self):
        """Helpfer function for get_download_url"""
        url = "http://www.doesntexist.com"
        try:
            request = urllib2.Request(self.get_hype_url(), "" , {'Content-Type': 'application/json'})
            request.add_header('cookie', self.cookie)
            response = urllib2.urlopen(request)
            song_data_json = response.read()
            response.close()
            song_data = json.loads(song_data_json)
            logger.debug("Retrieve song data: {} ".format(song_data) )
            url = song_data[u"url"]
        except urllib2.HTTPError, e:
            logger.warning('HTTPError = ' + str(e.code) + " trying hypem download url.")
        except urllib2.URLError, e:
            logger.warning('URLError = ' + str(e.reason)  + " trying hypem download url.")
        except Exception, e:
            logger.warning('generic exception: ' + str(e))
        return url

    @staticmethod
    def search_hype_html(query):
        encoded_query = urllib.quote_plus(query)
        search_url = "http://hypem.com/search/{}".format(encoded_query)
        data = {'ax':1 ,
                'ts': time()
                }
        data_encoded = urllib.urlencode(data)
        complete_url = search_url+"?{}".format(data_encoded)
        request = urllib2.Request(complete_url)
        response = urllib2.urlopen(request)
        cookie = response.headers.get('Set-Cookie')
        html = response.read()
        response.close()
        return html,cookie

    @staticmethod
    def url_hype_html(url):
        """This generates the complete hypem url. Guarenteed to be hypem.com url"""
        data = {'ax':1 ,
                'ts': time()
        }
        data_encoded = urllib.urlencode(data)
        complete_url = url+"?{}".format(data_encoded)
        request = urllib2.Request(complete_url)
        response = urllib2.urlopen(request)
        cookie = response.headers.get('Set-Cookie')
        html = response.read()
        response.close()
        return html,cookie

    @staticmethod
    def get_songs_from_html(html, cookie):
        """Parses the HTML and the interior json and returns list"""
        songs = []
        track_list = HypemSong.get_json_song_data(html,cookie)
        for track in track_list:
            try:
                key = track[u"key"]
                artist = track[u"artist"]
                id = track[u"id"]
                title = track[u"song"]
                posturl = track[u"posturl"]
                time = int(track[u"time"])
                type = track[u"type"]

                if type is False:
                    continue

                song, created = HypemSong.objects.get_or_create(song_id=id,
                                                           defaults={'title': title, 'key': key, 'artist': artist,
                                                                     'cookie': cookie, 'post_url': posturl, 'time': time,
                                                                     'song_id' : id, "song_type" : Song.HYPEM })
                songs.append(song)
            except KeyError, e:
                logger.warning("JSON song data was missing key: {}".format(str(e)) )
            except Exception, e:
                logger.warning("Uncaught exception: {}".format(str(e)) )

        return songs


    @staticmethod
    def get_json_song_data(html, cookie):
        """Parses the HTML and the interior json and returns list"""
        track_list = []
        soup = BeautifulSoup(html)
        html_tracks = soup.find(id="displayList-data")
        if html_tracks is None:
            return track_list
        try:
            track_list = json.loads(html_tracks.text)
            return track_list[u'tracks']
        except ValueError:
            logger.warning("Hypemachine contained invalid JSON.")
            return track_list