from fancyfeast.settings.base import *

# Override base.py settings here
# In production, change database to Postgres
DEBUG = False
ALLOWED_HOSTS = [*]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    from fancyfeast.settings.local import *
except:
    # Can tell user to create local.py
    pass