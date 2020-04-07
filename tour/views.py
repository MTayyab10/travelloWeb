from django.shortcuts import render
from .models import Tour

# Create your views here.
def index(request):
    cities = Tour.objects.all()
    return render(request, 'index.html', {'cities':cities})
def about(request):
    return render(request, 'About.html')
