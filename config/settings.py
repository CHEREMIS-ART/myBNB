from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str = "hotel_db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    DEBUG: bool = True
    SECRET_KEY: str = "django-insecure-change-in-production"

    class Config:
        env_file = ".env"


settings = Settings()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = settings.SECRET_KEY
DEBUG = settings.DEBUG

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "rest_framework",
    "src.hotels",
    "src.bookings",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": settings.POSTGRES_DB,
        "USER": settings.POSTGRES_USER,
        "PASSWORD": settings.POSTGRES_PASSWORD,
        "HOST": settings.POSTGRES_HOST,
        "PORT": settings.POSTGRES_PORT,
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
}
