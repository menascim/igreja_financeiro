import os
import django

# Configure o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'igreja_financeiro.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Cria o usuário se não existir
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@piber.com',
        password='admin123'  # 🔴 Altere para produção!
    )
    print("Superusuário criado com sucesso!")
else:
    print("Superusuário já existe.")
