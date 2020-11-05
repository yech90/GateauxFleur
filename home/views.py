from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from .forms import contactForm

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def generic(request):
    return render(request, 'generic.html', {})

def contactView(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            recipients = ['gateauxfleur.paris@gmail.com']
            send_mail(name, message, sender, recipients)
            return render(request, 'index.html', {'form':form})
    else:
        form = contactForm()

    return render(request, 'index.html', {'form':form})

