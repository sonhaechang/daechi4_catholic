import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

PROJECT_APPS += []

THIRD_PARTY_APPS += []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('DB_USER'),
        'PASSWORD': get_secret('DB_PASSWORD'),
        'HOST': 'localhost',
        # 'HOST': get_secret('DB_HOST'),
        'PORT': get_secret('DB_PORT'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')
AWS_REGION = get_secret('AWS_REGION')
AWS_STORAGE_BUCKET_NAME = get_secret('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400',}
AWS_LOCATION = 'static'
AWS_MEDIA_LOCATION = 'media'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_USE_SSL = True

STATICFILES_DIRS = [BASE_DIR / 'static']

# TODO: production에서 /var/log/django와 django.log가 permission denied 발생 확인 필요 수정후 주석 해제 필요
# Django Logging
# LOG_FILE = '/var/log/django/django.log'
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
#         },
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'logfile': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': LOG_FILE,
#             'when': "midnight",  # 매 자정마다
#             'backupCount': 31,
#             'formatter': 'standard',
#         },
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#     },
#     # Loggers (where does the log come from)
#     'loggers': {
#         'repackager': {
#             'handlers': ['console', 'logfile'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django': {
#             'handlers': ['console', 'logfile'],
#             'propagate': True,
#             'level': 'WARN',
#         },
#         'django.server': {
#             'handlers': ['console', 'logfile'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'django.db.backends': {
#             'handlers': ['console', 'logfile'],
#             'level': 'WARN',
#             'propagate': False,
#         },
#         '': {
#             'handlers': ['console', 'logfile'],
#             'level': 'DEBUG',
#         },
#         'raven': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#             'propagate': False,
#         },
#         'sentry.errors': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#             'propagate': False,
#         },
#         'gunicorn.error': {
#             'level': 'INFO',
#             'handlers': ['logfile'],
#             'propagate': True,
#         },
#         'gunicorn.access': {
#             'level': 'INFO',
#             'handlers': ['logfile'],
#             'propagate': False,
#         },
#         'django.request': {
#             'handlers': ['logfile'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#     }
# }
