from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import (
    ProfileView,
    add_contribution,
    UserAutocomplete,
    export_contributions
)

urlpatterns = [
    path('', ProfileView.as_view(), name='home'),
    path('cadastro/', views.register, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('contributions/add/', views.add_contribution, name='add_contribution'),
    path('exportar/', views.export_contributions, name='export'),
    path('user-autocomplete/', UserAutocomplete.as_view(), name='user-autocomplete'),
]
