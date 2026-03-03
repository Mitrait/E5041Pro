from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def docshell(request):
    return render(request, 'docshell.html')

def expert(request):
    return render(request, 'expert.html')

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return HttpResponse('Заявка отправлена!')
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})

def privacy(request):
    return render(request, 'privacy.html')

def consent(request):
    return render(request, 'consent.html')