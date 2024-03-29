from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Project
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
import requests
from django.template.loader import get_template
from django.contrib import messages


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'project': projects})


# contact form view

#  def contact_view(request):
#    form_class = ContactForm    # form class
#
#   # new logic
#   if request.method == 'POST':
#        form = form_class(data=request.POST)
#
#        if form.is_valid():
#            name = request.POST.get('name')
#            email = request.POST.get('email')
#            message = request.POST.get('message', '')
#
#            # Email the profile with the
#            # contact information
#            template = get_template('contact.html.txt')
#            context = {
#                'contact_name': name,
#                'contact_email': email,
#                'contact_message': message,
#            }
#            content = template.render(context)
#
#            email = EmailMessage(
#                name,
#                content,
#                "Your website" + '',
#                ['gabrielufot23@gmail.com'],
#                headers={'Reply-To': email}
#            )
#            email.send()
#            messages.success(request, 'Message sent successfully')
#            return redirect('contact')
#    return render(request, 'contact.html', {'form': form_class})


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            try:
                send_mail(subject, message, email, ['gabrielufot23@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return HttpResponse('success! Thanks for your message')


def apod(request):
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=9PywoHIu6W7m6IPrgkob9hhbgBWfhzbL1KJQFwRo')
    run = response.json()
    return render(request, 'apod.html', {
        'data': run['data'],
        'hd': run['True']
    })
