from django.shortcuts import render

# Create your views here.

# Its just like controller same as ruby on rails


def home(request):
    return render(request, 'home.html')


def customer_page(request):
    return render(request, 'home.html')


def courier_page(request):
    return render(request, 'home.html')
