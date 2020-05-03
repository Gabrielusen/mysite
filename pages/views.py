from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Project
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Email
from django.core.mail import send_mail, BadHeaderError


class HomePageView(ListView):
    template_name = 'home.html'
    model = Project


def contact_view(request):
    if request.method == 'GET':
        form = Email()
    else:
        form = Email(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['gabrielufot23@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success_view(request):
    return HttpResponse('Success! Thank you for your message.')
