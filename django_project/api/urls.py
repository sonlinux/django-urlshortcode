# coding: utf-8
__author__ = 'Alison Mukoma <alison@devsbranch.com>'
__license__ = 'GPL'
__copyright__ = 'devsbranch.com'

from django.conf.urls import url
from .views.url_shortcode import URLShortcodeAPI, URLRedirectView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', URLShortcodeAPI.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
