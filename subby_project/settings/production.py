from .settings import *
import os
import dj_database_url

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['cp317-w2018-g3.herokuapp.com']

STATICFILES_DIRD = (
    os.path.join(BASE_DIR, 'static')
)

DATABASE_URL = os.environ.get('DATABASE_URL', '')
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require = True)
}
