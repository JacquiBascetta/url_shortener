__author__ = 'jacqui'

from django.conf.urls import patterns, url

from url_short import views

urlpatterns = patterns('',
    url(r'^$', views.find_origurl, name='find_origurl')
)