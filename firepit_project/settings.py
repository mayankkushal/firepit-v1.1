"""
Django settings for firepit_project project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from oscar.defaults import *
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar import get_core_apps
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.contrib.admin import AdminSite

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!@v+mq-irmx^s59jr^8&0&kf$!f8s2a3rz%t!bb&l%(59(obm+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'firepit',
    'compressor',
    'widget_tweaks',
    'cloudinary',
    'social_django',
    'blog',
    'django_extensions',
    'newsletter',
] + get_core_apps( ['apps.catalogue','apps.basket', 'apps.address', 'apps.dashboard', 'apps.dashboard.catalogue', 
                    'apps.checkout', 'apps.search'])


SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'firepit_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, OSCAR_MAIN_TEMPLATE_DIR ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'firepit_project.wsgi.application'


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#Haystack search
'''HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
    },
}'''
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
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


AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.twitter.TwitterOAuth',
)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [STATIC_DIR, ]


#Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# Cloudinary config
# Cloudinary config
cloudinary.config( 
  cloud_name = "dvqjn4lzj", 
  api_key = "124346914869879", 
  api_secret = "5NZeAMeGO1QDowm8o8NperSewhE" 
)

from django.utils.translation import ugettext_lazy as _

# Oscar settings

#order pipeline
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

OSCAR_CURRENCY_LOCALE = 'en_US'
OSCAR_DEFAULT_CURRENCY = u'INR' 
OSCAR_CURRENCY_FORMAT = u'₹ #,##0' 

OSCAR_SEND_REGISTRATION_EMAIL = False

OSCAR_SHOP_NAME = 'FIREPIT'
OSCAR_SHOP_TAGLINE = 'You Think, We Provide'

# allow anonymous
OSCAR_ALLOW_ANON_REVIEWS = False
OSCAR_ALLOW_ANON_CHECKOUT = False

OSCAR_ACCOUNTS_REDIRECT_URL = 'customer:profile-update' #after registration redirect to edit

OSCAR_DASHBOARD_NAVIGATION += [
    {
        'label': _('Store Manager'),
        'icon': "icon-building",
        'children': [
            {
                'label': _('Stores'),
                'url_name': 'dashboard:store_list',
            }
         ],
    },
]

# search filters
OSCAR_SEARCH_FACETS = {
    'fields': OrderedDict([
        ('product_class', {'name': _('Type'), 'field': 'product_class'}),
        ('rating', {'name': _('Rating'), 'field': 'rating'}),
    ]),
    'queries': OrderedDict([
        
    ]),
}




# Image folder destination
from datetime import date
today = date.today()
today_path = today.strftime("%Y/%m/%d") ## this will create something like "2011/08/30"
path = 'images/products/'
OSCAR_IMAGE_FOLDER = os.path.join(path, today_path)

# email backends
OSCAR_FROM_EMAIL = 'something@firepit.in' #to be changed
OSCAR_STATIC_BASE_URL = 'firepit.in'
NEWSLETTER_CONFIRM_EMAIL = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# admin settings

AdminSite.site_header = 'FIREPIT administration'
AdminSite.site_title = 'FIREPIT Site Admin'
AdminSite.index_title = 'FIREPIT Administration'




#for deploying 
import dj_database_url
DATABASES = { 'default': dj_database_url.config() }
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass
