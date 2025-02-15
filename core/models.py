from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            RegexValidator(  # Agora reconhecido
                regex=r'^\+55\d{10,11}$',
                message="Formato: +5511999999999"
            )
        ],
        error_messages={'unique': 'Este telefone já está registrado!'}
    )
    class Meta:
        permissions = [
            ("pode_registrar_contribuicao", "Pode registrar contribuições para outros membros"),
        ]
class Contribution(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        verbose_name="Membro"
    )
    PAYMENT_METHODS = [
        ('PIX', 'PIX'),
        ('Cartão', 'Cartão de Crédito/Débito'),
        ('Dinheiro', 'Dinheiro'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(  # Apenas uma declaração do campo
        max_length=50,
        choices=PAYMENT_METHODS,
        default='PIX'
    )
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - R${self.valor}"  # Corrigido para 'valor'
