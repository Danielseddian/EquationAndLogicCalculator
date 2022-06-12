from dotenv import dotenv_values
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ENVS = dotenv_values(BASE_DIR/".env")

SECRET_KEY = ENVS.get("DJANGO_SECRET_KEY", "django-insecure")

DEBUG = ENVS.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = ENVS.get("ALLOWED_HOSTS", "*").split()

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

LOGIN_REDIRECT_URL = "application:index"

LOGOUT_REDIRECT_URL = "application:index"

USE_I18N = True

USE_TZ = True

STATIC_URL = "backend_static/"

STATIC_ROOT = BASE_DIR/"backend_static"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "EquationAndLogicCalculator.urls"

WSGI_APPLICATION = "EquationAndLogicCalculator.wsgi.application"

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "application.apps.ApplicationConfig",
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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


DATABASES = {
    "default": {
        'ENGINE': ENVS.get("DB_ENGINE", 'django.db.backends.postgresql_psycopg2'),
        'NAME': ENVS.get("DB_NAME", 'postgres'),
        'USER': ENVS.get("DB_USER", 'postgres'),
        'PASSWORD': ENVS.get("DB_PASS", 'postgres'),
        'HOST': ENVS.get("DB_HOST", 'localhost'),
        'PORT': ENVS.get("DB_PORT", '5432'),
    }
}

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
