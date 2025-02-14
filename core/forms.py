# core/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Contribution
from .models import CustomUser

# Formulário de login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistrationForm(UserCreationForm):
    phone = forms.CharField(
        label="Telefone",
        widget=forms.TextInput(attrs={
            'placeholder': '+5511999999999',
            'class': 'form-control'
        })
    )
    
    email = forms.EmailField(
        validators=[validate_email],
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
            'metodo': forms.Select(attrs={'class': 'form-control'}),  # Widget Select
        }

    # Opcional: Para personalizar o label ou traduzir
    metodo = forms.ChoiceField(
        label="Método de Pagamento",
        choices=Contribution.PAYMENT_METHODS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
