import sys
import os
from pathlib import Path
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'src'))

SECRET_KEY = os.getenv('SECRET_KEY', 'secret-dev')  # Altere em produção!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

DEBUG = False
ALLOWED_HOSTS = ['https://igreja-financeiro.onrender.com', 'localhost']
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para arquivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'igreja_financeiro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'core/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'igreja_financeiro.wsgi.application'

# Banco de dados (usando PostgreSQL no Render.com)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Piber',
        'USER': 'piber_user',
        'PASSWORD': 'pux332FGmio65ysWqKDJFjZcZQjaFe8S',
        'HOST': 'postgresql://piber_user:pux332FGmio65ysWqKDJFjZcZQjaFe8S@dpg-cumddd5umphs738hbiog-a.oregon-postgres.render.com/piber',
        'PORT': '5432',
    }
}

    )
}

AUTH_USER_MODEL = 'core.CustomUser'  # Modelo de usuário personalizado

# Configurações de login
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_REDIRECT_URL = '/login/'

# Arquivos estáticos (CSS, JS, imagens)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
