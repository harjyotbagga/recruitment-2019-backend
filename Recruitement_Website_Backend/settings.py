"""
Django settings for Recruitement_Website_Backend project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j!3+^8uj9@-16y4yh&d(c+*%o#nzqcq$r%6re5omz#qe7g=l)r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',
	'rest_framework',
	'rest_framework.authtoken',
	'rest_auth',
	'allauth',
	'allauth.account',
	'rest_auth.registration',
	'rest_framework_recaptcha',
	'corsheaders',
	'candidate.apps.CandidateConfig',
	'recruiter.apps.RecruiterConfig',
	'drf_yasg',
	'questions.apps.QuestionsConfig'
]

SITE_ID = 1

REST_FRAMEWORK = {
	'DEFAULT_THROTTLE_CLASSES': [
		'rest_framework.throttling.AnonRateThrottle',
		'rest_framework.throttling.UserRateThrottle',
		'rest_framework.throttling.ScopedRateThrottle'
	],

	'DEFAULT_THROTTLE_RATES': {
		'anon': '10/min',
		'user': '10/min',
		'candidate': '30/min',
		'recruiter': '15/min'
	},

	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
	),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
		'rest_framework.authentication.SessionAuthentication',
		'rest_framework.authentication.BasicAuthentication',
	),

	'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',

	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 2
}

AUTH_USER_MODEL = 'recruiter.User'

MIDDLEWARE = [
	#'corsheaders.middleware.CorsMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sambanmicro1203@gmail.com'
EMAIL_HOST_PASSWORD = 'Sameeran1203'

ROOT_URLCONF = 'Recruitement_Website_Backend.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')]
		,
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

WSGI_APPLICATION = 'Recruitement_Website_Backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},

	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# Activate Django-Heroku.
django_heroku.settings(locals())

if 'DATABASE_URL' in os.environ:
	import dj_database_url

	DATABASES = {'default': dj_database_url.config()}


DRF_RECAPTCHA_SECRET_KEY = '6LcRH8YUAAAAAGa4c2EDgU0iN623TZEG--Ldo-Am'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
