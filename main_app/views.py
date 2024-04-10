from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
 
from .models import Dog, Park
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
    id_list = dog.parks.all().values_list('id')
    parks_dog_doesnt_goto = Park.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', 
        {'dog': dog, 'feeding_form': feeding_form,
         'parks': parks_dog_doesnt_goto
    })

class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/dogs/{dog_id}'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs'

def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = dog_id
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)

class ParkList(ListView):
    model = Park

class ParkDetail(DetailView):
    model = Park

class ParkCreate(CreateView):
    model = Park
    fields = '__all__'
    success_url = reverse_lazy('parks_list')

class ParkUpdate(UpdateView):
    model = Park
    fields = '__all__'
    
class ParkDelete(DeleteView):
    model = Park
    success_url = '/parks/'

def assoc_park(request, dog_id, park_id):
    Dog.objects.get(id=dog_id).parks.add(park_id)
    return redirect('detail', dog_id=dog_id)