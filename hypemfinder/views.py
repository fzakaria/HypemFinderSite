from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, get_list_or_404, render
from hypemfinder.models import Song, HypemSong, SoundSong
from django.core.urlresolvers import reverse
from hypemfinder.forms import SearchForm
from django.template import RequestContext
from django.http import Http404
import urllib2
import logging
from hypemfinder.response import JsonResponse

logger = logging.getLogger(__name__)

def index(request):
    search_form = SearchForm()
    return render(request, 'hypemfinder/index.html', {'search_form': search_form})

def ajax_lookup(request):
    if request.method != 'GET':
        logger.warning("Tried a POST request to the ajax method")
        return HttpResponseBadRequest()
    search_form = SearchForm(request.GET)
    if search_form.is_valid() is False:
        return HttpResponseBadRequest()

    query = search_form.cleaned_data['query']
    search_type = search_form.cleaned_data['song_type']

    if search_type == Song.HYPEM:
        html, cookie = HypemSong.search_hype_html(query)
        songs = HypemSong.get_songs_from_html(html, cookie)
        logger.debug("FOUND {} songs.".format(len(songs)))
        return JsonResponse(songs)

    return HttpResponseBadRequest()


def download(request, song_type, song_id):
    #Step 1: Get the song in question
    if song_type == Song.HYPEM:
        song = get_object_or_404(HypemSong, pk=song_id)
    elif song_type == Song.SOUNDCLOUD:
        song = get_object_or_404(SoundSong, pk=song_id)
    else:
        raise Http404

    #Step 2: Call Hypem.com to get the song download URL
    song.download_url = song.get_download_url()
    try:
        download_request = urllib2.Request(song.download_url)
        download_response = urllib2.urlopen(download_request)
        response = HttpResponse(download_response, content_type='audio/mpeg')
        response['Content-Disposition'] = 'attachment; filename="{}.mp3"'.format(song.title)
        song.download_count += 1
        song.save()
        return response
    except urllib2.URLError, e:
        logger.warning("Failed performing request to {} with reason: {}".format(song.download_url, e.reason) )
        raise Http404

def details(request, song_id):
    search_form = SearchForm()
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'hypemfinder/details.html', { 'song': song, 'search_form': search_form} )


