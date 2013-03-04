__author__ = 'jacqui'

from django import forms
#from models import Category


class ShortLinkForm(forms.Form):
    original_URL = forms.URLField()
