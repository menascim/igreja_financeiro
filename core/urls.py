from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.register, name='cadastro'),
]
