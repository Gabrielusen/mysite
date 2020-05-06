from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Project
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


# class HomePageView(ListView):
#     template_name = 'home.html'
#     model = Project
#     field = ('name', 'email', 'subject', 'message')


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'project': projects})


def contact_view(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']

        # send an email
        send_mail(
            message_subject,  # subject
            message,  # message
            message_email,  # email
            ['gabrielufot23@gmail.com']  # To email
        )

        return render(request, 'contact.html', {'message_name': message_name})

    return render(request, 'contact.html', {})


def success_view(request):
    return HttpResponse('Success! Thank you for your message.')
