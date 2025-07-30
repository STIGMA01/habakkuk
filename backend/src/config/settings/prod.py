"""
In Production Mode

"""
from .base import *


DEBUG = False       # WARNING: DO NOT 'TRUE'

ALLOWED_HOSTS = [
    'awakening-christ.org',
    'www.awakening-christ.org',
    'frontend',     # Docker
]

STATIC_ROOT = '/var/www/web/static/'

# REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
#     'rest_framework.renderers.JSONRenderer'
# ]
# REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = [
#     'rest_framework.permissions.IsAuthenticated'
# ]

CORS_ALLOW_ALL_ORIGINS = False      # WARNING: DO NOT 'TRUE'
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://.*\.awakening-christ\.org$",
]



#-----------------------------
#       Validation
#-----------------------------
additional_patterns = [
    SettingsValidateGeneralPattern('DEBUG', truthiness_check=False, 
                                   type_check=bool, additional_validate_func=lambda value: value==False),      # Check DEBUG must be FALSE
    SettingsValidateGeneralPattern('ALLOWED_HOSTS', truthiness_check=True, type_check=list),                   # ALLOWED_HOSTS
    SettingsValidateGeneralPattern('CORS_ALLOW_ALL_ORIGINS', truthiness_check=False, 
                                   type_check=bool, additional_validate_func=lambda value: value==False),      # CORS_ALLOW_ALL_ORIGINS must be FALSE
]
exec_validate_settings(__name__, additional_patterns)


