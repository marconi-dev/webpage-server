import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
DOTENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(DOTENV_PATH)


SECRET_KEY = os.getenv("SECRET_KEY", default="django-insecure")

DEBUG = os.getenv("DEBUG", default="True") == "True"

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS", default="*")]
CSRF_TRUSTED_ORIGINS = [os.getenv("CSRF_TRUSTED_ORIGINS", default="http://*")]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps
    "studies.apps.StudiesConfig",
    "projects.apps.ProjectsConfig",
    "articles.apps.ArticlesConfig",
    "my_profile.apps.MyProfileConfig",
    # 3rd parties
    "storages",
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "webpage.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "webpage.wsgi.application"


# Database
DB_USE_SSL = os.getenv("DB_USE_SSL", default="True") == "True"
MY_SQL_DATABASE_CONFIG = {
    # Defaults to a local mysql instance with a django_db database
    # created. Login as root and use ssl certificate.
    "ENGINE": "django.db.backends.mysql",
    "USER": os.getenv("DB_USER", default="root"),
    "NAME": os.getenv("DB_NAME", default="django_db"),
    "PASSWORD": os.getenv("DB_PASSWORD", default="pass"),
    "PORT": os.getenv("DB_PORT", default=3306),
    "HOST": os.getenv("DB_HOST", default="127.0.0.1"),
    "OPTIONS": {"charset": "utf8mb4"},
}

if DB_USE_SSL:
    MY_SQL_DATABASE_CONFIG["OPTIONS"]["ssl"] = {"ca": os.getenv("MYSQL_ATTR_SSL_CA")}

DATABASES = {"default": MY_SQL_DATABASE_CONFIG}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
if DEBUG:
    STATIC_URL = "static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    MEDIA_URL = "media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

else:
    STORAGES = {
        "default": {"BACKEND": "storages.backends.s3.S3Storage"},
        "staticfiles": {"BACKEND": "storages.backends.s3.S3Storage"},
    }


# AWS
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# CORSHEADERS
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = [os.getenv("CORS_ALLOWED_ORIGINS")]
