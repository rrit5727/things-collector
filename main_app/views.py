from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Dog
from .forms import FeedingForm

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

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', 
        {'dog': dog, 'feeding_form': feeding_form
    })

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/{dog_id}'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs'