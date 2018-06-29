"""
Django settings for mysite_django1 project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^br&e5hs1#kulsgg&zgi-l&n_so%aq1al9zbqvt4nsiw0d6#j0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'user',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'utils.UserAuthMiddleware.UserAuthMiddle'
]

ROOT_URLCONF = 'mysite_django1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mysite_django1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'day01',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 分页条数
PAGE_NUMBERS = 3

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 没有跳转, 跳转地址
LOGIN_URL = '/user/login/'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
    'DEFAULT_AUTHENTICATION_CLASSES': (),
    'DEFAULT_RENDERER_CLASSES': (
        'utils.functions.CustomJsonRenderer',
    ),
    # 配置过滤
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),
}

# # 创建日志保存文件地址
# LOG_PATH = os.path.join(BASE_DIR, 'log')
# # 如果地址日志文件夹不存在,则自动创建
# if not os.path.isdir(LOG_PATH):
#     os.mkdir(LOG_PATH)
#
# LOGGING = {
#     # version 只能为1
#     'version': 1,
#     # disable_existing_loggers 键为True(默认值), 那么默认配置中的所有logger都将禁用.
#     # Logger 的禁用与删除不同; logger仍然存在,但是将默默丢弃任何传递给它的信息,也不会传播给上一级logger
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(massage)s'
#         },
#     },
#     'handlers': {
#         'stu_handlers': {
#             # 如果loggers的处理级别小于handlers的处理级别,则handler忽略该信息
#             'level': 'DEBUG',
#             # 指定文件类型为RotatingFileHandler, 当日志文件的大小超过了maxBytes以后, 就会自动切割
#             'class': 'logging.handlers.RotatingFileHandler',
#             # 输出文件地址
#             'filename': '%s/log.txt' % LOG_PATH,
#             # 使用哪一个日志格式化的配置
#             'formatter': 'verbose',
#             # 指定日志文件的大小为5M, 换算为1m=1024kb, 1kb=1024b
#             'maxBytes': 1024 * 1024 * 5
#         },
#     },
#     'loggers': {
#         'console': {
#           'handlers': ['stu_handlers'],
#           'level': 'INFO',
#           # propagete=0, 表示输出日志, 但消息不传递
#           # propagate=1是输出日志, 同时消息往更高级别的地方传递, root为最高级别
#           'propagate': False
#         },
#     },
# },
#
#

