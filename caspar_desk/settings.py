from settings_base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'QGHP8h328gp9h2qoigøh1jæøi2qjhrjoiwhaøoishfø3fewq''

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
