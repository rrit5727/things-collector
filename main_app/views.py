from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

@login_required
def dogs_index(request):
    dogs = Dog.objects.filter(user=request.user)
    # Another query
    # dogs = request.user.dog_set.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })

@login_required
def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    id_list = dog.parks.all().values_list('id')
    parks_dog_doesnt_goto = Park.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', 
        {'dog': dog, 'feeding_form': feeding_form,
         'parks': parks_dog_doesnt_goto
    })


class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age']
    # success_url = '/dogs/{dog_id}'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # let the CreateView's form_valid method do its work
        return super().form_valid(form)
    


class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs'

@login_required 
def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = dog_id
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)

class ParkList(LoginRequiredMixin, ListView):
    model = Park

class ParkDetail(LoginRequiredMixin, DetailView):
    model = Park

class ParkCreate(LoginRequiredMixin, CreateView):
    model = Park
    fields = '__all__'
    success_url = reverse_lazy('parks_list')

class ParkUpdate(LoginRequiredMixin, UpdateView):
    model = Park
    fields = '__all__'
    
class ParkDelete(LoginRequiredMixin, DeleteView):
    model = Park
    success_url = '/parks/'

@login_required
def assoc_park(request, dog_id, park_id):
    Dog.objects.get(id=dog_id).parks.add(park_id)
    return redirect('detail', dog_id=dog_id)

 
def signup(request): 
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save the user to the db
            user = form.save()
            # automatically login the new user
            login(request, user)
            return redirect('index')
        else: 
            erorr_message = 'Invalid sign up - try again'
    # A bad POST or GET request, so render signup template
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)   

