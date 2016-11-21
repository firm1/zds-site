# coding: utf-8

# Zeste de Savoir settings file for production
# WARNING: this file MUST be secret !!

import os

from settings import ZDS_APP, INSTALLED_APPS


##### Django settings #####

# NEVER set this True !!
DEBUG = False

USE_L10N = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zds_db',
        'USER': 'zds_user',
        'PASSWORD': 'zds_password',  # KEEP THIS SECRET !!
        'HOST': 'localhost',
        'PORT': '',
        'CONN_MAX_AGE': 600,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# KEEP THIS SECRET !!
SECRET_KEY = 'to-fill'

INSTALLED_APPS += (
    # Sentry client (errors logs)
    'raven.contrib.django.raven_compat',
)

ALLOWED_HOSTS = ['*']

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = False
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'site@zestedesavoir.com'
#EMAIL_HOST_PASSWORD = 'to-fill'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 4

MEDIA_ROOT = '/home/{{zds_unix_user}}/data/media'

STATIC_ROOT = '/home/{{zds_unix_user}}/data/static'
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.CachedStaticFilesStorage"


LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'formatters': {
       'verbose': {
           'format': '[%(levelname)s] -- %(asctime)s -- %(module)s : %(message)s'
       },
       'simple': {
           'format': '[%(levelname)s] %(message)s'
       },
   },
   'handlers': {
        'django_log':{
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{{zds_app_name}}/logging.django.log',
            'formatter': 'verbose'
        },
        'debug_log':{
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{{zds_app_name}}/debug.django.log',
            'formatter': 'verbose'
        },
        'generator_log':{
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{{zds_app_name}}/generator.log',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
   },
   'loggers': {
        'django': {
            'handlers': ['django_log'],
            'propagate': True,
            'level': 'WARNING',
        },
        'zds': {
            'handlers': ['django_log'],
            'propagate': True,
            'level': 'WARNING',
        },
        'django.request': {
            'handlers': ['mail_admins', 'django_log'],
            'level': 'ERROR',
            'propagate': False,
        },
        'generator': {
            'handlers': ['generator_log'],
            'level': 'WARNING',
        }
    }
}

# https://docs.djangoproject.com/en/stable/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')


##### Dependencies settings #####


# easy-thumbnails
# http://easy-thumbnails.readthedocs.io/en/2.1/ref/settings/
THUMBNAIL_OPTIMIZE_COMMAND = {
    'png': '/usr/bin/optipng {filename}',
    'gif': '/usr/bin/optipng {filename}',
    'jpeg': '/usr/bin/jpegoptim {filename}'
}

# Pandoc settings
PANDOC_LOC = '/usr/local/bin/'
PANDOC_LOG = '/var/log/{{zds_app_name}}/pandoc.log'
PANDOC_LOG_STATE = True
# fix for Gandi
PANDOC_PDF_PARAM = ("--latex-engine=xelatex "
                    "--template={} -s -S -N "
                    "--toc -V documentclass=scrbook -V lang=francais "
                    "-V mainfont=Merriweather -V monofont=\"SourceCodePro-Regular\" "
                    "-V fontsize=12pt -V geometry:margin=1in ".format('/opt/{{zds_app_name}}/assets/tex/template.tex'))

# Sentry (+ raven, the Python Client)
# https://docs.getsentry.com/hosted/clients/python/integrations/django/
# RAVEN_CONFIG = {
#    'dsn': 'to-fill'
#    'dsn': 'to-fill'
# }

# python-social-auth
# http://psa.matiasaguirre.net/docs/configuration/django.html
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'zds.member.models.save_profile',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)
# KEEP THIS SECRET !!
SOCIAL_AUTH_ACEBOOK_KEY = 'to-fill'
SOCIAL_AUTH_ACEBOOK_SECRET = 'to-fill'
SOCIAL_AUTH_WITTER_KEY = 'to-fill'
SOCIAL_AUTH_WITTER_SECRET = 'to-fill'
SOCIAL_AUTH_OOGLE_OAUTH2_KEY = 'to-fill'
SOCIAL_AUTH_OOGLE_OAUTH2_SECRET = 'to-fill'
SOCIAL_AUTH_ANITIZE_REDIRECTS = 'to-fill'

# Django reCAPTCHA
# https://github.com/praekelt/django-recaptcha
USE_CAPTCHA = False
NOCAPTCHA = True   # Use the "No Captcha engine"
RECAPTCHA_USE_SSL = True
# KEEP THIS SECRET !!
RECAPTCHA_UBLIC_KEY = 'to-fill'
RECAPTCHA_RIVATE_KEY = 'to-fill'


##### ZdS settings #####


# forum
# ZDS_APP['forum']['beta_forum_id'] = 23

# member
# ZDS_APP['member']['anonymous_account'] = 'anonyme'
# ZDS_APP['member']['external_account'] = 'Auteur externe'
# ZDS_APP['member']['bot_account'] = 'Clem'

# site
ZDS_APP['site']['url'] = 'https://zestedesavoir.com'
ZDS_APP['site']['association']['email'] = 'communication@zestedesavoir.com'
ZDS_APP['site']['association']['fee'] = u'(montant en attente de procédures administratives)'
ZDS_APP['site']['googleAnalyticsID'] = 'to-fill'
ZDS_APP['site']['googleTagManagerID'] = 'to-fill'

# content
#ZDS_APP['content']['build_pdf_when_published'] = False
ZDS_APP['article']['repo_path'] = '/home/{{zds_unix_user}}/data/articles-data'
ZDS_APP['content']['repo_private_path'] = '/home/{{zds_unix_user}}/data/contents-private'
ZDS_APP['content']['repo_public_path'] = '/home/{{zds_unix_user}}/data/contents-public'
ZDS_APP['content']['extra_content_generation_policy'] = 'WATCHDOG'

# Vote anonymisation - cf v18 : https://goo.gl/L6X4hw
VOTES_ID_LIMIT = 0

# tags in menu
TOP_TAG_MAX = 5

# path for old tutorials for Site du Z&ro
SDZ_TUTO_DIR = '/home/zds/tutos_sdzv3/Sources_md'

# Force HTTPS for logged users
# FORCE_HTTPS_FOR_MEMBERS = True
# ENABLE_HTTPS_DECORATOR = True

# visual changes
#ZDS_APP['visual_changes'] = ['snow', 'clem-christmas']
# ZDS_APP['visual_changes'] = ['clem-halloween']