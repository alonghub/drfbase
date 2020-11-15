"""
Django settings for drf project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
    'cmdb'
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

ROOT_URLCONF = 'drf.urls'

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

WSGI_APPLICATION = 'drf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'along_cmdb',
#         'USER': 'cmdb_dba',
#         'PASSWORD': 'oqj53PA2xZyn3EaD',
#         'HOST': '192.168.200.102',
#         'PORT': '3306'
#     }
# }

import dj_db_conn_pool

# dj_db_conn_pool.setup(pool_size=100, max_overflow=50)

if os.getenv('DRF_ENV') == 'prod':
    DATABASES = {
        'default': {
            'ENGINE': 'dj_db_conn_pool.backends.mysql',
            'POOL_OPTIONS': {
                'POOL_SIZE': 100,
                'MAX_OVERFLOW': 50
            },
            'NAME': 'along_cmdb',
            'USER': 'cmdb_dba',
            'PASSWORD': 'oqj53PA2xZyn3EaD',
            'HOST': '192.168.200.102',
            'PORT': '3306'
        },

        'cmdb': {
            'ENGINE': 'dj_db_conn_pool.backends.mysql',
            'NAME': 'along_cmdb',
            'USER': 'cmdb_dba',
            'PASSWORD': 'oqj53PA2xZyn3EaD',
            'HOST': '192.168.200.102',
            'PORT': '3306'
        }
    }
elif os.getenv('DRF_ENV') == 'test':
    DATABASES = {
        'default': {
            'ENGINE': 'dj_db_conn_pool.backends.mysql',
            'NAME': 'along_cmdb',
            'USER': 'cmdb_dba',
            'PASSWORD': 'oqj53PA2xZyn3EaD',
            'HOST': '192.168.200.102',
            'PORT': '3306'
        },

        'cmdb': {
            'ENGINE': 'dj_db_conn_pool.backends.mysql',
            'NAME': 'along_cmdb',
            'USER': 'cmdb_dba',
            'PASSWORD': 'oqj53PA2xZyn3EaD',
            'HOST': '192.168.200.102',
            'PORT': '3306'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'dj_db_conn_pool.backends.mysql',
            'POOL_OPTIONS': {
                'POOL_SIZE': 10,
                'MAX_OVERFLOW': 10
            },
            'NAME': 'along_cmdb',
            'USER': 'cmdb_dba',
            'PASSWORD': 'oqj53PA2xZyn3EaD',
            'HOST': '192.168.200.102',
            'PORT': '3306'
        },

        'cmdb': {
            'ENGINE': 'dj_db_conn_pool.backends.mysql',
            'POOL_OPTIONS': {
                'POOL_SIZE': 10,
                'MAX_OVERFLOW': 10
            },
            'NAME': 'along_cmdb',
            'USER': 'cmdb_dba',
            'PASSWORD': 'oqj53PA2xZyn3EaD',
            'HOST': '192.168.200.102',
            'PORT': '3306'
        }
    }

# 设置数据库的路由规则方法
DATABASES_ROUTERS = ['drf.database_router.DatabaseAppsRouter']

# 设置APP对应的数据库路由表，哪个app要连接哪个数据库，没有指定会用default那个
DATABASES_APPS_MAPPING = {
    'cmdb': 'cmdb'
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # 全局使用的认证类
    "DEFAULT_AUTHENTICATION_CLASSES": ["api.utils.auth.Authentication"],
    #
    # 全局使用的权限类
    "DEFAULT_PERMISSION_CLASSES": ['api.utils.permission.MyPermission'],
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),

    # 全局解析器
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser", "rest_framework.parsers.FormParser"]
}

# Redis
if os.getenv('DRF_ENV') == 'prod':
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/2",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "CONNECTION_POOL_KWARGS": {"max_connections": 1000},
                "PASSWORD": "1qaz!QAZ",
            }
        }
    }
elif os.getenv('DRF_ENV') == 'test':
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/2",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "CONNECTION_POOL_KWARGS": {"max_connections": 300},
                "PASSWORD": "",
            }
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/2",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "CONNECTION_POOL_KWARGS": {"max_connections": 300},
                "PASSWORD": "",
            }
        }
    }
