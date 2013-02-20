from django.db import models
import random


class ShortLink(models.Model):
    original_url = models.CharField(max_length=2048)
    mini_url = models.CharField(max_length=20, primary_key=True)

    def randomize(self):
        chars = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz1234567890", 7))
        return chars

    mini_url = randomize

    def __unicode__(self):
        return self.original_url + ", " + self.mini_url
