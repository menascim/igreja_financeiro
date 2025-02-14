# core/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Contribution
from .models import CustomUser
from django.core.validators import EmailValidator  # Adicione esta linha


# Formulário de login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        validators=[EmailValidator(message="E-mail inválido!")],  # Uso correto
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    
    email = forms.EmailField(
        validators=[EmailValidator(message="Insira um e-mail válido!")],  # Corrigido
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['valor', 'metodo']
        widgets = {
            'metodo': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            })
        }

    # Opcional: Para personalizar o label ou traduzir
    metodo = forms.ChoiceField(
        label="Método de Pagamento",
        choices=Contribution.PAYMENT_METHODS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
