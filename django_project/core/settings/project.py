# coding=utf-8

"""Project level settings.

Adjust these values as needed but don't commit passwords etc. to any public
repository!
"""

from .contrib import *  # noqa


# Project apps
INSTALLED_APPS += (
    'core',
    'shortcode',
)

# Due to profile page does not available,
# this will redirect to home page after login
LOGIN_REDIRECT_URL = '/'

# How many versions to list in each project box
PROJECT_VERSION_LIST_SIZE = 10

# Set debug to false for production
DEBUG = TEMPLATE_DEBUG = True

SOUTH_TESTS_MIGRATE = False


# Project specific javascript files to be pipelined
# For third party libs like jquery should go in contrib.py
PIPELINE_JS['project'] = {
    'source_filenames': (
        'js/urlshort.js',
    ),
    'output_filename': 'js/project.js',
}

# Project specific css files to be pipelined
# For third party libs like bootstrap should go in contrib.py
PIPELINE_CSS['project'] = {
    'source_filenames': (
        'css/urlshort.css',
    ),
    'output_filename': 'css/project.css',
    'extra_context': {
        'media': 'screen, projection',
    },
}
