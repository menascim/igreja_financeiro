from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileView
from .views import Profile, export_contributions

urlpatterns = [
    path('perfil/', views.profile, name='profile'),
    path('', views.profile, name='profile'),  # Página inicial (após login)
    path('cadastro/', views.register, name='cadastro'),  # Cadastro de usuários
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('exportar/', views.export_contributions, name='export'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('export-contrib/', export_contributions, name='export_contributions'),
]


