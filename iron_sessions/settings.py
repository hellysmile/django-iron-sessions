import os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def from_env(key):
    return os.environ.get(key, False)


IRON_CACHE_PROJECT_ID = getattr(
    settings, 'IRON_CACHE_PROJECT_ID', from_env('IRON_CACHE_PROJECT_ID')
)
IRON_CACHE_TOKEN = getattr(
    settings, 'IRON_CACHE_TOKEN', from_env('IRON_CACHE_TOKEN')
)
IRON_SESSIONS_BRACKET = getattr(
    settings, 'IRON_SESSIONS_BRACKET', 'iron_sessions'
)


if not (IRON_CACHE_PROJECT_ID and IRON_CACHE_TOKEN):
    raise ImproperlyConfigured(
        '''
        IRON_CACHE_PROJECT_ID or IRON_CACHE_TOKEN
        isnt available from your ENV or settings.py
        '''
    )
