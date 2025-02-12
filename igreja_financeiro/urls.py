from django.urls import path
from core import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('export/', views.export_contributions, name='export'),
]
