from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileView
from .views import ProfileView, add_contribution


urlpatterns = [
   path('', ProfileView.as_view(), name='home'),
    path('cadastro/', views.register, name='cadastro'),
    path('login/', views.login_view, name='login'),  # Usando a view personalizada
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('contributions/add/', views.add_contribution, name='add_contribution'),
    path('exportar/', views.export_contributions, name='export'),
]


