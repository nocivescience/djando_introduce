from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
def home(request):
    return render(request, 'generator/home.html', {'name': 'Nocive'})
def about(request):
    return render(request, 'generator/about.html',{'name': 'About'})
def generate_password(request):
    generate_password=''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length', 12))
    for x in range(length):
        generate_password += np.random.choice(characters)
    return render(request, 'generator/password.html', {'password': generate_password})