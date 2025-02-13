from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileView

urlpatterns = [
    path('perfil/', views.profile, name='profile'),
    path('', views.profile, name='profile'),  # Página inicial (após login)
    path('cadastro/', views.register, name='cadastro'),  # Cadastro de usuários
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('exportar/', views.export_contributions, name='export'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('health/', health_check, name='health_check'),
]


