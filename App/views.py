from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def mehendi(request):
    return render(request, 'mehendi.html')

def contact(request):
    return render(request, 'contact.html')

def birthday(request):
    return render(request, 'birthday.html')

def fruits_catering(request):
    return render(request, 'fruits_catering.html')

def salad_dressing(request):
    return render(request, 'salad_dressing.html')

def juice_catering(request):
    return render(request, 'juice_catering.html')
