# coding: utf-8
__author__ = 'Alison Mukoma <mukomalison@gmail>'
__license__ = 'GPL'
__doc__ = ''

from django.db import models
from django.utils.encoding import smart_text
from django.core.urlresolvers import reverse
from django.conf import settings

from ..utils.short_url import create_short_url
from ..validators import is_url_valid

# we try to get the settings length and if it's empty we default to 8
SHORT_URL_MAX_LEN = getattr(settings.SHORT_URL_MAX_LEN,
                             'SHORT_URL_MAX_LEN', 8)


class URLShortcodeManager(models.Manager):
    def all(self, *args, **kwargs):
        """
        We attempt to override the intitial 'all' method
        to only return active links.
        """
        qs_parent = super(URLShortcodeManager, self).all(*args, **kwargs)
        qs = qs_parent.filter(is_active=True)
        return qs

    def refresh_short_urls(self, items=None):
        qs_urls = URLDefine.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            # Note that we can also order the object from the models Metaclass.
            qs_short_urls = qs_urls.order_by('-id')[:items]
        # we reset the count to recreate existing short codes
        new_short_url_codes = 0
        for query in qs_urls:
            query.shortened_url = create_short_url(query)
            print(query.id)
            query.save()
            # we attempt to do do this for all queried objects
            new_short_url_codes += 1
        msq = 'Fresh short URs created: {codes}'.format(
            codes=new_short_url_codes)
        return msq


class URLDefine(models.Model):
    url = models.CharField(max_length=250, validators=[is_url_valid])
    shortened_url = models.CharField(max_length=SHORT_URL_MAX_LEN, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = URLShortcodeManager()

    class Meta:
        verbose_name = 'URL Entry'
        verbose_name_plural = 'URL Entries'

    def __str__(self):
        """smart_text method will allow us to see issues in the admin panel."""
        return smart_text(self.url)

    def __unicode__(self):
        """
        Fail safe option in case we use python version
        not supporting  __str__."""
        return smart_text(self.url)

    def save(self, *args, **kwargs):
        if self.shortened_url is None or self.shortened_url == '':
            self.shortened_url = create_short_url(self)
        if not 'http' in self.url:
            self.url = 'http://' + self.url
        super(URLDefine, self).save(*args, **kwargs)

    def get_url_shortcode(self):
        """Same operation as the 'get_absolute_url' method."""
        url_path = reverse('shortcode', kwargs={
            'url_shortcode':  self.shortened_url})
        return url_path