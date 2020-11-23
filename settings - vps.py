
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!nz^f3aos(cyr*q#zqs+se)u$-7-ars)lr#n71%dm0*o2#!48u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['165.227.94.242', 'localhost']

SITE_ID = 1
# Application definition

INSTALLED_APPS = [
"""
Django settings for mysite project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!nz^f3aos(cyr*q#zqs+se)u$-7-ars)lr#n71%dm0*o2#!48u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['165.227.94.242', 'localhost'] ##put in your url from your digitalocean here

SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
        'blog.apps.BlogConfig',
        'taggit',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'django.contrib.postgres',
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

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject', ##THIS IS THE NAME DATABASE FROM THE MYPROJECTDIR FROM TUTORIAL
        'USER': 'myprojectuser', ##THIS IS THE USER FROM THE MYPROJECTDIR FROM TUTORIAL
        'PASSWORD': 'myprojectuserpassword', ##THIS IS THE PASS FROM THE MYPROJECTDIR FROM TUTORIAL
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarit>
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator>
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidato>
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidat>
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'your_account@gmail.com'

EMAIL_HOST_PASSWORD = 'your_password'

EMAIL_PORT = 587

EMAIL_USE_TLS = True
