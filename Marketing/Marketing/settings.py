"""
Django settings for Marketing project.

Generated by 'django-admin startproject' using Django 3.0.6.

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
SECRET_KEY = '5_#t*k^+ha56$i1-oo62p(b4bfrr&vv^o#zlkzo(pia#8m&)t#'

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
    'analysis',
    'analysis.templatetags',
    'captcha',
]

CAPTCHA_NOISE_FUNCTIONS = (
    # 'captcha.helpers.noise_null', #没有樣式
    'captcha.helpers.noise_arcs',  # 線
    'captcha.helpers.noise_dots',  # 點
)

# CAPTCHA_IMAGE_SIZE = (150, 70) #圖片大小
# CAPTCHA_BACKGROUND_COLOR = '#00ff00' #背景頻色

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge' #圖片為英文字母
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge' #圖片中為數學計算式

CAPTCHA_LENGTH = 6 #英文字母個數

# CAPTCHA_TIMEOUT = 1 #時間限制(分)

FILE_UPLOAD_HANDLERS = (
    "django_excel.ExcelMemoryFileUploadHandler",
    "django_excel.TemporaryExcelFileUploadHandler"
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Marketing.urls'

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

WSGI_APPLICATION = 'Marketing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Marketing',
        'USER': 'admin',
        'PASSWORD':'cycug02Marketing0914',
        'HOST':'innovation-marketing.ccyobfykchsy.ap-northeast-2.rds.amazonaws.com',
        'PORT':'3306',
    }
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


LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 指定上傳的檔案存放位置
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 獲取上傳的檔案的url
MEDIA_URL = '/media/'

IMPORT_EXPORT_USE_TRANSACTIONS = True

# Session setting
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_AGE = 1800

