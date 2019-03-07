# coding: utf-8
__author__ = 'Alison Mukoma <alison@devsbranch.com>'
__license__ = 'GPL'
__copyright__ = 'devsbranch.com'

import random
import string

from django.conf import settings

# we try to get the settings length and if it's empty we default to 4
SHORT_URL_MIN_LEN = getattr(settings.SHORT_URL_MIN_LEN, 'SHORT_URL_MIN_LEN', 8)


def short_code_generator(size=SHORT_URL_MIN_LEN, chars=string.ascii_lowercase+string.digits):
    """We use the string module to generate a unique combination of
    characters and numbers for our short url."""

    generated_url_code = ''.join(random.choice(chars) for _ in range(size))
    return generated_url_code


def create_short_url(instance, size=SHORT_URL_MIN_LEN):
    fresh_url_code = short_code_generator(size=size)
    kls =instance.__class__ # a stub to acquire the class instance we are in
    qs_exists = kls.objects.filter(shortened_url=fresh_url_code).exists()
    if qs_exists:
        return create_short_url(instance, size=size)
    return fresh_url_code

