import urllib2, urllib
from bs4 import BeautifulSoup
from time import time
import json
import logging

logger = logging.getLogger(__name__)

def generate_hype_html(url):
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

def get_track_list(html):
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
        print "Not valid json"
        return []

def generate_hype_download_url(song_url, cookie):
    request = urllib2.Request(song_url, "" , {'Content-Type': 'application/json'})
    request.add_header('cookie', cookie)
    response = urllib2.urlopen(request)
    song_data_json = response.read()
    response.close()
    song_data = json.loads(song_data_json)
    logger.debug("Retrieve song data: {} ".format(song_data) )
    url = song_data[u"url"]
    return url