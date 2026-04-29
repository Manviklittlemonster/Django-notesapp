import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DEBUG = False
ALLOWED_HOSTS = ['localhost', '3.109.54.221', '<EC2-Public-IP>']
