# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('export/', views.export_contributions, name='export'),
]
