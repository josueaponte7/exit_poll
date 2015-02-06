"""
Django settings for exit_poll project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

RUTA_TEMPLATES = os.path.join(BASE_DIR, 'templates')

RUTA_STATIC = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (RUTA_STATIC,)

TEMPLATE_DIRS = (RUTA_TEMPLATES,)

MEDIA_ROOT = os.path.join(BASE_DIR, 'imagenes')
MEDIA_URL = '/imagenes/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g=rig)fiok%qyr5128t0yng*n^h4w!l7oip3@604gq37(a#gcy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pixelfields_smart_selects',
    'smart_selects',
    'rest_framework',
    'django_extensions',
    'corsheaders',
    'apps.inicio',
    'apps.login',
    'apps.menu',
    'apps.configuraciones',
    'apps.topologia.estados',
    'apps.topologia.municipios',
    'apps.topologia.parroquias',
    'apps.circuitos',
    'apps.grupo_etareo',
    'apps.tipos.categoria_eleccion',
    'apps.tipos.tipo_eleccion',
    'apps.centro_votacion',
    'apps.partidos',
    'apps.elecciones',
    'apps.exitpoll',
    'apps.candidatos'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'exit_poll.urls'

WSGI_APPLICATION = 'exit_poll.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'exit_poll',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
