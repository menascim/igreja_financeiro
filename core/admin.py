# core/admin.py (adicione este arquivo)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('phone', 'email')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
