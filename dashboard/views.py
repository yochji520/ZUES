from django.shortcuts import render
from django.shortcuts import render, HttpResponse


def index_view(request):
    return render(request, 'index.html')


def dashboard_view(request):
    return render(request, 'welcome.html')