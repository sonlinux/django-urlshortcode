# coding: utf-8
__author__ = 'Alison Mukoma <mukomalison@gmail>'
__license__ = 'GPL'
__doc__ = ''

from urlparse import urlparse

from django.http import HttpResponseRedirect, Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from shortcode.models.short_url import URLDefine
from api.serializers.url_serializer import URLDefineSerializer as URLSerializer

class URLShortcodeAPI(APIView):
    """API for posting URL."""

    def post(self, request, format=None):
        self.serializer = URLSerializer(data=request.data)
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            shortcode = serializer.data.get('shortened_url', None)
            url = serializer.data.get('url', None)

            self.host = self.request.environ['HTTP_HOST']
            self.domain = urlparse(self.host)

            response_data = {}
            main_url = self.domain.scheme+self.host+'/'+shortcode
            response_data.update({ 'shortened_url': main_url })

            return Response(response_data,
                            status=status.HTTP_201_CREATED)
        return Response("Something went wrong in processing your request. "
                        "Ensure your data is JSON valid.",
                        status=status.HTTP_400_BAD_REQUEST)


class URLRedirectView(APIView):

    def get(self, request, **kwargs):
        shortcode_hash = self.kwargs.get('shortcode', None)
        url_path = {}

        qs_url = URLDefine.objects.filter(shortened_url__iexact=shortcode_hash)
        if qs_url:

            url_path.update({'url': qs_url})
        print('Sorry we could not find your URL.')
        url = url_path['url'][0]

        return HttpResponseRedirect(url)