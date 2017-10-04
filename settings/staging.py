from base import *
import dj_database_url

DEBUG = False


# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}



# Paypal environment variables
PAYPAL_NOTIFY_URL = 'http://geekstuff.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'http://geeknshtuff@outlook.com'

SITE_URL = 'https://geekstuff.herokuapp.com'
ALLOWED_HOSTS.append('geekstuff.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}