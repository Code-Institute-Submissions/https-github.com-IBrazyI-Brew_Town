from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings


def index(request):

    return render(request, 'home/index.html')

