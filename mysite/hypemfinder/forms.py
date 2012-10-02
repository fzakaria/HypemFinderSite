from django import forms
from urlparse import urlparse
from django.core.exceptions import ValidationError

class SearchForm(forms.Form):
    url = forms.URLField(initial='http://')

    def clean_url(self):
        url = self.cleaned_data["url"]
        domain = urlparse(url).hostname
        if domain != "hypem.com":
            raise ValidationError("Must be a hypem.com url")
        return url

