from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.parse(CLEAR_DB_URL)

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://geekshtop.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'geeknshtuff@outlook.com'



