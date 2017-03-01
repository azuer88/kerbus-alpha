"""
Django settings for kerbus project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Build paths for webpack and static settings
DJANGO_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = os.path.basename(DJANGO_DIR)
PROJECT_ROOT = os.path.normpath(os.path.join(DJANGO_DIR, "../../../"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ub&1l9*b))7$wr+gn&^j3rx7r2rl5!b$b!^fws9tb2db_(i7jn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'webpack_loader',
    'rest_framework',
    'main',
    'asimplemenu',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kerbus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kerbus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, '../static'))
ASSETS_ROOT = os.path.join(PROJECT_ROOT,'src', 'assets')
STATICFILES_DIR = (
     ('fonts', os.path.join(ASSETS_ROOT, 'fonts')),
     ('images', os.path.join(ASSETS_ROOT, 'images')),
     ('icons', os.path.join(ASSETS_ROOT, 'icons')),
)
BUNDLES_DIR = os.path.join(ASSETS_ROOT, 'bundles', '')

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': BUNDLES_DIR,  # must end with slash
        'STATS_FILE': os.path.join(PROJECT_ROOT, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map'],
    }
}


# split settings:
from local_settings import *
try:
    LOCAL_SETTINGS
except NameError:
    try:
        from local_settings import *  # NOQA W040 1
    except ImportError:
        pass

REST_FRAMEWORK = {
    # Use Django's standard django.contrib.auth permissions
    'DEFAULT_PERMISSION_CLASSES': [
         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'PAGE_SIZE': 10,
}


if not DEBUG:
   BUNDLES_DIR = os.path.join(PROJECT_ROOT, 'src', 'static', 'bundles', '')
   WEBPACK_LOADER['DEFAULT'].update({
      'BUNDLE_DIR_NAME': BUNDLES_DIR,
      'STATS_FILE': os.path.join(PROJECT_ROOT, 'webpack-stats-prod.json'),
   })
