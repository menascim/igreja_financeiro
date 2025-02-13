from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),  # Página inicial (após login)
    path('login/', views.login_view, name='login'),  # Login personalizado (se necessário)
    path('cadastro/', views.register, name='cadastro'),  # Cadastro de usuários
]
