"""
Django settings for sample project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import ast

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if not os.environ.get("ENV", None):
    from dotenv import load_dotenv

    load_dotenv("../.sample-env")

SECRET_KEY = os.environ.get(
    "SECRET_KEY", "4g^+patmx=&8kbyenh=vy7uycv-jp049y@qq=^)5mf%gz*$7i@"
)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ast.literal_eval(os.getenv("DEBUG", "True"))

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = ["django.contrib.staticfiles", "stars"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sample.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "sample.wsgi.application"

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = "/static/"

if not DEBUG:
    # aws settings
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=34608000",
    }
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_ACL = "public-read"
    AWS_QUERYSTRING_AUTH = False
    # CLOUDFRONT_DOMAIN = os.environ["CLOUDFRONT_DOMAIN"]
    # CLOUDFRONT_ID = os.environ.get("CLOUDFRONT_ID")
    # AWS_S3_CUSTOM_DOMAIN = CLOUDFRONT_DOMAIN
    # s3 static settings
    AWS_LOCATION = "static"
    # STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
    STATICFILES_STORAGE = "sample.customstorage.CustomManifestS3Boto3Storage"
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

NASA_API_URL = "https://api.nasa.gov/"
NASA_API_KEY = os.environ.get("NASA_API_KEY", "DEMO_KEY")
