# coding: utf-8
__author__ = 'Alison Mukoma <alison@devsbranch.com>'
__license__ = 'GPL'
__copyright__ = 'devsbranch.com'

from django.conf.urls import url
from .views.url_shortcode import URLShortcodeAPI
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', URLShortcodeAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
