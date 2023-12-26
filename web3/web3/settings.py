
import os.path
from pathlib import Path
from py2neo import Graph
from neo4j import GraphDatabase
from neomodel import config
from yandexgptlite import YandexGPTLite


BASE_DIR = Path(__file__).resolve().parent.parent
driver = GraphDatabase.driver("bolt://localhost:7687",
                               auth=("neo4j", "neo4jneo4j"))

NEOMODEL_NEO4J_BOLT_URL = os.environ.get('NEO4J_BOLT_URL', 'bolt://neo4j:neo4jneo4j@localhost:7687')
NEOMODEL_SIGNALS = True
NEOMODEL_FORCE_TIMEZONE = False
NEOMODEL_MAX_CONNECTION_POOL_SIZE = 50


SECRET_KEY = 'django-insecure-=q40gcj5!pcw%zo4enoi%8fxn(6z7$ym5b#1q_sn+dhp5%n@o3'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hodata.apps.HodataConfig',
    'django_neomodel',
    'yandexgptlite'


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web3.urls'

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

WSGI_APPLICATION = 'web3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'neo4j': {
        'ENGINE':   'django.db.backends.neo4j',
        'NAME':     'neo4j',
        'HOST':     'localhost',
        'PORT':     '7687',
        'USERNAME': 'neo4j',
        'PASSWORD': 'neo4jneo4j',
        }
}
NEO4J_DATABASES = {
    'default' : {
        'HOST':'localhost',
        'PORT':7687,
        'ENDPOINT':'/db/data'
    }
}
#
# DATABASES = {
# 'default': {
# 'ENGINE': 'django.db.backends.neo4j',
# 'NAME': 'neo4j',
# 'HOST': 'localhost',
# 'PORT': '7687',
# 'USERNAME': 'neo4j',
# 'PASSWORD': 'neo4jneo4j',
# }
# }

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
