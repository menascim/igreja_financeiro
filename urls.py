from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Inclui as URLs do app "core"
    path('accounts/', include('django.contrib.auth.urls')),  # URLs padrão de autenticação (login/logout)
]
