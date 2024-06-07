from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

def contato(request):
    return render(request, 'contato.html')