__author__ = 'jacqui'

from django.conf.urls import patterns, url

from url_short import views

urlpatterns = patterns('',
    url(r'^$', views.find_origurl),
    url(r'^[a-z0-9]*$', views.redirect_mini),
)