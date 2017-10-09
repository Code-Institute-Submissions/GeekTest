from base import *
import dj_database_url

DEBUG = False



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CLEAR_DB_URL = os.environ.get("CLEARDB_DATABASE_URL", "")

DATABASES['default'] = dj_database_url.parse(CLEAR_DB_URL)

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'geekstuff.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'geeknshtuff@outlook.com'

SITE_URL = 'http://geekstuff.herokuapp.com'
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