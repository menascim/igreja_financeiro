from django.urls import path
from . import views import register 

urlpatterns = [
    path('', views.profile, name='profile'),  # Rota raiz
    path('login/', views.login_view, name='login'),
    path('export/', views.export_contributions, name='export'),
    path('cadastro/', register, name='cadastro'),
]
