from __future__ import absolute_import

from django.views.generic.base import RedirectView
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import (
    HomeView,
    QuoteView,
)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^quote/$', QuoteView.as_view(), name='quote'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/public/images/favicon.ico'))
)

urlpatterns += staticfiles_urlpatterns()
