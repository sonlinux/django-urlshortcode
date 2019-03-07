# coding: utf-8
__author__ = 'Alison Mukoma <mukomalison@gmail>'
__license__ = 'GPL'
__doc__ = ''

from rest_framework import serializers
from shortcode.models.short_url import URLDefine

class URLDefineSerializer(serializers.ModelSerializer):
    """
    Serializer for URL definition model.
    Nothing special here, we are just serializing all current fields,
    the main event scenarios to be handled in the API views.
    """
    class Meta:
        model = URLDefine
        fields = '__all__'
