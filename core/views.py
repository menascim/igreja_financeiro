from dal import autocomplete
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, ContributionForm
from .models import Contribution
from .forms import ContributionForm
from .services import send_whatsapp_notification
import pandas as pd
from twilio.rest import Client
import os

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contributions'] = Contribution.objects.filter(user=self.request.user)
        context['form'] = ContributionForm()  # Certifique-se de que esta linha está indentada corretamente
        return context  # Esta linha também deve estar alinhada com o início do métod

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name', '')  # Adiciona first_name
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def profile(request):
    contributions = Contribution.objects.filter(user=request.user).order_by('-data')  # Corrigido para 'data'
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.user = request.user
            contribution.save()
            try:
                # Corrigido para usar a função correta
                send_whatsapp_confirmation(request.user.phone)
            except Exception as e:
                print(f"Erro ao enviar WhatsApp: {str(e)}")
            return redirect('profile')
    else:
        form = ContributionForm()
    return render(request, 'profile.html', {
        'contributions': contributions,
        'form': form
    })

# views.py (trecho atualizado)
@login_required
def add_contribution(request):
    is_admin = request.user.is_staff
    
    if request.method == 'POST':
        form = ContributionForm(request.POST, is_admin=is_admin)
        if form.is_valid():
            contribution = form.save(commit=False)
            
            if not is_admin:
                contribution.user = request.user  # Usuário normal: vincula a si mesmo
                
            contribution.save()
            return redirect('profile')
    else:
        form = ContributionForm(is_admin=is_admin)
    
    return render(request, 'admin/add_contribution.html', {'form': form})
            
            # Envia WhatsApp
            try:
                send_whatsapp_confirmation(
                    request.user.phone.replace("+55", ""),  # Remove +55 se existir
                    contribution.valor
                )
            except Exception as e:
                print(f"Erro fora do Twilio: {str(e)}")
            
            return redirect('profile')
    
    return redirect('profile')
    
@login_required
def export_contributions(request):
    contributions = Contribution.objects.filter(user=request.user)
    df = pd.DataFrame(list(contributions.values('amount', 'date', 'payment_method')))
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="contribuicoes.xlsx"'
    df.to_excel(response, index=False)
    return response

def send_whatsapp_confirmation(phone, valor):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"✅ Recebemos sua contribuição, Financeiro Piber! Valor: R$ {valor}",
            from_='whatsapp:+14155238886',
            to=f'whatsapp:+55{phone}'  # Remove o "+55" se já incluso no número
        )
        return message.sid
    except Exception as e:
        print(f"Erro ao enviar WhatsApp: {str(e)}")

def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Login automático
            login(request, user) 
            
            # Mensagem de boas-vindas via WhatsApp
            mensagem = (
                f"🎉 Cadastro realizado com sucesso!\n"
                f"Nome: {user.first_name}\n"
                f"Telefone: {user.phone}"
            )
            send_whatsapp_notification(user.phone, mensagem)
            
            return redirect('profile')  # Redirecionamento correto

class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = CustomUser.objects.all()
        if self.q:
            qs = qs.filter(
                Q(first_name__icontains=self.q) | 
                Q(phone__icontains=self.q)
            )
        return qs
