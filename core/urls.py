from django.urls import path
from .views import register  # Importe a nova view

urlpatterns = [
    # ... outras URLs ...
    path('cadastro/', register, name='cadastro'),
]
