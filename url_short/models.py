from django.db import models
import random
from django import forms


class ShortLink(models.Model):
    original_url = models.URLField(verify_exists=True, unique=True)
    mini_url = models.CharField(max_length=20, primary_key=True, unique=True)

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        kwargs.setdefault('mini_url', self.randomize())
        super(ShortLink, self).__init__(*args, **kwargs)

    def randomize(self, mini_url):
        chars = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz1234567890", 7))
        return chars

    def __unicode__(self):
        return self.original_url + ", " + self.mini_url


class LinkForm(forms.Form):
    u = forms.URLField(verify_exists=True,
                       label='What URL would you like to shorten?',
                       )