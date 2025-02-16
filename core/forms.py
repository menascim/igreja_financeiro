# core/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import EmailValidator
from .models import Contribution, CustomUser
from dal_select2 import widgets

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        validators=[EmailValidator(message="Insira um e-mail válido!")],
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ContributionForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=widgets.ModelSelect2(
            url='user-autocomplete',
            attrs={'data-html': True}
        ),
        required=False,
        label="Membro Destinatário"  # Correção: vírgula adicionada
    )

    metodo = forms.ChoiceField(
        label="Método de Pagamento",
        choices=Contribution.PAYMENT_METHODS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Contribution
        fields = ['user', 'valor', 'metodo']
        widgets = {
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            })
        }

    def __init__(self, *args, **kwargs):
        is_admin = kwargs.pop('is_admin', False)
        super().__init__(*args, **kwargs)

        if not is_admin:
            del self.fields['user']
        else:
            self.fields['user'].queryset = CustomUser.objects.filter(is_staff=False)
            self.fields['user'].required = True
        # Removido o else duplicado
