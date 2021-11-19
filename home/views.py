from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request, 'home/index.html')


def newsletter_email(request, email):
    if method == GET:
        email = request.GET.get('email')

        send_mail('Newsletter',
                    'Welcome {{ user_email }} to the brewtown newsletter!',
                     settings.DEFAULT_FROM_EMAIL,
                      user_email)