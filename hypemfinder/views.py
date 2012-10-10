from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from hypemfinder.models import Song
from django.core.urlresolvers import reverse
from hypemfinder.forms import SearchForm
from django.template import RequestContext
from utils import generate_hype_html, get_track_list,generate_hype_download_url
from django.http import Http404
import urllib2
import logging
from hypemfinder.response import JsonResponse

logger = logging.getLogger(__name__)

def index(request):
    search_form = SearchForm()
    return render(request, 'hypemfinder/index.html', { 'search_form': search_form} )

def ajax_lookup(request):
    if request.method != 'GET':
        logger.warning("Tried a POST request to the ajax method")
        return HttpResponseBadRequest()
    url = request.GET.get('url')
    if url is None:
        logger.warning("Did not send any url parameter to the GET request")
        return HttpResponseBadRequest()
    logger.debug("Ajax Lookup Request for url: {}".format(url) )
    html, cookie = generate_hype_html(url)
    track_list = get_track_list(html)
    songs = Song.get_by_tracklist(track_list, cookie)
    logger.debug("FOUND {} songs.".format(len(songs)))
    return JsonResponse(songs)

def lookup(request):
    search_form = SearchForm() #an unbound form
    if request.method == 'GET':
        search_form = SearchForm(request.GET)
        if search_form.is_valid():# all validation passed
            url = search_form.cleaned_data['url']
            html, cookie = generate_hype_html(url)
            track_list = get_track_list(html)
            songs = Song.get_by_tracklist(track_list, cookie)
            return render(request, 'hypemfinder/song_list.html', { 'search_form': search_form, 'songs': songs} )
    return render(request, 'hypemfinder/index.html', { 'search_form': search_form} )


def download(request, song_id):
    #Step 1: Get the song in question
    song = get_object_or_404(Song, pk=song_id)
    #Step 2: Call Hypem.com to get the song download URL
    song.download_url = generate_hype_download_url(song.get_hype_url(), song.cookie)
    try:
        hype_request = urllib2.Request(song.download_url)
        hype_response = urllib2.urlopen(hype_request)
        response = HttpResponse(hype_response, content_type='audio/mpeg')
        response['Content-Disposition'] = 'attachment; filename="{}.mp3"'.format(song.title)
        song.download_count += 1
        song.save()
        return response
    except urllib2.URLError, e:
        logger.warning("Failed performing request to {} with reason: {}".format(song.url, e.reason) )
        raise Http404

def details(request, song_id):
    search_form = SearchForm()
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'hypemfinder/details.html', { 'song': song, 'search_form': search_form} )


