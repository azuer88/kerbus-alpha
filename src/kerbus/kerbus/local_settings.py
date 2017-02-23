LOCAL_SETTINGS = True

# local settings follows

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ub&1l9*b))7$wr+gn&^j3rx7r2rl5!b$b!^fws9tb2db_(i7jn'

# enable django-debug-toolbar: run `pip install django-debug-toolbar`
from settings import MIDDLEWARE, INSTALLED_APPS

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1',)
INSTALLED_APPS += ('debug_toolbar',)
