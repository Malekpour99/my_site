# Development Configuration 

from my_site.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ne0c2=(4*u1k5p+m)zxz46l8k1&gzwse7^n)j=!j7wgdr-m&$w"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Redirecting to coming soon template
COMING_SOON = False  # Set to False when you are ready to launch

ALLOWED_HOSTS = []

# INSTALLED_APPS # if required

# Sites
SITE_ID = 2

# Custom backend settings for authentication
AUTHENTICATION_BACKENDS = ["accounts.backends.MyBackend"]

# Using console based Email message to reset password, instead of SMTP Service
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [
    BASE_DIR / "statics"
]

# Django Debug Toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# Django summernote settings
# X_FRAME_OPTIONS = "SAMEORIGIN"
SUMMERNOTE_THEME = 'bs4'
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,
    }
}