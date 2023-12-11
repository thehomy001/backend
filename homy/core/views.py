from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def home(request, *args, **kwargs):
    return JsonResponse({"message": "This is core"})

def success(request,uid):
    template = render_to_string('core/email_template.html')
    email = EmailMessage(
        'Thanks you for signing in',
        template,
        settings.EMAIL_HOST_USER,
        ['pushkar@thehomy.co'],
    )
    email.fail_silently=False
    email.send()
