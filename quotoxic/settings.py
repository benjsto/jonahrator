from djangoappengine.settings_base import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import nltk

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'ron_quixote'

# DEBUG = DEBUG
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []

base_path = os.getcwdu()
nltk.data.path.append(base_path + "/nltk_data")

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'djangotoolbox',
    'nltk',
    'quotoxic',
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

DATABASES = {}

ROOT_URLCONF = 'quotoxic.urls'

WSGI_APPLICATION = 'quotoxic.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_TZ = True

USE_I18N = True
USE_L10N = True

STATIC_URL = '/static/'
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'frontend/app'),)
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'frontend'),)
