from django.shortcuts import render

dogs = [
  {'name': 'bingo', 'breed': 'jack russel', 'description': 'tenacious terrier', 'age': 3},
  {'name': 'Woofles', 'breed': 'Cholotzinquitli', 'description': 'Charming', 'age': 2},
]

def home(request):
    return render(request, 'home.html')