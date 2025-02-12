from django.contrib import admin
from django.urls import path, include  # Adicione 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Inclua as URLs do app "core"
]
