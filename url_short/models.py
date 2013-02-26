from django.db import models
import random
from django.forms import ModelForm
from django import forms


class ShortLink(models.Model):
    original_url = models.URLField('What URL would you like to shorten?')
    mini_url = models.CharField(max_length=20)

    def randomize(self):
        chars = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz1234567890", 7))
        return chars

class ShortLinkForm(ModelForm):
    class meta:
        model = ShortLink
        fields = 'original_url'


