from django.db import models
from django.forms import ModelForm
import random



def randomize():
    chars = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz1234567890", 7))
    return chars

class ShortLink(models.Model):
    original_URL = models.CharField(max_length = 2048)
    mini_URL = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.original_URL

class ShortLinkForm(ModelForm):
    class Meta:
        model = ShortLink
        exclude = ('mini_URL',)


