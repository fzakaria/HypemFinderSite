from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from hypemfinder.models import Song
from django.core.urlresolvers import reverse
from hypemfinder.forms import SearchForm
from django.template import RequestContext
from utils import generate_hype_html, get_track_list, generate_hype_url
import urllib2

def index(request):
    search_form = SearchForm()
    return render(request, 'hypemfinder/index.html', { 'search_form': search_form} )

def ajax_lookup(request):
  if request.method == 'GET':
    url = request.GET.get('url','')
    print "url is : " + url + "\n"
    html, cookie = generate_hype_html(url)
    track_list = get_track_list(html)
    songs = Song.get_by_tracklist(track_list, cookie)
    jsongs = []
    for song in songs:
      jsongs.append(song.to_json)
    print jsongs
    return HttpResponse(jsongs, mimetype="application/json")

def lookup(request):
    search_form = SearchForm() #an unbound form
    if request.method == 'GET':
        search_form = SearchForm(request.GET)
        if search_form.is_valid():# all validation passed
            print "IS VALID!"
            url = search_form.cleaned_data['url']
            html, cookie = generate_hype_html(url)
            track_list = get_track_list(html)
            songs = Song.get_by_tracklist(track_list, cookie)
            return render(request, 'hypemfinder/song_list.html', { 'search_form': search_form, 'songs': songs} )
    return render(request, 'hypemfinder/index.html', { 'search_form': search_form} )


def download(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    hype_request = urllib2.Request(song.url)
    hype_response = urllib2.urlopen(hype_request)
    response = HttpResponse(hype_response, content_type='audio/mpeg')
    response['Content-Disposition'] = 'attachment; filename={}.mp3'.format(song.title)
    return response

def details(request, song_id):
    search_form = SearchForm()
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'hypemfinder/details.html', { 'song': song, 'search_form': search_form} )
