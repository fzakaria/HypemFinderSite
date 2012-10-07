"""
Test file for hypemfinder.
This will test the actual code as well as the 
site is still using the same API that we've investigated
"""

from django.test import TestCase
from utils import generate_hype_html, get_track_list, generate_hype_url

class GenerateHypemHtml(TestCase):

    def test_can_read_hype_html(self):
        url = "http://hypem.com/latest"
        print "Testing Url: ", url
        html,cookie = generate_hype_html(url)
        track_list = get_track_list(html)
        print "Found: ",len(track_list), " tracks."
        self.assertTrue(len(track_list) > 0)

