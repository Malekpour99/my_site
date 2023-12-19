# Prodection Configuration

from my_site.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ne0c2=(4*u1k5p+m)zxz46l8k1&gzwse7^n)j=!j7wgdr-m&$w"

# Securing CSRF token in the cookie
CSRF_COOKIE_SECURE = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["themalekpour.com", "www.themalekpour.com"]

# INSTALLED_APPS # if required

# Sites
SITE_ID = 2

# Custom backend settings for authentication
AUTHENTICATION_BACKENDS = ["accounts.backends.MyBackend"]

# SMTP service configuration for sending emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'malekpour.projects@gmail.com'
EMAIL_HOST_PASSWORD = 'app_password'

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

STATICFILES_DIRS = [BASE_DIR / "statics"]

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