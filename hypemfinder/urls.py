from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('hypemfinder.views',
    url(r'^$', 'index'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),
    url(r'^ajaxlookup/$', 'ajax_lookup'),
    url(r'^download/(?P<song_type>\w+)/(?P<song_id>\w+)/$', 'download'),
    url(r'^songs/(?P<song_id>\w+)/$', 'details'),
)
