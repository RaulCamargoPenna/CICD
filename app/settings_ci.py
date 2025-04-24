# settings_ci.py

from .settings import *  # Importa tudo do settings padrão

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Banco em memória para testes
    }
}

# Outras configs específicas de testes se quiser
DEBUG = False
