from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=20, 
        unique=True,
        error_messages={'unique': 'Este telefone já está registrado!'}
    )
class Contribution(models.Model):
    PAYMENT_METHODS = [
        ('PIX', 'PIX'),
        ('Cartão', 'Cartão de Crédito/Débito'),
        ('Dinheiro', 'Dinheiro'),
    ]

    metodo = models.CharField(
        max_length=50,
        choices=PAYMENT_METHODS,  # Adicione as opções aqui
        default='PIX'  # Opcional: defina um valor padrão
    )
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - R${self.amount}"
