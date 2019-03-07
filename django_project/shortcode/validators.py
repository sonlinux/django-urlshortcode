# coding: utf-8
__author__ = 'Alison Mukoma <alison@devsbranch.com>'
__license__ = 'GPL'
__copyright__ = 'devsbranch.com'

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def is_url_valid(url):
    validator = URLValidator()
    url_to_validate = url
    if "http" in url_to_validate:
        valid_url = url_to_validate
    else:
        valid_url = 'http://' + url
    try:
        validator(valid_url)
    except:
        raise ValidationError('Please provide a valid URL')
    return valid_url

