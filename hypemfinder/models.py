from django.db import models

class Song(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    cookie = models.CharField(max_length=200)
    url = models.URLField()

    def get_hype_url(self):
        return  "http://hypem.com/serve/source/{}/{}".format(self.id,self.key)
