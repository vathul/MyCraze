"""
Django settings for sase project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0zthi*rhgfo+5#pzj#4wzzsp18iyi!l5tpza=3jc1+ybexd4&)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	  'mycraze',
    'social.apps.django_app.default'
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.request',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.github.GithubOAuth2',
   'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mycraze',
        'USER':'root',
        'PASSWORD':'Sr!Kr!shnan123',
        'HOST':'localhost',
        'PORT':'3306'
    }
}

ROOT_URLCONF = 'sase.urls'

WSGI_APPLICATION = 'sase.wsgi.application'

#Django Auth Configuration
LOGIN_URL = '/mycraze/login'
LOGOUT_URL = '/mycraze/logout'

#Social Auth Configuration
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/mycraze/user-resume/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/mycraze/profile-complete/'

# Google Project Details
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '723821424184-b4fatepotlc14bkhkg3fkg0po4hp7flt.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '-vS3QVozqTx8TBK72ARvtXQ6'

#Facebook Project Details
SOCIAL_AUTH_FACEBOOK_KEY = '784705508290213'
SOCIAL_AUTH_FACEBOOK_SECRET = '27ff2c6ed2e53a73e7d240fa81a3dbda'

#Github Project Details
SOCIAL_AUTH_GITHUB_KEY = 'cb4ccb6a648aaa4f57f7'
SOCIAL_AUTH_GITHUB_SECRET = 'c5de7d07f0aef56037c2a9a15843231deb1bcf14'



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Template

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

PROFILE_IMAGES_DIR = '/var/www/html/'