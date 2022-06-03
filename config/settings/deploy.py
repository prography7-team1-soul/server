from config.settings.base import *

ALLOWED_HOSTS = ['*']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('NAME'),
        'HOST': env('HOST'),
        'USER': env('USER'),
        'PASSWORD': env('PASSWORD'),
        'PORT': env('PORT'),
    }
}