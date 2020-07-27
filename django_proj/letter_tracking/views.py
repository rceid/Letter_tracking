from django.shortcuts import render
from .models import Letter


def home(request):
    context ={
        'letters': Letter.objects.all()
    }
    return render(request, 'letter_tracking/home.html', context)

def about(request):
    return render(request, 'letter_tracking/about.html', {'title': '#Quedusallife'})
