# coding: utf-8
__author__ = 'Alison Mukoma <mukomalison@gmail>'
__license__ = 'GPL'
__doc__ = ''


from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import JsonResponse
# from django.views import View
from django.http import HttpResponseRedirect, Http404

from shortcode.models.short_url import URLDefine
from api.serializers.url_serializer import URLDefineSerializer as URLSerializer


class URLShortcodeAPI(APIView):
    """API for posting URL."""
    # authentication_classes = (authentication.SessionAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)


    def get(self, request, *args):
        queryset = URLDefine.objects.all()
        serializer = URLSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        url = request.POST.get('url', None)
        shortened_url = request.POST.get('shortened_url', None)
        count = 0

        URLDefine(
            url=url,
            shortened_url=shortened_url,
        ).save()

        urls = URLDefine.objects.all()
        serializer = URLSerializer (urls, many=True)
        return Response (serializer.data)


class URLRedirectView(APIView):

    def get(self, request, shortcode=None, *args, **kwargs):
        qs = URLDefine.objects.filter(shortened_url__iexact=shortcode)
        # serializer = URLSerializer(qs)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        # print(ClickEvent.objects.create_event(obj))
        return Response(HttpResponseRedirect(obj.url))

#
#
# class URLShortcodeAPI(APIView):
#     def get(self, request):
#         print(self.request.query_params.get('shortened_url'),
#               self.request.query_params)
#         shortened_url = self.request.query_params.get('shortened_url')
#         try:
#             req_url=URLDefine.objects.get(shortened_url=shortened_url)
#             req_url.count = req_url.count + 1
#             req_url.save()
#             serializer=URLSerializer(req_url)
#             return Response(serializer.data)
#         except Exception as e:
#             print(e)
#             return JsonResponse({"mesage": "Requested URL not dfound"})
#
#     def post(self, request):
#         url = request.POST.get('url', None)
#         shortened_url = request.POST.get('shortened_url', None)
#         count = 0
#
#         URLDefine(
#             url=url,
#             shortened=shortened_url,
#         ).save()
#
#         urls = URLDefine.objects.all()
#         serializer = URLSerializer (urls, many=True)
#         return Response (serializer.data)
#
