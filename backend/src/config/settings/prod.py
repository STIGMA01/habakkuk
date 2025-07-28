# settings/production.py
from .base import *

DEBUG = False       # WARNING: DO NOT 'TRUE'

ALLOWED_HOSTS = []

STATIC_ROOT = '/var/www/web/static/'

# REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
#     'rest_framework.renderers.JSONRenderer'
# ]
# REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = [
#     'rest_framework.permissions.IsAuthenticated'
# ]

CORS_ALLOW_ALL_ORIGINS = False      # WARNING: DO NOT 'TRUE'
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://.*\.awakening-christ\.net$",
]


