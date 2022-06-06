from django.shortcuts import render
from .models import Tour

# Create your views here.

def main_page(request):
    tours = Tour.objects.all()
    context = {
        'tours': tours
    }
    return render(request, 'mainapp/index.html', context)
