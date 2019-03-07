# coding=utf-8
"""
core.settings.contrib
"""
from .base import *  # noqa

from .dev import *  # accessing the cache backend configs

# Extra installed apps - grapelli needs to be added before others
INSTALLED_APPS = (
    'grappelli',
) + INSTALLED_APPS

INSTALLED_APPS += (
    'widget_tweaks',  # lets us add some bootstrap css to form elements
    'easy_thumbnails',
    'rest_framework',  # used for API
    'rest_framework_swagger',
    'crispy_forms',
    # 'django_hosts',

)

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

# noinspection PyUnresolvedReferences

MIGRATION_MODULES = {'accounts': 'core.migration'}

GRAPPELLI_ADMIN_TITLE = 'Site administration panel'

STOP_WORDS = (
    'a', 'an', 'and', 'if', 'is', 'the', 'in', 'i', 'you', 'other',
    'this', 'that'
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Easy-thumbnails options
THUMBNAIL_SUBDIR = 'thumbnails'
THUMBNAIL_ALIASES = {
    '': {
        'entry': {'size': (50, 50), 'crop': True},
        'medium-entry': {'size': (100, 100), 'crop': True},
        'large-entry': {'size': (400, 300), 'crop': True},
        'thumb300x200': {'size': (300, 200), 'crop': True},
    },
}

# Pipeline related settings

INSTALLED_APPS += (
    'pipeline',)

DEFAULT_FILE_STORAGE = (
    'django_hashedfilenamestorage.storage.HashedFilenameFileSystemStorage')

# use underscore template function
PIPELINE_TEMPLATE_FUNC = '_.template'

# enable cached storage - requires uglify.js (node.js)
# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Contributed / third party js libs for pipeline compression
# For hand rolled js for this app, use project.py
PIPELINE_JS = {}
PIPELINE_JS['contrib'] = {
    'source_filenames': (
        # 'js/gifffer.js',
        'js/jquery.min.js',
        # 'chosen/chosen.js',
        # 'js/skel.min.js',
        'js/main.js',
        # 'js/util.js',
        # 'js/csrf-ajax.js',
        # 'js/form.js',
    ),
    'output_filename': 'js/contrib.js',
}

# Contributed / third party css for pipeline compression
# For hand rolled css for this app, use project.py
PIPELINE_CSS = {}
PIPELINE_CSS['contrib'] = {
    'source_filenames': (
        'chosen/chosen.min.css',
        'css/form.css',
        'css/fonts.css',
        'css/font-awesome.min.css',
        'css/main.css'
    ),
    'output_filename': 'css/contrib.css',
    'extra_context': {
        'media': 'screen, projection',
    },
}
# These get enabled in prod.py
PIPELINE_ENABLED = False
PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None

# Django-allauth related settings

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

INSTALLED_APPS += (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
)

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': ['user:email', 'public_repo', 'read:org']
    }
}

SHORT_URL_MIN_LEN = 8
SHORT_URL_MAX_LEN = 15

# Django-host specific settings
#
# # We place django-hosts request middleware first in the tuple.
# MIDDLEWARE_CLASSES = (
#     'django_hosts.middleware.HostsRequestMiddleware',
#     ) + MIDDLEWARE_CLASSES
#
# # And end the list with the response  middleware in the tuple.
# MIDDLEWARE_CLASSES += ('django_hosts.middleware.HostsResponseMiddleware',)
#
# ROOT_HOSTCONF = 'core.hosts'
# DEFAULT_HOST = 'www'
# DEFAULT_REDIRECT_URL = "http://www.shortcode.com:8000"
# PARENT_HOST = "shortcode.com:8000"
#
