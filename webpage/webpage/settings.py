import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
DOTENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(DOTENV_PATH)


SECRET_KEY = os.getenv('SECRET_KEY', default='django-insecure')

DEBUG = os.getenv('DEBUG', default='True') == 'True'

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS', default='*')]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'studies.apps.StudiesConfig',
    'projects.apps.ProjectsConfig',
    'articles.apps.ArticlesConfig',
    'my_profile.apps.MyProfileConfig',

    # 3rd parties
    'storages',
    'rest_framework',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webpage.urls'

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

WSGI_APPLICATION = 'webpage.wsgi.application'


# Database
PG_DATABASE_CONFIG = {
    'ENGINE':   'django.db.backends.postgresql',
    'PORT':     os.getenv('PG_PORT', default=5432),
    'USER':     os.getenv('PG_USER', default='postgres'),
    'NAME':     os.getenv('PG_NAME', default='postgres'),
    'HOST':     os.getenv('PG_HOST', default='localhost'),
    'PASSWORD': os.getenv('PG_PASSWORD', default='postgres'),
}
DATABASES = {'default': PG_DATABASE_CONFIG}

# Password validation
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
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
if DEBUG:
    STATIC_URL  = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MEDIA_URL   = 'media/'
    MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')

else:
    STORAGES = {
        'default':      {'BACKEND': 'storages.backends.s3.S3Storage'},
        'staticfiles':  {'BACKEND': 'storages.backends.s3.S3Storage'}
    }


# AWS
AWS_ACCESS_KEY_ID       = os.getenv("AWS_ACCESS_KEY_ID")
AWS_S3_ENDPOINT_URL     = os.getenv("AWS_S3_ENDPOINT_URL")
AWS_SECRET_ACCESS_KEY   = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CORSHEADERS
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = [os.getenv("CORS_ALLOWED_ORIGINS")]
