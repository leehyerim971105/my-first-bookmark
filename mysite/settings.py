"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dr6w6(6q%2yd+n%ub)w#iih0lh%5g57m!eq32!4+%4=3ki%unh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.pythonanywhere.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark.apps.BookmarkConfig',     # (ch02) bookmark 앱을 추가 등록
    'blog.apps.BlogConfig',             # (ch03) blog 앱을 추가 등록
    'tagging.apps.TaggingConfig',       # (ch07) tagging 앱을 추가 등록
    'disqus',                           # (ch08) 1/4
    'django.contrib.sites',             # (ch08) 2/4
    'photo.apps.PhotoConfig',
]

DISQUS_WEBSITE_SHORTNAME = 'leehyerim1105'   # (ch08) 3/4 [Website Name]
SITE_ID = 1                             # (ch08) 4/4 django.contrib.sites를 등록할 때 사용하는 값, 임의로 지정하지만, 중복되지 않도록!

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 교과서 39 쪽처럼 수정
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'ko-kr'# 'en-us' # 수정 (교과서 40 쪽)
LANGUAGE_CODE = 'en-us' # 원래대로

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'         # 수정 (교과서 40 쪽)

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]   # 추가 (교과서 40 쪽)

MEDIA_URL = '/media/'                             # 추가 (교과서 40 쪽)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')   # 추가 (교과서 40 쪽)

# ch11 1/1 추가
# 로그인 페이지로 리다이렉트시키는 URL이며 login_required() 데코레이터에서 사용함
# LOGIN_URL = '/accounts/login/'        # 기본값 사용
# 로그아웃 페이지로 리다이렉트시키는 URL
# LOGOUT_URL = '/accounts/logout/'      # 기본값 사용
# 장고 기본 로그인 뷰 contrib.auth.login()는 로그인 성공 시
#   next 매개변수로 지정한 URL로 리다이렉트 하는데,
#   만일 next 매개변수가 지정되지 않으면 이 URL로 리다이렉트 시키며,
#   login_required() 데코레이터에서 사용함
LOGIN_REDIRECT_URL = '/'