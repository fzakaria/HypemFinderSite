"""Common settings and globals."""
import sys
from os.path import abspath, basename, dirname, join, normpath

########## PATH CONFIGURATION
# Absolute filesystem path to the top-level project folder.
SITE_ROOT = dirname(dirname(dirname(abspath(__file__))))

# Site name.
SITE_NAME = basename(SITE_ROOT)

# Absolute filesystem path to the secret file which holds this project's
# SECRET_KEY. Will be auto-generated the first time this file is interpreted.
SECRET_FILE = normpath(join(SITE_ROOT, 'deploy', 'SECRET'))

# Add all necessary filesystem paths to our system path so that we can use
# python import statements.
sys.path.append(SITE_ROOT)
sys.path.append(normpath(join(SITE_ROOT, 'apps')))
sys.path.append(normpath(join(SITE_ROOT, 'libs')))
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# Disable debugging by default.
DEBUG = False
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## MANAGER CONFIGURATION
# Admin and managers for this project. These people receive private site
# alerts.
ADMINS = (
     ('Farid Zakaria', 'farid.m.zakaria@gmail.com'),
)
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## GENERAL CONFIGURATION
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# The ID, as an integer, of the current site in the django_site database table.
# This is used so that application data can hook into specific site(s) and a
# single database can manage content for multiple sites.
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
########## END GENERAL CONFIGURATION


########## STATIC FILE CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT =  normpath(join(SITE_ROOT, 'static'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
########## END STATIC FILE CONFIGURATION
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
########## END TEMPLATE CONFIGURATION

########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION

########## URL CONFIGURATION
ROOT_URLCONF = '{}.urls'.format( SITE_NAME )
########## END URL CONFIGURATION

########## APP CONFIGURATION
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'hypemfinder',
	'widget_tweaks',
)
########## END APP CONFIGURATION

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{}.wsgi.application'.format( SITE_NAME )


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
            'format': '%(levelname)s %(message)s'
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
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
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
            'handlers': ['rotating_file','console'],
            'level': 'DEBUG',
        },
    }
}
##########END LOGGING CONFIGURATION

########## KEY CONFIGURATION
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'g48u7jc54y4a%vj5t-1v__e4a7rkj*d@!uz=me&amp;kgb&amp;5z8tdk!'
