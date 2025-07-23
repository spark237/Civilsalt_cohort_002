from django.shortcuts import render
from .models import person

# Create your views here.
def home(request):
    people = person.objects.all() 
    return render(request, 'Listapp/home.html', {'people': people})