import sys
import os
from pathlib import Path
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'src'))

SECRET_KEY = os.getenv('SECRET_KEY', 'secret-dev')  # Altere em produção!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

DEBUG = True
ALLOWED_HOSTS = ['*']
]

INSTALLED_APPS = [
    'dal',
    'dal_select2',
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
    'default': dj_database_url.config(default='postgres://piber_user:pux332FGmio65ysWqKDJFjZcZQjaFe8S@dpg-cumddd5umphs738hbiog-a.oregon-postgres.render.com/piber')
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

# Para desenvolvimento (DEBUG=True)
CSRF_COOKIE_SECURE = False    # Não requer HTTPS
CSRF_COOKIE_HTTPONLY = False  # Permite acesso via JS (opcional)
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000']  # Domínios permitidos

# Para produção (DEBUG=False)
CSRF_TRUSTED_ORIGINS = ['https://igreja-financeiro.onrender.com']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# settings.py
CSRF_COOKIE_SECURE = True  # True em produção, False em desenvolvimento
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000', 
    'https://igreja-financeiro.onrender.com'
]
