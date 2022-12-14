"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from urllib.parse import urlparse
from datetime import timedelta
from django.core.management.utils import get_random_secret_key

import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config("SECRET_KEY")
# SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
SECRET_KEY = str(os.getenv("DJANGO_SECRET_KEY", get_random_secret_key()))

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config("DEBUG")
DEBUG = str(os.getenv("DEBUG", "False") == "True")
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOST", "127.0.0.1,localhost").split(",")
# ALLOWED_HOSTS = ["argueapi.synercomgroup.net", "localhost"]
# ALLOWED_HOSTS = [".synercomgroup.net", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "accounts",
    "data_settings",
    "aircraft_template_manager",
    "occurrence_report",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "phonenumber_field",
    "helpers",
    "django_filters",
    "corsheaders",
    "django_rest_passwordreset",
    "import_export",
    "clearcache",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "core.urls"
AUTH_USER_MODEL = "accounts.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "EXCEPTION_HANDLER": "helpers.error_handler.custom_exception_handler",
    # "EXCEPTION_HANDLER": "helpers.custom_error_handler.custom_exception_handler",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=10),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# IMPORT_EXPORT_USE_TRANSACTIONS = True


# Database


# # https://docs.djangoproject.com/en/4.1/ref/settings/#databases


# POSTGRES_DB = str(os.getenv("POSTGRES_DB"))
# POSTGRES_PASSWORD = str(os.getenv("POSTGRES_PASSWORD"))
# POSTGRES_USERNAME = str(os.getenv("POSTGRES_USERNAME "))
# POSTGRES_HOST = str(os.getenv("POSTGRES_HOST"))
# POSTGRES_PORT = str(os.getenv("POSTGRES_PORT"))

# POSTGRES_READY = (
#     POSTGRES_DB is not None
#     and POSTGRES_PASSWORD is not None
#     and POSTGRES_USERNAME is not None
#     and POSTGRES_HOST is not None
#     and POSTGRES_PORT is not None
# )
# if POSTGRES_READY:
#     DATABASES = {
#         "default": {
#             "ENGINE":"django.db.backends.postgresql_psycopg2",
#             "NAME": POSTGRES_DB,
#             "USER": POSTGRES_USERNAME,
#             "PASSWORD": POSTGRES_PASSWORD,
#             "HOST": POSTGRES_HOST,
#             "PORT": POSTGRES_PORT,
#             "OPTIONS": {"sslmode": "require"},
#         }
#     }
# else:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#         }
#     }

POSTGRES_DB = str(os.getenv("POSTGRES_DB"))
POSTGRES_PASSWORD = str(os.getenv("POSTGRES_PASSWORD"))
POSTGRES_USERNAME = str(os.getenv("POSTGRES_USERNAME "))
POSTGRES_HOST = str(os.getenv("POSTGRES_HOST"))
POSTGRES_PORT = str(os.getenv("POSTGRES_PORT"))

DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "False"

if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != "collectstatic":
    # if os.getenv("DATABASE_URL", None) is None:
    #     raise Exception("DATABASE_URL environment variable not defined")
    # DATABASES = {
    #     "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    # }
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": POSTGRES_DB,
            "USER": POSTGRES_USERNAME,
            "PASSWORD": POSTGRES_PASSWORD,
            "HOST": POSTGRES_HOST,
            "PORT": POSTGRES_PORT,
            "OPTIONS": {"sslmode": "require"},
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# EMAIL SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# For printing in Backend Terminal Console
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SENDGRID_API_KEY = str(os.getenv("SENDGRID_API_KEY"))

EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = "apikey"  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = str(os.getenv("DEFAULT_FROM_EMAIL"))


# CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True

CORS_ALLOW_ALL_ORIGINS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Actual directory user files go to
# URL used to access the media
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# MEDIA_ROOT = BASE_DIR + MEDIA_URL

AVIATION_STACK_API_KEY = str(os.getenv("AVIATION_STACK_API_KEY"))