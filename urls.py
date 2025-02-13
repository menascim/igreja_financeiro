from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Inclui as URLs do app "core"
    path('accounts/', include('django.contrib.auth.urls')),  # URLs padrão de autenticação (login/logout)
    path(settings.ADMIN_URL, admin.site.urls),  # Usa o caminho configurado
]
