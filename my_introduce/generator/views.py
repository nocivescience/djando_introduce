from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'generator/home.html', {'name': 'Nocive'})
def about(request):
    return render(request, 'generator/about.html',{'name': 'About'})