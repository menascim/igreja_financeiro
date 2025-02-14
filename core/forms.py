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
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(required=True, label="Nome")  # Novo campo

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'email', 'phone', 'password1', 'password2']  # Campo adicionado

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
