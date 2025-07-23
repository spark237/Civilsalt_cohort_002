from django.shortcuts import render
from .models import person

# Create your views here.
def home(request):
    context = {} 
    return render(request, 'Listapp/home.html', context)