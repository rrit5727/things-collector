from django.shortcuts import render

from .models import Dog

# dogs = [
#   {'name': 'bingo', 'breed': 'jack russel', 'description': 'tenacious terrier', 'age': 3},
#   {'name': 'Woofles', 'breed': 'Choloitzcuintli', 'description': 'Charming', 'age': 2},
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })