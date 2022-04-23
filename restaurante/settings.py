"""
Django settings for restaurante project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
from os import environ
from dotenv import load_dotenv
# https://cloudinary.com/documentation/django_integration#installation
# para crear la configuracion  entre mi proyecto y cloudinary
import cloudinary
# indicar que subire imagenes
import cloudinary.uploader
# usar la api de cloudinary
import cloudinary.api

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&dxzvas@-j7m*cxy6808$bsc2&z*935m@8+bm92@#vg#!t&p*^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# Host que van a poder levantar la API
ALLOWED_HOSTS = ['localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Librerias
    'rest_framework',
    'cloudinary',
    'corsheaders',
    # Aplicaciones
    'autorizacion',
    'fact_electr',
    'menu',
]

# esta en la documentacion http://whitenoise.evans.io/en/stable/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # agregar el middleware de los cors hasta antes del CommonMiddleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restaurante.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'restaurante.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('DB_NAME'),
        'PASSWORD': environ.get('DB_PASSWORD'),
        'USER': environ.get('DB_USER'),
        'HOST': environ.get('DB_HOST'),
        'PORT': environ.get('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# sirve para definir cuando modificamos el contenido del modelo auth_user undicar ahora cual tiene que hacer caso
AUTH_USER_MODEL = 'autorizacion.Usuario'

# Sirve para toda la configuración de nuestro DjangoRestFramework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# sirve para modificar las configuraciones iniciales de simplejwt
SIMPLE_JWT= {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1, minutes=5),
    'ALGORITHM': 'HS384',
}

cloudinary.config(
    cloud_name=environ.get('CLOUDINARY_NAME'),
    api_key=environ.get('CLOUDINARY_KEY'),
    api_secret=environ.get('CLOUDINARY_SECRET'),
)

# esta en la documentacion http://whitenoise.evans.io/en/stable/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# para saber donde se guardaran los archivos estaticos(css, js, imagenes)usados por DRF, y el panel administrativo
# se usa para cuando corramos el comando 'python manage.py collectstatic'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# CORS_ORIGIN_ALLOW_ALL=True
# son los origenes permitidos si queremos usar todos usaremos LO DE ARRIBA
CORS_ALLOWED_ORIGINS=['http://127.0.0.1:5500']
# son los metodos permitidos, por defecto son todas
CORS_ALLOWED_METHODS=['GET','POST'] # no podrá > PUT | DELETE
# Son las cabeceras permitidas, por defecto todas
CORS_ALLOWED_HEADERS=['content-type','authorization','origin']