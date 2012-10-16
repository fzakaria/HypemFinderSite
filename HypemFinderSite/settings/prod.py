"""Development settings and globals."""
from common import *
from os.path import join, normpath

########## DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hypem_db',                      # Or path to database file if using sqlite3.
        'USER': 'djangouser',                      # Not used with sqlite3.
        'PASSWORD': '123456',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
########## END DATABASE CONFIGURATION

########## LOGGING CONFIGURATION
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] - %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        #Dump every message to /dev/null
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        #Create a time based rotating file every day
        'rotating_file': {                 
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler', 
            'formatter': 'standard',
            'when' : 'D',    
            'filename': join(SITE_ROOT, 'logs', 'hypemfinder.log')
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'hypemfinder': {
            'handlers': ['rotating_file'],
            'level': 'INFO',
        },
    }
}
##########END LOGGING CONFIGURATION


