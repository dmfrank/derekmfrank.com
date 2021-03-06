# $Id: urls.py,v 1.1 2013-06-30 17:08:56-07 dmf - $
# Derek Frank
#
# NAME
#   urls.py - webmaster
#
# DESCRIPTION
#   A url patterns definition for webmasters.
#

from django.conf.urls import patterns, url
import views


# Webmasters and other 3rd party site apps
urlpatterns = patterns('',
    # Google Analytics/Webmaster
    url(r'^google0a2e75908547fa0e.html$', views.google, name='googlewebmaster'),
    
    # Bing Webmaster
    url(r'^BingSiteAuth.xml$', views.bing, name='bingwebmaster'),
)
