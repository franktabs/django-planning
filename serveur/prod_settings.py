from re import TEMPLATE
from .settings import *
import dj_database_url

DEBUG = True

TEMPLATE_DEBUG = True

SECRET_KEY = "d!27&+0*fw30)6=0w6x)5(6(a0y_oah+47kf-d6gjr82e^0jm("

ALLOWED_HOSTS = [ '127.0.0.1', 'https://planning-ap.herokuapp.com', '.herokuapp.com', '192.168.8.102', '192.168.8.101', 'localhost']

DATABASES['default']= dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'