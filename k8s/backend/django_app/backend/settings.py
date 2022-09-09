"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from apps.core.utils import get_value_env as env
import warnings
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
if not env('SECRET_KEY'):
    warnings.warn((
                      "Please define SECRET_KEY before importing {0}, as a fallback "
                      "for when the environment variable is not available."
                  ).format(__name__))
else:
    SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG", True)

ALLOWED_HOSTS = ['*']


#############################################
#  Application definition
#############################################

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # Third apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'rest_framework',
    'django_filters',

    'corsheaders',
    'bootstrap4',
    'webpack_loader',

    # Own apps
    'apps.core',
    'apps.request_loan'
]

#############################################
#  MIDDLEWARE
#############################################
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

CORS_ORIGIN_ALLOW_ALL = True


# if env("ENVIRONMENT", "local") == 'local':
#    MIDDLEWARE.append('apps.core.middleware.dev_cors_middleware')

#############################################
#  TEMPLATES CONFIG
#############################################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "backend/templates"),
        ],
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

WSGI_APPLICATION = 'backend.wsgi.application'
ROOT_URLCONF = 'backend.urls'


#############################################
# DATABASE CONFIG
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#############################################
DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

#############################################
#  AUTHENTICATION CONFIG
#############################################

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/dashboard/'

LOGOUT_REDIRECT_URL = LOGIN_URL

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https' if env('ENVIRONMENT', 'local') != 'local' else 'http'

ACCOUNT_FORMS = {'login': 'apps.user.forms.MyCustomLoginForm'}

#############################################
# LOCALES & LANG
#############################################

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################
# STATIC FILESstaticfiles
#############################################
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "../static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "backend/static"),
    os.path.join(BASE_DIR, "assets"),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]


#############################################
# DJANGO REST FRAMEWORK CONFIG
#############################################

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'apps.core.pagination.CustomPageNumberPagination',
    'PAGE_SIZE': 5
}

#############################################
# WEBPACK TO RENDER REACT
#############################################

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.dev.json') if env('ENVIRONMENT', 'local') == 'local'
        else os.path.join(BASE_DIR, 'webpack-stats.prod.json'),
    },
}

if env("ENVIRONMENT", "local") != 'local':
    COMPRESS_OFFLINE = True

BASE_URL = env('BASE_URL')
SITE_ID = env('SITE_ID')