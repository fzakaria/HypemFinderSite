from django import forms
from hypemfinder.models import Song
from django.forms import ModelForm

class SearchForm(ModelForm):
    query = forms.CharField(max_length=200)
    class Meta:
        model = Song
        fields = ('song_type',)

