# coding: utf-8
__author__ = 'Alison Mukoma <mukomalison@gmail>'
__license__ = 'GPL'
__doc__ = ''

from django.core.management.base import BaseCommand

from shortcode.models import URLDefine


class Command(BaseCommand):
    """
    We add the url refresh to management commands
    so as we can access it with the base manager.
    """

    def add_arguments(self, parser):
        parser.add_argument(
        '--items',
        dest='items',
        default='',
        help='Refresh existing URL short codes (generate new ones).Provide '
             'how many you would like to refresh or leave empty to refresh '
             'all.'
        )

    def handle(self, *args, **options):
        handler = URLDefine.objects.refresh_short_urls(
            items=options['items']
        )
        return handler
