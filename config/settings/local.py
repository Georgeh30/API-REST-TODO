from .base import *
from config.settings import db

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] # https://docs.djangoproject.com/es/4.1/ref/settings/

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = db.SQLITE # db.SQLITE # db.POSTGRESQL # db.MYSQL


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# STATICFILES_DIRS = (BASE_DIR, 'static') # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')