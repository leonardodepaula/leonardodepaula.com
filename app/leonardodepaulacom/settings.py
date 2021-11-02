# Python
from pathlib import Path
import os

# Parâmetros da aplicação
PRODUCAO = bool(int(os.environ.get('PRODUCAO', 0)))

# Base DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key
SECRET_KEY = os.environ.get('SECRET_KEY', 'DUMMY_SECRET_KEY')

# Debug
DEBUG = bool(int(os.environ.get('DEBUG', 1)))

# Allowed Hosts
ALLOWED_HOSTS = []

if PRODUCAO:

    ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS_ENV')
    ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(','))

else:

    ALLOWED_HOSTS.extend(['127.0.0.1'])

# APPS
INSTALLED_APPS = [

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'core.apps.CoreConfig'

]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'leonardodepaulacom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'leonardodepaulacom', 'templates')],
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

WSGI_APPLICATION = 'leonardodepaulacom.wsgi.application'


# Banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
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
USE_L10N = True
USE_TZ = True

# Media
MEDIA_URL = '/media/'

if PRODUCAO:
    MEDIA_ROOT = '/media_files/'
else:
    MEDIA_ROOT = os.path.join(BASE_DIR,'MEDIA/')


# Static
STATIC_URL = '/static/'

if PRODUCAO:
    STATIC_ROOT = '/static_files/'
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'STATIC/')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'),)

# Outras configurações
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
AUTH_USER_MODEL = 'core.User'

# Informações da aplicação
ENGINE_DB = DATABASES.get('default').get('ENGINE')
print(f'leonardodepaula.com | Produção: {PRODUCAO} | DEBUG: {DEBUG} | Allowed Hosts: {ALLOWED_HOSTS} | Banco de dados: {ENGINE_DB}')