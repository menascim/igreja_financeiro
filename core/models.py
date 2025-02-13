from django.contrib.auth.models import AbstractUser
from django.db import models

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

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)

    def __str__(self):
        return f"{self.user.username} - R${self.amount}"
