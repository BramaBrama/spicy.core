from django.conf import settings

USE_CUSTOM_ADMIN = getattr(settings, 'USE_CUSTOM_ADMIN', True)

SITESKIN = getattr(settings, 'SITESKIN', 'example.com')
SITESKIN_ADMIN = getattr(settings, 'SITESKIN_ADMIN', 'spicy-admin')

OBJECTS_PER_PAGE = getattr(settings, 'OBJECTS_PER_PAGE', 50)
ADMIN_OBJECTS_PER_PAGE = getattr(settings, 'ADMIN_OBJECTS_PER_PAGE', 50)

PAGES_FROM_START = getattr(settings, 'PAGES_FROM_START', 2)
PAGES_TO_END = getattr(settings, 'PAGES_TO_END', 2)

CACHE_PREFIX = getattr(settings, 'CACHE_PREFIX', 'sk')
CACHE_TIMEOUT = getattr(settings, 'CACHE_TIMEOUT', 1*60)

DEBUG_ERROR_PAGES = getattr(settings, 'DEBUG_ERROR_PAGES', False)

DEFAULT_TEMPLATE = getattr(settings, 'DEFAULT_TEMPLATE', '/')

SITEMAP_URL = getattr(settings, 'SITEMAP_URL', '/')
SITEMAP_GZIP_COMPRESSION = 6 # Must be in 1-9 interval, 1 is fastest.

MAX_MESSAGE_STRING_LENGTH = 1000

ENABLE_INSERT_BLOCK = getattr(settings, 'ENABLE_INSERT_BLOCK', True)
INSERT_BLOCK_DEFAULT_SIZE = getattr(settings, 'INSERT_BLOCK_DEFAULT_SIZE', 500)

SITESKIN_INDEX_VIEW = getattr(settings, 'SITESKIN_INDEX_VIEW', 'spicy.core.siteskin.views.render')

# == move contetn block
USE_RENDER_FROM_RESPONSE_LIKE_SSI = getattr(settings, 'USE_RENDER_FROM_RESPONSE_LIKE_SSI', True)
