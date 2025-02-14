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
            try:
                user = form.save()
                return redirect('login')
            except IntegrityError as e:
                form.add_error('phone', 'Este telefone já está cadastrado!')
        else:
            print(form.errors)
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
    contributions = Contribution.objects.filter(user=request.user).order_by('-date')
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.user = request.user
            contribution.save()
            try:
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

@login_required
def add_contribution(request):
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.user = request.user
            contribution.save()
    return redirect('profile')
    
@login_required
def export_contributions(request):
    contributions = Contribution.objects.filter(user=request.user)
    df = pd.DataFrame(list(contributions.values('amount', 'date', 'payment_method')))
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="contribuicoes.xlsx"'
    df.to_excel(response, index=False)
    return response

def send_whatsapp_confirmation(phone):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body='🎉 Sua contribuição foi registrada com sucesso! Obrigado.',
        from_='whatsapp:+14155238886',
        to=f'whatsapp:+55{phone}'
    )
    return message.sid
