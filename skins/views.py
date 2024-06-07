from django.shortcuts import render, redirect, get_object_or_404
from .models import Skin
from .forms import SkinForm

def skin_list(request):
    skins = Skin.objects.all()
    return render(request, 'skin_list.html', {'skins': skins})

def contato(request):
    return render(request, 'contato.html')