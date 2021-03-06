"""
Django settings for Autotest_platform project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import djcelery
from celery.schedules import crontab
from datetime import timedelta

djcelery.setup_loader()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#zpo_me0s492$q_8-2qav%53jx+965%3qx9j0eyqzf8yx=%%rr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'Product',
    'Admin',
]

# AUTH_USER_MODEL = 'Product.User'

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Autotest_platform.urls'

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

WSGI_APPLICATION = 'Autotest_platform.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'autotest1',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST':'192.168.99.100',
        'PORT':'3306',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
# BROKER_URL = 'amqp://guest:guest@localhost:5672'
# CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost:5672'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


#   定时调用Product.tasks.timingRunning
CELERYBEAT_SCHEDULE = {
    'timing': {
        'task': 'Product.tasks.timingRunning',
        # 'schedule': crontab(hour=10, minute=30),
        'schedule': timedelta(seconds=300),
    },
}

CELERY_TASK_RESULT_EXPIRES = 7200  # celery任务执行结果的超时时间，
CELERYD_CONCURRENCY = 1 if DEBUG else 10 # celery worker的并发数 也是命令行-c指定的数目 根据服务器配置实际更改 一般25即可
CELERYD_MAX_TASKS_PER_CHILD = 100  # 每个worker执行了多少任务就会死掉，我建议数量可以大一些，比如200


EMAIL_SEND_USERNAME = '790844153@qq.com'  # 定时任务报告发送邮箱，支持163,qq,sina,企业qq邮箱等，注意需要开通smtp服务
EMAIL_SEND_PASSWORD = 'nrzwklhaietbbfdb'     # 邮箱密码

# AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')