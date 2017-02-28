LOCAL_SETTINGS = True
DEBUG = True

# local settings follows

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'change-this-to-some-random-UID-value'

# enable django-debug-toolbar: run `pip install django-debug-toolbar`
from settings import MIDDLEWARE, INSTALLED_APPS

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1',)
INSTALLED_APPS += ('debug_toolbar',)
