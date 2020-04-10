from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'ugaach/home.html')


def about(request):
    return render(request, 'ugaach/about.html')


def feedback(request):
    return render(request, 'ugaach/feedback.html')

