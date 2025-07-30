"""
Development settings

"""
from .base import *


DEBUG = True

ALLOWED_IPS = [
    'localhost',
    '127.0.0.1',
    '::1',
    'frontend',       # Docker service name
    '172.17.0.0/16',  # Docker 기본 브리지
    '172.18.0.0/16',  # Docker Compose
]


CORS_ALLOW_ALL_ORIGINS = True



#-----------------------------
#       Validation
#-----------------------------
additional_patterns = [
]
exec_validate_settings(__name__, additional_patterns)


