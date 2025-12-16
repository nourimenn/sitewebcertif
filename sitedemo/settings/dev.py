from .base import *
import os
from dotenv import load_dotenv
load_dotenv()  # charge automatiquement .env à la racine du projet


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-85ma8%6$d!ha8(gbb0tqn3)kz@s@j7fs*k&x@**vzh^w3hd%o"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

WAGTAILIMAGES_JPEG_QUALITY = 100


try:
    from .local import *
except ImportError:
    pass
