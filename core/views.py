from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Contribution
from .forms import LoginForm, ContributionForm
import pandas as pd
from twilio.rest import Client
import os

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    contributions = Contribution.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.user = request.user
            contribution.save()
            send_whatsapp_confirmation(request.user.phone)  # Notificação via WhatsApp
            return render(request, 'profile.html', {'user': request.user})
    else:
        form = ContributionForm()
    return render(request, 'profile.html', {'contributions': contributions, 'form': form})

@login_required
def export_contributions(request):
    contributions = Contribution.objects.filter(user=request.user)
    df = pd.DataFrame(list(contributions.values('amount', 'date', 'payment_method')))
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="minhas_contribuicoes.xlsx"'
    df.to_excel(response, index=False)
    return response

def send_whatsapp_confirmation(phone):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body='🎉 Sua contribuição foi registrada com sucesso! Obrigado.',
        from_='whatsapp:+14155238886',  # Número do Twilio Sandbox
        to=f'whatsapp:+55{phone}'       # Formato: +5511999999999
    )
    return message.sid
