from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from .models import ContactMessage


def index(request):
    return render(request, 'core/index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(**form.cleaned_data)
            messages.success(request, '留言已提交！')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})