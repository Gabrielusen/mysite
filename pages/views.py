from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Project
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
import requests
from django.template.loader import get_template


# class HomePageView(ListView):
#     template_name = 'home.html'
#     model = Project
#     field = ('name', 'email', 'subject', 'message')


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'project': projects})


# contact form view

def contact_view(request):
    form_class = ContactForm    # form class

    # new logic
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('contact.html.txt')
            context = {
                'contact_name': name,
                'contact_email': email,
                'contact_message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                name,
                content,
                "Your website" + '',
                ['gabrielufot23@gmail.com'],
                headers={'Reply-To': email}
            )
            email.send()
            return redirect('contact')
    return render(request, 'contact.html', {'form': form_class})


def success_view(request):
    return HttpResponse('Success! Thank you for your message.')


def apod(request):
    url_apod = 'https://api.nasa.gov/planetary/apod?api_key=9PywoHIu6W7m6IPrgkob9hhbgBWfhzbL1KJQFwRo'
    date = '2020-05-22'
    params = {
        'date': date,
        'hd': 'True'
    }
    return render(request, 'apod.html', {'params': params})
