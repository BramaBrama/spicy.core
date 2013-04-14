# -*- coding: utf-8 -*-

import re

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from spicy.utils.html import make_slug

USERNAME_MAX_LENGTH = getattr(settings, 'USERNAME_MAX_LENGTH', 100)

SHA1_RE = getattr(settings, 'SHA1_RE', re.compile('^[a-f0-9]{40}$'))

CUSTOM_USER_MODEL = getattr(settings, 'CUSTOM_USER_MODEL', 'profile.TestProfile')

ACCOUNT_ACTIVATION_DAYS = getattr(settings, 'ACCOUNT_ACTIVATION_DAYS', 2)

CHECK_USER_AGREEMENT = getattr(settings, 'CHECK_USER_AGREEMENT', False)
REGISTRATION_ENABLED = getattr(settings, 'REGISTRATION_ENABLED', True)

# django.contrib.auth required settings

settings.LOGIN_URL = '/signin/'
settings.LOGIN_REDIRECT_URL = '/'
settings.LOGOUT_URL = '/signout/'

# social-auth patch
settings.SOCIAL_AUTH_USERNAME_FIXER = make_slug

REASSOCIATION_TIMEOUT = getattr(settings, 'REASSOCIATION_TIMEOUT', 300)
# How many seconds will we let user to start reassociation with existing
# profile after authorization in a social network.


PASSWORD_HASH_KEY = '_PASSWORD_HASH'



BRUTEFORCE_CHECK = getattr(settings, 'BRUTEFORCE_CHECK', False)

BRUTEFORCE_SOFT_LIMIT = 5
BRUTEFORCE_SOFT_PERIOD = 300
BRUTEFORCE_HARD_LIMIT = 20
BRUTEFORCE_HARD_PERIOD = 3600

AUTH_ALLOW, AUTH_WARN, AUTH_DISALLOW = range(3)


ACCESS_CACHE_PREFIX = 'access-cache'
ACCESS_CACHE_PERIOD = 60 # Period for tracking doc access, in seconds.
ACCESS_RELOAD_PERIOD = 10 # Period for reloading doc access info in admin.

ACCESS_LEVEL = (
    (0, _('Public for web')),
    (1, _('Is visible for user of this web site domain only')),
    (2, _('Only my friends have access')),
    (3, _('Only for me. Access restricted.')),
    (4, _('Only prepaid access is avalable')),
)

DEFAULT_ACCESS_LEVEL = 0

MESSAGE_NOTIFICATION, MESSAGE_FREQUEST, MESSAGE_MESSAGE, MESSAGE_EVENT = range(4)
MESSAGE_TYPE = (
    (MESSAGE_NOTIFICATION, _('Notification')),
    (MESSAGE_FREQUEST, _('Friend request')),
    (MESSAGE_MESSAGE, _('Message')),
    (MESSAGE_EVENT, _('Event')),
)

DEFAULT_MESSAGE_TYPE = 0

MAX_INVITES = getattr(settings, 'MAX_INVITES', 10)

TAG_EDIT_MIN_SCORE = getattr(settings, 'TAG_EDIT_MIN_SCORE', 10)

DEFAULT_PROFILE_URL = getattr(
    settings, 'DEFAULT_PROFILE_URL', lambda u: u.get_absolute_url())
