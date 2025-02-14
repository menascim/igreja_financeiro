from django.conf import settings
from twilio.rest import Client

def send_whatsapp_notification(phone, message):
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=settings.TWILIO_WHATSAPP_NUMBER,
            to=f'whatsapp:{phone}'
        )
        return True
    except Exception as e:
        print(f"Erro ao enviar WhatsApp: {str(e)}")
        return False
