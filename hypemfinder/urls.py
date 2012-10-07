from django.conf.urls import patterns, include, url


urlpatterns = patterns('hypemfinder.views',
    url(r'^$', 'index'),
    url(r'^lookup/$', 'lookup'),
    url(r'^ajaxlookup/$', 'ajax_lookup'),
    url(r'^download/(?P<song_id>\w+)/$', 'download'),
    url(r'^songs/(?P<song_id>\w+)/$', 'details'),
)
