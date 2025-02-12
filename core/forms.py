# core/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Contribution

# Formulário de login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# Formulário de contribuição
class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['amount', 'payment_method']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }
