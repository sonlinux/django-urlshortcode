# coding: utf-8
__author__ = 'Alison Mukoma <mukomalison@gmail>'
__license__ = 'GPL'
__doc__ = ''

from django.conf import settings
from django_hosts import patterns, host

host_patterns = pattern(
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', core.hostconf.urls, name='wildcard'),
)
